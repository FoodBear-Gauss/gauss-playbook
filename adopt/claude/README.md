# Claude Code Enforcement Kit

A mechanical guard for the live-write rules in
[`../../risk-and-approval.md`](../../risk-and-approval.md#3-the-approval-boundary-for-live-writes),
for repositories where people use Claude Code. It is one way to do adoption
[step 5](../README.md#steps): make one rule mechanical.

The guard never approves anything. It can only make Claude Code stop and ask a
person.

## Files

| File | Copy to | What it does |
|---|---|---|
| [`hooks/live_write_guard.py`](hooks/live_write_guard.py) | `.claude/hooks/live_write_guard.py` | PreToolUse hook on the Bash tool. When a command matches a live-write pattern, it returns `ask` and shows the exact command. Never returns `allow`. |
| [`live-write-patterns.example.json`](live-write-patterns.example.json) | `.claude/live-write-patterns.json` | The patterns. Ships empty, with generic examples to replace. |
| [`settings.json`](settings.json) | `.claude/settings.json` | Denies reading `.env`, `.env.*` and common secret files. Denies editing the settings, the hook and the pattern file through file tools. Registers the hook with a 10 second timeout. |

How the guard decides:

| Situation | Result |
|---|---|
| Not a Bash command | No output. Normal permission flow. |
| Hook input unreadable, or no `tool_input.command` | `ask`, whether or not the pattern file exists |
| Command text mentions `live-write-patterns`, `live_write_guard` or `.claude/settings` | `ask`, always, even with no pattern file. A Bash `rm` or `mv` of the pattern file would otherwise switch the guard off silently. |
| `.claude/live-write-patterns.json` missing | No output. The guard is not configured. |
| Pattern file is not valid JSON, is not a file, `patterns` is not a list, a pattern is empty, or a pattern does not compile | `ask` on every Bash command: `live-write guard misconfigured: <detail>` |
| Command matches a pattern | `ask`, with the command (first 300 characters), the matched text in context when it falls past that, and the go-and-arm rule |
| No match | No output. Normal permission flow. |

No output does not approve a command. Claude Code's own permission rules still
apply.

## Install

1. Get the owner's agreement, as for the rest of adoption.
2. Copy the three files to the paths above and make the hook executable
   (`chmod +x .claude/hooks/live_write_guard.py`). The hook needs `python3`
   (3.9 or later).
3. If the repository already has `.claude/settings.json`, merge the `deny` list
   and the `hooks` block into it instead of replacing it.
4. If the repository commits a `.env.example`, the `Read(.env.*)` rule also
   hides it from Claude. Keep the rule, or narrow it, as the owner decides.
5. The secret-file deny list is a starting set. Extend it during discovery with
   the secret files the repository actually has.

Settings and the hook are protected from Claude's file tools, so a person edits
them in an editor, not through Claude.

## Fill the patterns

Do this after discovery has read the repository's write scripts, not before.

1. List every command that can write to a live platform: each write script,
   its live or arm flag, and any make target or alias that calls it.
2. Write one regex per command in `patterns`. Match the part that makes it live
   (the flag, the script name), so dry runs stay quiet where possible.
   Keep patterns simple: anchored flags and script names, no nested quantifiers
   such as `(a+)+`. A slow pattern can run past the 10 second hook timeout, and
   after a timeout the command goes ahead without a decision.
3. Delete `_example_patterns`, or leave it; the guard ignores it.
4. Keep real script names, store names and endpoints in the adopting
   repository. This playbook is public.

## Test it once

1. Run the unit tests in this playbook: `python3 -m unittest discover -s tests -v`.
2. In the adopting repository, open a **fresh** Claude Code session and ask it to
   run a command that matches a pattern, against a test store or with the
   network off.
3. Pass: Claude Code stops and asks, and the prompt shows the exact command and
   the go-and-arm reason. Decline it.
4. Record the result, with the date and the Claude Code version, in the adopting
   repository's `DEVLOG.md`.

## Limits

- It covers only commands Claude runs through its Bash tool. A person, a cron
  job or a script run outside Claude is not stopped. The in-script staging guard
  (dry run by default, a person arms) covers that.
- Other tools that run commands (PowerShell on Windows, the Monitor tool, MCP
  terminal tools) are not matched. Deny them, or extend the matcher after
  checking their `tool_input` field names.
- Deleting or moving the pattern file through Bash switches the guard off
  without notice once it is gone. The built-in check asks on commands that name
  the guard's files, but a command that reaches them another way (a glob, a
  variable, a script) is not caught. Check the file is present after any session
  that touched `.claude/`.
- Patterns match command text. A renamed script, an alias, `bash -c`, or a
  script that calls the write script internally can slip past. The sandbox is
  the only operating-system boundary.
- File-tool deny rules do not bind every Bash command. A Python or Node process
  started through Bash can read or edit files those rules protect.
- If `python3` is missing or the hook cannot start, it does not block. Run the
  test above after any change to the machine or the settings.
- The guard has never fired in a real repository yet. Treat it as unproven
  until the test above passes in an adopting repository.
