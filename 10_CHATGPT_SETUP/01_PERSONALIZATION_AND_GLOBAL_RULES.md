# Step 1 - Personalization and global rules

Use global personalization for **durable preferences that should follow you across projects**.

On current ChatGPT web/desktop:
1. Open **Settings**.
2. Open **Personalization**.
3. Ensure customization is enabled.
4. Open **Custom Instructions**.
5. Add your durable working rules.

A safe generic starting point is:

`03_PROMPTS/00_GLOBAL_WORKING_RULES_TEMPLATE.txt`

## What belongs globally

Good global content:
- explain unfamiliar technical concepts clearly;
- distinguish evidence from assumptions;
- inspect before consequential mutation;
- protect secrets;
- verify before claiming success;
- prefer bounded/reversible changes.

Avoid putting these globally:
- today's Git branch;
- current bug;
- temporary server address;
- specific milestone state;
- project-only security exceptions.

Those become stale and belong in the project.

## Important precedence behavior

Inside a ChatGPT Project, **Project instructions apply to that project and take precedence over global custom instructions**.

Therefore keep project-specific authority in Project instructions and project knowledge files rather than trying to force every project rule into the global field.
