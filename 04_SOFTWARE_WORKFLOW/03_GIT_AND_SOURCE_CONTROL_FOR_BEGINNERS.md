# Git and source control for beginners

You do not need to master Git before using it.

Think of Git as a history system for your project.

## Minimum concepts

- **Repository:** the project and its history.
- **Commit:** a named checkpoint.
- **Branch:** a line of work.
- **Main/default branch:** the trusted primary line.
- **Pull/Merge Request:** a proposed change that can be reviewed before joining the trusted line.
- **Tag:** a durable name often used for releases.

## Safe beginner pattern

1. Keep the default branch protected when your hosting service supports it.
2. Make each feature/fix in its own branch.
3. Keep changes small and focused.
4. Commit only after reviewing what changed.
5. Run tests before merging.
6. Prefer review before merging production code.
7. Do not force-push shared branches unless you understand the consequence and explicitly intend it.
8. Do not commit secrets.

## Ask your AI before Git changes

> Show me the current repository, branch, working-tree state, and recent history. Explain what each means. Do not mutate anything yet.

Then:

> Propose the smallest Git operation needed. Tell me whether it changes only my local machine or also a remote/shared repository.

This makes remote mutations much harder to perform accidentally.
