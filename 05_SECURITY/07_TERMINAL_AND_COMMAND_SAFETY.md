# Terminal and command safety for beginners

A terminal command can change files, install software, delete data, expose secrets, or affect remote systems. Do not treat generated commands as harmless text.

## Before running commands

Ask the AI to identify:
- operating system;
- shell/terminal type;
- current folder;
- whether the command is read-only or mutating;
- whether it affects only this machine or also a remote/cloud system;
- whether administrator/root privileges are required;
- how to verify success.

## Prefer diagnosis first

When troubleshooting, start with commands that inspect:
- versions;
- status;
- logs;
- configuration;
- current directory;
- source-control state.

Do not begin with reset/reinstall/delete.

## Privilege

Administrator/root access magnifies mistakes.

- Use elevated privilege only for the exact operation that needs it.
- Avoid persistent administrator/root shells for convenience.
- Never paste a password, token, or private key into a command unless you understand where it will be stored and exposed.

## Download-and-execute commands

Be cautious with patterns that download code from the internet and immediately run it.

Before executing:
- verify the official source;
- inspect what is being downloaded when practical;
- confirm the expected checksum/signature when the publisher provides one.

## Destructive commands

Before deletion or overwrite:
- print/confirm the exact target;
- make sure it is not empty;
- make sure it is inside the intended folder;
- avoid broad wildcards;
- have backup/recovery when the data matters.

Never allow an AI-discovered path to become a destructive target without validating it first.

## Shell safety

If the AI gives a multi-command block:
- ask whether a failure in one command could terminate or alter your interactive shell;
- ask for a bounded/safe script or child process if fail-fast behavior is needed;
- avoid persistent shell options/traps you do not understand.

## Source-control commands

Before Git mutations, inspect:
- repository;
- branch;
- working-tree changes;
- remote target.

Ask explicitly whether a command:
- changes only local state;
- rewrites history;
- pushes to a remote;
- merges;
- deletes a branch/tag.

## Cloud and production commands

Treat these as high impact:
- deployments;
- database migrations;
- deleting cloud resources;
- changing DNS;
- changing IAM/permissions;
- rotating keys;
- modifying firewalls;
- changing billing/scaling.

Require explicit scope, approval, rollback, and post-change verification.
