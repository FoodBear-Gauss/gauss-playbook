# Coverage Sheet: <Action> on <Platform>

- **Combination:** <one action type on one platform, e.g. "price on platform A">
- **Release / commit:** <identity of what was tested>
- **Test store(s):** <names agreed with the owner>
- **Tester:** <name>  **Second engineer:** <name, confirms live and fault checks>
- **Date:** <YYYY-MM-DD>

One sheet per combination. Every check ends in one of four states. "Not run"
always carries a reason. A blank row is not a pass.

| Check ID | What is checked | Where it runs | Result | Evidence | Notes |
|---|---|---|---|---|---|
| | Dry run shows the exact plan and writes nothing | | passed / failed / not applicable / not run | <link or file> | |
| | Live push on a test store, with a go and an arming record | | | | |
| | Re-read matches the plan | | | | |
| | Injected mismatch is reported as a mismatch | | | | |
| | Network timeout fails with a reason and no partial write | | | | |
| | Expired login fails with a reason | | | | |
| | Restore puts the store back, confirmed by re-read | | | | |

## Summary

- Passed: <n>  Failed: <n>  Not applicable: <n>  Not run: <n>
- **Limits found:** <what this combination cannot do yet>
- **Owner sign-off:** <name, date, or "pending">
