# Step 3 - Project memory and isolation

Current ChatGPT Projects can use **default memory** or **project-only memory** when available for the account/workspace.

## Use project-only memory when

You want the project strongly isolated from unrelated chats and memories.

This is especially useful when:
- project context must not bleed into unrelated work;
- multiple clients or organizations must stay separate;
- you want the project files/chats to be the main context boundary.

In current ChatGPT:
1. Open the Project.
2. Open **Project settings**.
3. Under **Memory**, choose **Project-only memory** when appropriate.
4. Save.

Project-only memory means project chats can use context from that project, but do not pull conversation context from outside it.

Shared projects are currently project-only automatically.

## Use default memory when

Cross-project/personal continuity is desirable and appropriate for the data.

## Important

Memory is convenience, not your authoritative project database.

Keep important:
- requirements;
- accepted decisions;
- security boundaries;
- verified current state;
- tests;
- release evidence

in project files so they can be inspected, versioned, corrected, and handed off.
