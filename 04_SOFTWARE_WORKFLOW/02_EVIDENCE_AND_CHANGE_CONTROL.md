# Evidence and change control

## Four evidence labels

Use these consistently:

### VERIFIED
Directly observed now from a trustworthy source.

Examples:
- test output from the current commit;
- live API response;
- current repository status.

### DOCUMENTED PRIOR EVIDENCE
Previously verified and recorded, but not necessarily rechecked now.

### USER-PROVIDED
The user states it is true, but the AI has not independently verified it.

### INFERENCE
A reasoned conclusion, not direct proof.

### UNKNOWN
Not established.

## Before a consequential change

Record:
- objective;
- current evidence;
- exact files/components affected;
- exact mutation;
- expected result;
- rollback/recovery;
- verification.

## After the change

Record:
- what actually changed;
- test outputs;
- unexpected differences;
- residual risk;
- PASS/FAIL/INCOMPLETE.

## Why this matters

Without explicit evidence labels, AI-assisted projects easily develop "memory laundering": a guess appears in one response, gets repeated later, and eventually looks like a fact.
