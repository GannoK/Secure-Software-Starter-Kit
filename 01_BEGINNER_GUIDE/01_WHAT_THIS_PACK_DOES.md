# What this pack does

## The problem

AI can make software development much more accessible, but ordinary chat has weaknesses:

- important decisions disappear inside long conversations;
- the AI may rely on old information;
- assumptions can accidentally become treated as facts;
- a later session may repeat or undo completed work;
- generated code can contain security problems;
- an AI can confidently propose commands or changes that were never tested.

This pack gives you a simple project memory and safety system.

## Five concepts

### 1. Project knowledge
Important information lives in files, not only in chat.

### 2. RAG
The AI retrieves the small set of project files relevant to the current question.

### 3. Authority
Some files contain rules. Others contain facts or history. The AI should know the difference.

### 4. Evidence
A claim such as "the tests pass" should come from actual test output, not expectation.

### 5. Gates
Before an important change, you check that the project is ready. After the change, you prove that it worked.

## You do not need to know everything first

You can describe your idea in ordinary language. Ask the AI to help turn it into:
- requirements;
- architecture;
- risks;
- tasks;
- tests;
- documentation.

The important part is that the AI must clearly separate what **you decided** from what **it proposes**.
