"""Tests for adopt/claude/hooks/live_write_guard.py. Standard library only.

Run: python3 -m unittest discover -s tests -v
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "adopt" / "claude"
HOOK = KIT / "hooks" / "live_write_guard.py"


def bash_event(command: str, cwd: str = "") -> dict:
    return {
        "session_id": "test",
        "cwd": cwd,
        "hook_event_name": "PreToolUse",
        "tool_name": "Bash",
        "tool_input": {"command": command},
    }


class GuardTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.project = Path(self._tmp.name)
        (self.project / ".claude").mkdir()
        self.outputs: list[str] = []

    def tearDown(self) -> None:
        self._tmp.cleanup()
        for out in self.outputs:  # never "allow", in any case
            if out.strip():
                decision = json.loads(out)["hookSpecificOutput"]["permissionDecision"]
                self.assertNotEqual(decision, "allow")

    def write_config(self, text: str) -> None:
        (self.project / ".claude" / "live-write-patterns.json").write_text(text, encoding="utf-8")

    def run_hook(self, stdin: str, use_env: bool = True) -> subprocess.CompletedProcess:
        env = {k: v for k, v in os.environ.items() if k != "CLAUDE_PROJECT_DIR"}
        if use_env:
            env["CLAUDE_PROJECT_DIR"] = str(self.project)
        result = subprocess.run(
            [sys.executable, str(HOOK)], input=stdin, capture_output=True,
            text=True, env=env, cwd=self._tmp.name, timeout=30,
        )
        self.outputs.append(result.stdout)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def decision(self, result: subprocess.CompletedProcess) -> dict:
        out = json.loads(result.stdout)["hookSpecificOutput"]
        self.assertEqual(out["hookEventName"], "PreToolUse")
        return out

    def test_match_asks_with_command_in_reason(self) -> None:
        self.write_config(json.dumps({"patterns": [r"--live\b"]}))
        cmd = "python3 scripts/push.py --store test-1 --live"
        out = self.decision(self.run_hook(json.dumps(bash_event(cmd))))
        self.assertEqual(out["permissionDecision"], "ask")
        self.assertIn(cmd, out["permissionDecisionReason"])
        self.assertIn("risk-and-approval.md", out["permissionDecisionReason"])

    def test_long_command_is_truncated(self) -> None:
        self.write_config(json.dumps({"patterns": [r"--live\b"]}))
        cmd = "echo --live " + "x" * 500
        out = self.decision(self.run_hook(json.dumps(bash_event(cmd))))
        self.assertEqual(out["permissionDecision"], "ask")
        self.assertIn(cmd[:300] + "...", out["permissionDecisionReason"])
        self.assertNotIn(cmd, out["permissionDecisionReason"])

    def test_match_past_head_is_shown(self) -> None:
        self.write_config(json.dumps({"patterns": [r"--live\b"]}))
        cmd = "echo " + "a" * 400 + " ; ./w --live"
        out = self.decision(self.run_hook(json.dumps(bash_event(cmd))))
        self.assertEqual(out["permissionDecision"], "ask")
        reason = out["permissionDecisionReason"]
        self.assertIn("'--live'", reason)
        self.assertIn("; ./w --live", reason)
        self.assertIn(cmd[:300] + "...", reason)

    def test_guard_files_ask_even_without_config(self) -> None:
        for cmd in ("rm .claude/live-write-patterns.json",
                    "mv .claude/hooks/live_write_guard.py /tmp/x",
                    "git checkout -- .claude/settings.json",
                    "python3 -c \"open('.claude/settings.local.json','w')\""):
            with self.subTest(cmd=cmd):
                out = self.decision(self.run_hook(json.dumps(bash_event(cmd))))
                self.assertEqual(out["permissionDecision"], "ask")
                self.assertIn("guard's own files", out["permissionDecisionReason"])

    def test_guard_files_ask_with_config(self) -> None:
        self.write_config(json.dumps({"patterns": [r"--live\b"]}))
        out = self.decision(self.run_hook(json.dumps(bash_event("rm .claude/live-write-patterns.json"))))
        self.assertEqual(out["permissionDecision"], "ask")

    def test_match_uses_cwd_when_env_unset(self) -> None:
        self.write_config(json.dumps({"patterns": [r"--arm\b"]}))
        event = bash_event("make push --arm", cwd=str(self.project))
        out = self.decision(self.run_hook(json.dumps(event), use_env=False))
        self.assertEqual(out["permissionDecision"], "ask")

    def test_non_match_is_silent(self) -> None:
        self.write_config(json.dumps({"patterns": [r"--live\b"]}))
        result = self.run_hook(json.dumps(bash_event("python3 scripts/push.py --dry-run")))
        self.assertEqual(result.stdout, "")

    def test_empty_patterns_is_silent(self) -> None:
        self.write_config((KIT / "live-write-patterns.example.json").read_text(encoding="utf-8"))
        result = self.run_hook(json.dumps(bash_event("python3 scripts/push.py --live")))
        self.assertEqual(result.stdout, "")

    def test_non_bash_tool_is_silent(self) -> None:
        self.write_config(json.dumps({"patterns": [r"--live\b"]}))
        event = {"tool_name": "Edit", "tool_input": {"file_path": "a.txt", "new_string": "--live"}}
        result = self.run_hook(json.dumps(event))
        self.assertEqual(result.stdout, "")

    def test_missing_config_is_silent(self) -> None:
        result = self.run_hook(json.dumps(bash_event("python3 scripts/push.py --live")))
        self.assertEqual(result.stdout, "")

    def test_config_directory_asks(self) -> None:
        (self.project / ".claude" / "live-write-patterns.json").mkdir()
        out = self.decision(self.run_hook(json.dumps(bash_event("ls"))))
        self.assertEqual(out["permissionDecision"], "ask")
        self.assertIn("live-write guard misconfigured", out["permissionDecisionReason"])

    def test_empty_pattern_asks(self) -> None:
        self.write_config(json.dumps({"patterns": [""]}))
        out = self.decision(self.run_hook(json.dumps(bash_event("ls"))))
        self.assertEqual(out["permissionDecision"], "ask")
        self.assertIn("empty pattern", out["permissionDecisionReason"])

    def test_invalid_json_config_asks(self) -> None:
        self.write_config("{not json")
        out = self.decision(self.run_hook(json.dumps(bash_event("ls"))))
        self.assertEqual(out["permissionDecision"], "ask")
        self.assertIn("live-write guard misconfigured", out["permissionDecisionReason"])

    def test_patterns_not_a_list_asks(self) -> None:
        self.write_config(json.dumps({"patterns": "--live"}))
        out = self.decision(self.run_hook(json.dumps(bash_event("ls"))))
        self.assertEqual(out["permissionDecision"], "ask")
        self.assertIn("live-write guard misconfigured", out["permissionDecisionReason"])

    def test_bad_regex_asks(self) -> None:
        self.write_config(json.dumps({"patterns": ["push (unclosed"]}))
        out = self.decision(self.run_hook(json.dumps(bash_event("ls"))))
        self.assertEqual(out["permissionDecision"], "ask")
        self.assertIn("live-write guard misconfigured", out["permissionDecisionReason"])

    def test_malformed_stdin_asks(self) -> None:
        self.write_config(json.dumps({"patterns": [r"--live\b"]}))
        for stdin in ("not json", "[]", json.dumps({"tool_name": "Bash", "tool_input": {}})):
            with self.subTest(stdin=stdin):
                out = self.decision(self.run_hook(stdin))
                self.assertEqual(out["permissionDecision"], "ask")

    def test_malformed_stdin_asks_without_config(self) -> None:
        for stdin in ("", "not json", "[]", json.dumps({"tool_name": "Bash", "tool_input": {}})):
            with self.subTest(stdin=stdin):
                out = self.decision(self.run_hook(stdin))
                self.assertEqual(out["permissionDecision"], "ask")


class KitFilesTest(unittest.TestCase):
    def test_hook_is_executable(self) -> None:
        if os.name == "posix":
            self.assertTrue(os.access(HOOK, os.X_OK), "chmod +x the hook")

    def test_settings_template(self) -> None:
        settings = json.loads((KIT / "settings.json").read_text(encoding="utf-8"))
        deny = settings["permissions"]["deny"]
        for rule in ("Read(.env)", "Read(.env.*)", "Edit(/.claude/settings.json)",
                     "Edit(/.claude/hooks/**)", "Edit(/.claude/live-write-patterns.json)"):
            self.assertIn(rule, deny)
        entry = settings["hooks"]["PreToolUse"][0]
        self.assertEqual(entry["matcher"], "Bash")
        command = entry["hooks"][0]["command"]
        self.assertEqual(entry["hooks"][0]["timeout"], 10)
        self.assertIn("${CLAUDE_PROJECT_DIR}/.claude/hooks/live_write_guard.py", command)

    def test_example_patterns(self) -> None:
        data = json.loads((KIT / "live-write-patterns.example.json").read_text(encoding="utf-8"))
        self.assertEqual(data["patterns"], [])
        self.assertTrue(data["_example_patterns"])
        for pattern in data["_example_patterns"]:
            re.compile(pattern)


if __name__ == "__main__":
    unittest.main()
