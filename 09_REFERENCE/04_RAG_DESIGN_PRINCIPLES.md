# RAG design principles

A strong project RAG system is not "upload everything and hope the AI figures it out."

## 1. Route before retrieving

Use an index that says which document is relevant to which kind of task.

## 2. Retrieve minimally

More context is not always better. Irrelevant context can:
- distract the model;
- introduce conflicts;
- expose unnecessary data;
- increase prompt-injection surface.

## 3. Separate document roles

Keep different kinds of knowledge distinct:
- normative rules;
- requirements;
- architecture;
- environment facts;
- accepted decisions;
- current mutable state;
- historical notes;
- external reference material.

## 4. Version important authority

A document can contain:
- ID;
- version;
- status;
- authority class;
- date.

## 5. Make supersession explicit

Do not leave two contradictory documents both looking current.

## 6. Define precedence

Decide what wins when sources disagree.

## 7. Treat retrieval as a security boundary

Retrieved text does not automatically gain authority.

## 8. Preserve provenance

For consequential decisions, record which source/version supported the action.

## 9. Prefer live evidence for mutable facts

Repository branch, running version, deployment status, package versions, and service health should be checked when they matter.

## 10. Test your retrieval

Ask:
- Does the right document appear?
- Does irrelevant private data stay out?
- Can a malicious document hijack behavior?
- Does old guidance beat a current standard accidentally?
- Can one user's data appear in another user's response?
