# Glossary

| Word | Meaning |
|---|---|
| **Arm** | The click by a person that turns a dry run into a live push, after a go. |
| **Combination** | One action type on one platform, for example "price on platform A". Coverage is tracked per combination. |
| **Coverage sheet** | The record for one combination: every check, marked passed, failed, not applicable or not run (with the reason). |
| **Dry run** | A push that shows its plan and writes nothing. The default. |
| **Go** | The owner's permission for one live push, or for one agreed batch of like pushes on the same store in one sitting. A go expires. |
| **House rules** | The owner's rules for a repository. They override this playbook for local facts. |
| **Live write** | Any change to a delivery platform, POS, shared sheet, database or customer-visible menu. |
| **Re-read** | Reading the platform back after a write and comparing it with the plan. |
| **Restore** | The step that puts a test store back to how it was before a live test. |
| **Risk tier** | R0 to R3; see [`risk-and-approval.md`](risk-and-approval.md). |
| **Silent success** | A run that reports success when the platform did not change as planned. |
| **Test store** | A store the owner has named for live tests. No other store is written during testing. |
