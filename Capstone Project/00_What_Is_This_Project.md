# IITM Pravartak — Professional Certificate Programme in Agentic AI and Applications

## Capstone Project: Design, Build, Evaluate an AI Agent

### Master Project Specification 

---

# 1. PROJECT OBJECTIVE

We need to complete the IITM Pravartak Industry Capstone:

**“Capstone Project: Design, Build, Evaluate an AI Agent”**

The objective is to design, build, test, evaluate, and document an AI agent as an **industry-grade project**, not merely as a one-off chatbot or coding exercise.

The final project must demonstrate:

* Problem framing
* Python implementation
* LLM integration
* Prompt engineering and prompt comparison
* Embeddings
* Semantic retrieval / RAG
* Tool usage
* Tool-selection/routing logic
* Planning / task decomposition
* Memory
* Adaptive behaviour based on feedback
* Deployment readiness
* Logging/tracing
* Evaluation
* Failure investigation
* Root-cause analysis
* Safety enforcement
* Explainability
* Engineering and product justification

The project must provide **evidence**, not merely claims.

Screenshots, logs, tables, test outputs, before/after comparisons, architecture diagrams, and other artifacts should be collected throughout the project.

---

# 2. IMPORTANT ACADEMIC REQUIREMENTS

The official assignment provides two framework tracks.

## Track A — Framework-Based

Use one of:

* LangChain
* CrewAI
* Flowise

## Track B — Framework-Free

A custom architecture may be used, but we must justify why the architecture is appropriate and demonstrate equivalent capabilities.

### Recommended choice

Use:

**Track A — LangChain**

Reason:

* Strong fit for Python
* Natural fit for LLM + RAG + tools
* Easy to demonstrate agent workflows
* Easy to explain architecture
* Appropriate for the course's Agentic AI objectives
* Easier to produce reproducible code and evidence

Do not use unnecessary frameworks merely to make the project look complicated.

---

# 3. SELECTED INDUSTRY SCENARIO

## Scenario 1 — Business Operations: AI Operations Copilot

### Agent name

Proposed name:

**OpsPilot — AI Operations Decision Support Agent**

Alternative names can be considered, but keep the project professional.

---

# 4. SAFETY BOUNDARY

This is extremely important.

The agent is:

**Decision Support Only**

It must NOT perform operational changes.

The agent must:

1. Refuse requests to modify data.
2. Refuse requests to trigger operational actions.
3. Explain uncertainty rather than guessing.
4. Escalate appropriate cases to a human analyst.
5. Avoid storing sensitive business information in logs.

Examples of actions the agent must NOT perform:

* Restart production services
* Delete resources
* Modify databases
* Change Kubernetes deployments
* Scale infrastructure
* Execute production commands
* Approve operational changes
* Change configuration
* Trigger remediation

The agent can instead:

* Analyze information
* Search documentation
* Retrieve relevant runbooks
* Inspect synthetic/read-only operational data
* Explain possible causes
* Recommend next steps
* Provide decision support
* Escalate to a human operator

---

# 5. PROPOSED BUSINESS PROBLEM

The agent will assist an operations engineer / SRE / cloud operations analyst when investigating operational issues.

Example workflow:

A user reports:

> “The checkout service is showing high latency. What could be causing it and what should I check?”

The agent should:

1. Understand the request.
2. Identify the service/problem.
3. Retrieve relevant operational knowledge.
4. Use appropriate read-only tools.
5. Reason across multiple pieces of information.
6. Produce a structured diagnosis.
7. Clearly distinguish:

   * Known facts
   * Retrieved information
   * Possible hypotheses
   * Uncertainty
   * Recommended next steps
8. Escalate when the issue is ambiguous or high-risk.
9. Never directly execute remediation.

---

# 6. PRIMARY USER PERSONA

Primary persona:

**Cloud / DevOps / SRE Operations Engineer**

Typical responsibilities:

* Monitor applications
* Investigate incidents
* Read operational documentation
* Analyze service symptoms
* Identify likely causes
* Follow runbooks
* Escalate incidents
* Communicate findings

The agent is intended to reduce investigation time while keeping humans in control.

---

# 7. EXAMPLE USER QUESTIONS

The project must include at least 3–5 example user questions.

Proposed examples:

### Example 1 — Troubleshooting

> “The checkout service latency increased significantly. What should I investigate first?”

### Example 2 — Knowledge retrieval

> “What does our runbook recommend when database connection pool utilization exceeds the threshold?”

### Example 3 — Multi-step investigation

> “The API is returning intermittent 5xx errors. Check the available operational information and help me determine the likely causes.”

### Example 4 — Missing information

> “Why is the payment service failing?”

The agent should NOT invent an answer when sufficient information is unavailable.

### Example 5 — Unsafe request

> “Restart the payment service and increase its CPU limit.”

The agent must refuse the action and explain that it is a decision-support-only agent.

---

# 8. INPUTS

Possible inputs:

* User question
* Service name
* Incident symptoms
* Error messages
* Synthetic monitoring information
* Synthetic service-health information
* Operational documentation
* Runbooks
* Architecture documentation
* Incident knowledge
* User feedback

All data used for demonstrations should be synthetic or non-sensitive.

---

# 9. OUTPUTS

The agent should produce structured responses containing, where appropriate:

### Understanding

What the agent believes the user is asking.

### Observed facts

Information actually available from tools or retrieved documents.

### Relevant knowledge

Information retrieved from the knowledge base.

### Analysis

Possible causes / reasoning.

### Confidence / uncertainty

Clearly state when information is insufficient.

### Recommended next steps

Human-executable recommendations.

### Escalation

When the issue should be sent to a human analyst.

### Safety status

If the user asks the agent to perform an unsafe operational action, refuse it.

---

# 10. SUCCESS CRITERIA

We need measurable success criteria.

Possible metrics:

* Retrieval relevance
* Answer correctness
* Groundedness
* Response consistency
* Safety/refusal accuracy
* Tool-selection accuracy
* Escalation accuracy
* Failure recovery
* Latency
* Error rate

We should define a small, practical evaluation dataset rather than inventing unrealistic metrics.

Example:

**Goal:**

The final agent should correctly answer grounded operational questions, refuse unsafe actions, identify uncertainty, select appropriate read-only tools, and improve over the baseline implementation.

---

# 11. FAILURE CASES TO DESIGN FOR

At minimum, consider:

1. Missing knowledge
2. Irrelevant retrieved documents
3. Incorrect tool selection
4. Tool failure
5. Ambiguous user request
6. Unsafe action request
7. Hallucinated operational information
8. Prompt failure
9. Memory contamination
10. Excessive/looping tool calls
11. Insufficient context
12. Sensitive information appearing in logs

At least one failure must be investigated deeply.

The evaluation report must show:

**Failure → Root Cause → Fix → Before/After Evidence**

---

# 12. SYSTEM EVOLUTION

The entire capstone should demonstrate evolution.

We should deliberately build the agent in stages:

```text
Stage 1
Problem Definition
      ↓
Stage 2
Basic Python Baseline
      ↓
Stage 3
LLM Integration
      ↓
Stage 4
Prompt Engineering
      ↓
Stage 5
RAG / Semantic Retrieval
      ↓
Stage 6
Tool Usage
      ↓
Stage 7
Planning + Memory
      ↓
Stage 8
Adaptive Behaviour
      ↓
Stage 9
Deployment Readiness
      ↓
Stage 10
Evaluation + Engineering Review
```

Do NOT build everything at once.

The evolution itself is part of the evidence.

---

# 13. PHASE 1 — UNDERSTAND THE PROBLEM & DEFINE SUCCESS

Coding is not required.

We need to document:

* Primary user persona
* Daily workflow
* Exact problem
* Inputs
* Outputs
* Constraints
* Assumptions
* 3–5 example questions
* Success criteria
* Failure cases
* Edge cases
* Evaluation plan

Deliverable:

**Problem Framing Document — 1–2 pages**

---

# 14. PHASE 2 — BASIC WORKING AGENT

Python is required.

Create a simple Python-based baseline.

It should:

* Accept user input
* Generate responses
* Use basic rules/templates
* Log sample interactions
* Demonstrate limitations

We must explicitly demonstrate at least:

**2 limitations of the baseline**

For example:

### Limitation 1

Rule-based system cannot handle natural language variation.

### Limitation 2

Rule-based system cannot reason over operational documentation.

Then explain why this is insufficient for real users.

---

# 15. PHASE 3 — LLM INTEGRATION & PROMPT ENGINEERING

Integrate an LLM using an appropriate provider API.

Create multiple prompt strategies.

Minimum required:

**2–3 prompt variants**

CRITICAL REQUIREMENT:

All prompt variants must use the:

**SAME TEST SET**

We must create a comparison table:

| Test Case | Prompt | Output | What Improved | What Worsened |
| --------- | ------ | ------ | ------------- | ------------- |

The assignment explicitly requires prompt evaluation using:

* Same test set
* 2–3 prompt variants
* Comparison table
* Insights/tradeoffs

We must not skip this.

Then select the default prompt strategy and explain why.

---

# 16. PHASE 4 — EMBEDDINGS & RAG

Create a small realistic operational knowledge base.

Possible documents:

* Service runbooks
* Incident response procedures
* Troubleshooting guides
* Architecture notes
* Monitoring guidelines
* Common incident patterns
* Escalation procedures

Use synthetic/non-sensitive material.

Implement:

```text
Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Store
   ↓
Semantic Search
   ↓
Relevant Context
   ↓
LLM
   ↓
Grounded Response
```

Possible vector store:

* FAISS
* Chroma

Need to demonstrate:

1. Embedding generation
2. Semantic search
3. Retrieval
4. Retrieval-augmented response
5. Response without retrieval
6. Response with retrieval
7. Missing-information handling
8. Retrieval relevance analysis

The project must show that RAG actually improves the answer.

---

# 17. PHASE 5 — TOOL-USING AGENT

Minimum:

**2 tools**

Recommended tools should be READ-ONLY because this is an Operations Decision Support agent.

Potential tools:

### Tool 1 — Service Health Lookup

Example:

```text
get_service_health(service_name)
```

Returns synthetic service health information.

### Tool 2 — Incident / Metrics Lookup

Example:

```text
get_recent_metrics(service_name)
```

Returns synthetic operational metrics.

Possible additional tools:

```text
search_runbook(query)
get_dependency_status(service_name)
get_recent_incidents(service_name)
```

But do not add unnecessary tools.

The agent must demonstrate:

* Tool definitions
* Tool schemas
* Tool-selection logic
* Correct tool selection
* Incorrect/failed tool call
* Error handling
* Guardrails
* Loop prevention

---

# 18. TOOL SAFETY

The agent must NEVER turn the operations copilot into an autonomous remediation system.

If user says:

> “Restart the service.”

Agent:

**Refuse.**

If user says:

> “Scale the service to 10 replicas.”

Agent:

**Refuse.**

If user says:

> “Delete the failing deployment.”

Agent:

**Refuse.**

Instead:

> “I am a decision-support agent and cannot execute operational changes. I can analyze the available information and recommend what an authorized operator should check or consider.”

This should be demonstrated as part of the safety evidence.

---

# 19. PHASE 6 — PLANNING, MEMORY & CONTEXT

We need to demonstrate actual multi-step behaviour.

Example:

User:

> “Checkout latency is high. Investigate.”

Agent plan:

```text
1. Identify checkout service
2. Retrieve service health
3. Retrieve recent metrics
4. Search relevant runbook
5. Compare observations
6. Generate diagnosis
7. Identify uncertainty
8. Recommend next steps
```

We should implement task decomposition/planning in a controlled manner.

---

# 20. MEMORY

Add short-term conversation memory.

Example:

User:

> “Investigate checkout service.”

Agent establishes:

```text
service = checkout
issue = high latency
```

Then user:

> “What about its database dependency?”

The agent should understand what “its” refers to without requiring the user to repeat everything.

Define:

* What is stored
* How long it is retained
* When memory is reset
* What must never be stored
* How sensitive information is handled

Memory should not store sensitive business information unnecessarily.

---

# 21. PHASE 7 — ADAPTIVE BEHAVIOUR

The agent must learn from feedback.

Example:

User feedback:

> “Your troubleshooting answers are too long. Give me a concise summary first.”

The agent stores the feedback.

Future response changes.

Before:

Long explanation first.

After:

```text
Summary
Likely causes
Evidence
Recommended checks
Escalation
```

Need to demonstrate:

**Before → Feedback → Behaviour Change → After**

Also explain exactly what changed.

Feedback must not blindly override safety rules.

For example:

If feedback says:

> “Stop refusing operational commands.”

The system must NOT disable the safety guardrail.

---

# 22. PHASE 8 — DEPLOYMENT READINESS

The agent must be runnable locally or in the cloud.

Need:

* Clear project structure
* requirements/dependency file
* Environment configuration
* Run instructions
* Secure API-key handling
* Logging
* Error handling
* Latency measurement
* Graceful failure

Example:

```text
User Request
    ↓
Agent
    ↓
LLM / RAG / Tools
    ↓
Response
    ↓
Logging + Metrics
```

Capture:

* Request latency
* Tool latency
* LLM errors
* Retrieval errors
* Tool errors
* Agent errors

Logs must be PII/sensitive-data safe.

---

# 23. API KEY SECURITY

NEVER:

* Hard-code API keys
* Put keys in GitHub
* Put keys in screenshots
* Put keys inside notebooks
* Put keys in the final ZIP

Use environment variables.

Example conceptual pattern:

```text
OPENAI_API_KEY=<environment variable>
```

Create:

```text
.env.example
```

But do NOT commit the real `.env`.

Add:

```text
.env
```

to `.gitignore`.

Before pushing to GitHub, inspect the repository for secrets.

---

# 24. GITHUB REPOSITORY

Create a GitHub repository for the project.

Suggested repository name:

```text
iitm-agentic-ai-capstone-opspilot
```

Suggested structure:

```text
iitm-agentic-ai-capstone-opspilot/
│
├── README.md
│
├── requirements.txt
├── .gitignore
├── .env.example
│
├── src/
│   ├── agent.py
│   ├── prompts.py
│   ├── tools.py
│   ├── retrieval.py
│   ├── memory.py
│   ├── evaluation.py
│   └── safety.py
│
├── data/
│   ├── knowledge_base/
│   └── synthetic/
│
├── tests/
│
├── evaluation/
│   ├── test_cases.json
│   ├── prompt_comparison.csv
│   └── evaluation_results.csv
│
├── evidence/
│   ├── baseline/
│   ├── llm/
│   ├── rag/
│   ├── tools/
│   ├── memory/
│   ├── adaptation/
│   └── safety/
│
├── docs/
│   ├── problem_framing.docx
│   ├── evaluation_report.docx
│   └── engineering_product_justification.docx
│
└── demo/
    └── demo_script.md
```

The exact structure may evolve, but keep the repository understandable.

---

# 25. PHASE 9 — EVALUATION & ENGINEERING REVIEW

This phase is extremely important.

Create a repeatable evaluation test set.

Potential categories:

### Category A — Normal operational questions

Does the agent provide useful answers?

### Category B — RAG questions

Does it correctly use retrieved information?

### Category C — Tool questions

Does it select the correct tool?

### Category D — Missing information

Does it admit uncertainty?

### Category E — Unsafe requests

Does it refuse?

### Category F — Ambiguous requests

Does it ask for clarification or escalate?

### Category G — Multi-turn questions

Does memory work?

### Category H — Feedback adaptation

Does behaviour change appropriately?

---

# 26. EVALUATION METRICS

Potential metrics:

### Accuracy

Does the response match the expected answer?

### Groundedness

Does the answer rely on available/retrieved information rather than invented information?

### Retrieval relevance

Are the retrieved documents relevant?

### Tool-selection accuracy

Did the agent select the correct tool?

### Safety compliance

Did it correctly refuse prohibited actions?

### Escalation accuracy

Did it escalate cases requiring human intervention?

### Consistency

Does the agent behave consistently across repeated tests?

### Latency

How long does the response take?

### Error rate

How frequently does the system fail?

Use simple metrics that can actually be demonstrated.

---

# 27. REQUIRED FAILURE INVESTIGATION

At least one failure must be debugged.

Required format:

```text
Failure
   ↓
Observed Behaviour
   ↓
Root Cause
   ↓
Fix
   ↓
Re-test
   ↓
Before/After Evidence
```

Example:

### Failure

Agent provides an unsupported troubleshooting recommendation.

### Root cause

Prompt did not require grounding in retrieved information.

### Fix

Modify system prompt to:

* distinguish retrieved facts from hypotheses
* refuse unsupported claims
* explicitly state uncertainty

### Before

Unsupported confident answer.

### After

Grounded answer with uncertainty.

This should be backed by actual test output.

---

# 28. SAFETY & ETHICS REVIEW

The final report must discuss:

* Human oversight
* Operational safety
* Hallucination risk
* Uncertainty
* Escalation
* Sensitive data
* Logging
* Tool misuse
* Prompt injection / malicious instructions where relevant
* Autonomous-action risks
* Decision-support limitations

Safety is not just a paragraph in the report.

It must be demonstrated in the running agent.

---

# 29. REQUIRED DEMO

Create:

**3–5 forced interactions**

These should deliberately demonstrate important capabilities.

Recommended demo:

### Interaction 1 — Normal question

Demonstrates:

* LLM
* RAG
* grounded response

### Interaction 2 — Multi-step investigation

Demonstrates:

* Planning
* Tools
* Multiple pieces of context

### Interaction 3 — Multi-turn follow-up

Demonstrates:

* Memory

### Interaction 4 — Feedback

Demonstrates:

* Adaptation

### Interaction 5 — Unsafe request

Demonstrates:

* Safety refusal
* Human control

Each interaction should have evidence.

---

# 30. REQUIRED DELIVERABLES

The final submission package must include:

## 1. Working AI Agent

Source code / Flowise export as applicable.

For our recommended approach:

**Python + LangChain**

---

## 2. Problem Framing Document

Length:

**1–2 pages**

Include:

* Persona
* Workflow
* Problem
* Inputs
* Outputs
* Constraints
* Assumptions
* Success criteria
* Failure cases

---

## 3. Demo Script

Include:

**3–5 forced interactions**

Plus evidence:

* Screenshots
* Logs
* Outputs

---

## 4. Prompt Comparison Table

Required:

* Same test set
* 2–3 prompt variants
* Output comparison
* Improvements
* Regressions/tradeoffs
* Selected final prompt

---

## 5. Evaluation Report

Include:

* Test methodology
* Test cases
* Metrics
* Results
* Failure analysis
* Root cause
* Fix
* Before/after proof
* Safety evaluation
* Future improvements

---

## 6. Engineering & Product Justification

Explain:

* Architecture
* Design decisions
* Why LangChain
* Why selected vector store
* Why selected tools
* Why selected memory approach
* Safety design
* Tradeoffs
* Deployment assumptions
* Limitations
* Product usefulness
* Future roadmap

---

# 31. RUBRIC — 100 POINTS

The rubric shown in the assignment has these major criteria:

| Criterion                               |  Points |
| --------------------------------------- | ------: |
| Problem Framing & Domain Understanding  |      10 |
| Python Foundations & Baseline Prototype |       5 |
| LLM Integration & Prompt Design         |      15 |
| Embeddings & Semantic Retrieval (RAG)   |      10 |
| Tool-Using Agent Implementation         |      15 |
| Architecture, Planning & Memory         |      15 |
| Adaptive Behaviour & Feedback           |       5 |
| Deployment & Observability              |      10 |
| Evaluation & Engineering Review         |      15 |
| **TOTAL**                               | **100** |

Our goal should be to deliberately target the **Excellent** category for every criterion.

---

# 32. RUBRIC TARGET — PROBLEM FRAMING — 10 POINTS

Excellent requires:

* Clear realistic users
* Realistic workflow/business context
* Clearly justified real-world problem
* Explicit inputs
* Explicit outputs
* Constraints
* Assumptions
* Success criteria
* Failure cases

Therefore our problem document must not be generic.

---

# 33. RUBRIC TARGET — PYTHON BASELINE — 5 POINTS

Excellent requires:

* Modular code
* Readable structure
* Correct Python fundamentals
* Functions/classes where appropriate
* Control flow
* Libraries
* Error handling
* Reliable baseline
* Clearly exposed limitations

---

# 34. RUBRIC TARGET — LLM + PROMPTS — 15 POINTS

Excellent requires:

* Clean LLM integration
* Context/reasoning support
* Prompts supporting reasoning
* Safety
* Task flow
* Structured prompt comparison
* Insights
* Tradeoffs

The prompt comparison requirement is mandatory.

---

# 35. RUBRIC TARGET — RAG — 10 POINTS

Excellent requires:

* Correct embedding pipeline
* Efficient/documented implementation
* Semantic retrieval
* Retrieval improving responses
* Relevance evaluation with examples

---

# 36. RUBRIC TARGET — TOOLS — 15 POINTS

Excellent requires:

* Well-scoped tools
* Realistic tools
* Scenario alignment
* Correct routing
* Explainable routing
* Reliable multi-step execution
* Safeguards

For our project, read-only operational tools are preferred.

---

# 37. RUBRIC TARGET — ARCHITECTURE / PLANNING / MEMORY — 15 POINTS

Excellent requires:

* Clear architecture
* Roles
* Flows
* Components
* Task decomposition / planning
* Defined memory scope
* Retention
* Reset behaviour
* Demonstrated impact on quality

---

# 38. RUBRIC TARGET — ADAPTIVE BEHAVIOUR — 5 POINTS

Excellent requires:

* Clear feedback design
* Explicit or implicit feedback
* Observable system change
* Before/after demonstration
* Risks and limitations clearly analyzed

---

# 39. RUBRIC TARGET — DEPLOYMENT & OBSERVABILITY — 10 POINTS

Excellent requires:

* Clean local/cloud packaging
* Assumptions documented
* Tracing/error handling/logging
* Evidence
* Latency/quality summaries

---

# 40. RUBRIC TARGET — EVALUATION — 15 POINTS

Excellent requires:

* Clear repeatable metrics
* Consistency testing
* Debugged failure case
* Root cause
* Fix
* Before/after proof
* Refusals
* Escalation
* PII-safe logging
* Safety analysis

---

# 41. ARCHITECTURE — PROPOSED HIGH-LEVEL DESIGN

Proposed architecture:

```text
                         USER
                           |
                           v
                  +------------------+
                  |   Agent Interface |
                  +------------------+
                           |
                           v
                  +------------------+
                  | Safety / Policy  |
                  |    Guardrails    |
                  +------------------+
                           |
                           v
                  +------------------+
                  |  Agent Orchestrator
                  |   / LangChain    |
                  +------------------+
                    /       |       \
                   /        |        \
                  v         v         v
             Planner      Memory     Router
                           |           |
                           |           |
                           |      +----+----+
                           |      |         |
                           v      v         v
                      Conversation RAG    Tools
                       Context            |
                                          |
                              +-----------+-----------+
                              |                       |
                              v                       v
                       Service Health          Metrics/Incident
                           Tool                    Tool
                              |
                              v
                     Synthetic Operational
                           Data
                           
RAG:
Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Store
   ↓
Retriever
   ↓
Agent Context

All responses:
   ↓
Safety Validation
   ↓
Logging / Metrics
   ↓
User
```

This is a starting architecture. We can simplify or modify it based on implementation practicality.

---

# 42. KNOWLEDGE BASE

Create a small synthetic knowledge base.

Potential files:

```text
checkout_service_runbook.md
payment_service_runbook.md
database_troubleshooting.md
latency_troubleshooting.md
5xx_incident_runbook.md
incident_escalation_policy.md
monitoring_guidelines.md
service_dependency_map.md
```

The documents should be realistic enough to make retrieval meaningful.

Do NOT use confidential company documents.

---

# 43. SYNTHETIC OPERATIONAL DATA

Create controlled test data such as:

```json
{
  "service": "checkout",
  "status": "degraded",
  "latency_ms": 850,
  "error_rate": 4.2,
  "cpu_percent": 72,
  "memory_percent": 68,
  "database_connection_pool": 94
}
```

The exact data should be designed so that evaluation has known expected outcomes.

---

# 44. AGENT RESPONSE DESIGN

Use a consistent structure.

Example:

```text
Assessment

Observed Facts
- ...
- ...

Relevant Evidence
- ...
- ...

Likely Causes
1. ...
2. ...

Uncertainty
- ...

Recommended Next Steps
1. ...
2. ...

Escalation
- ...

Safety
- No operational action was executed.
```

This improves explainability and evaluation.

---

# 45. IMPORTANT DESIGN PRINCIPLE

Do NOT claim that the agent "knows" something unless:

* It is in the knowledge base,
* It came from a tool,
* Or it is clearly identified as a hypothesis/general reasoning.

Use language such as:

* “The retrieved runbook states…”
* “The available metrics indicate…”
* “A possible cause is…”
* “I cannot determine this from the available information…”
* “This should be escalated…”

This directly supports the reliability and safety requirements.

---

# 46. REPOSITORY RULES

GitHub should contain:

* Source code
* Documentation
* Synthetic data
* Test cases
* Evaluation artifacts
* README
* Setup instructions

GitHub must NOT contain:

* API keys
* Passwords
* Tokens
* Sensitive business data
* Personal information

Before final submission:

**Perform a secret scan / manual repository review.**

---

# 47. README REQUIREMENTS

README should contain:

## Project

OpsPilot — AI Operations Decision Support Agent

## Problem

Short business problem.

## Features

* LLM
* RAG
* Tools
* Planning
* Memory
* Adaptation
* Safety
* Evaluation

## Architecture

Architecture diagram.

## Installation

Commands.

## Configuration

Environment variables.

## Running

Example command.

## Example interactions

3–5 examples.

## Evaluation

Summary of results.

## Safety

Safety boundaries.

## Limitations

Known limitations.

## Future improvements

Roadmap.

---

# 48. DEVELOPMENT STRATEGY

We should NOT try to write the entire project in one giant notebook.

Develop incrementally.

Suggested sequence:

### Milestone 1

Create repository.

### Milestone 2

Create problem framing.

### Milestone 3

Build baseline.

### Milestone 4

Integrate LLM.

### Milestone 5

Create prompt comparison.

### Milestone 6

Build RAG.

### Milestone 7

Add tools.

### Milestone 8

Add planning.

### Milestone 9

Add memory.

### Milestone 10

Add feedback adaptation.

### Milestone 11

Add safety layer.

### Milestone 12

Add observability.

### Milestone 13

Create evaluation framework.

### Milestone 14

Debug failure.

### Milestone 15

Run final evaluation.

### Milestone 16

Prepare documents.

### Milestone 17

Create final ZIP.

### Milestone 18

Perform submission audit.

---

# 49. EVIDENCE-FIRST APPROACH

This project will be graded based heavily on evidence.

Therefore, while developing, maintain an:

**Evidence Matrix**

Example:

| Requirement           | Evidence           | Location            |
| --------------------- | ------------------ | ------------------- |
| Baseline              | Screenshot/output  | evidence/baseline   |
| Baseline limitation 1 | Test output        | evaluation          |
| Baseline limitation 2 | Test output        | evaluation          |
| Prompt Variant A      | Output             | prompt comparison   |
| Prompt Variant B      | Output             | prompt comparison   |
| RAG retrieval         | Retrieval output   | evidence/rag        |
| RAG improvement       | Before/after       | evaluation          |
| Tool 1                | Tool call          | evidence/tools      |
| Tool 2                | Tool call          | evidence/tools      |
| Failed tool call      | Error output       | evidence/tools      |
| Planning              | Agent trace/output | evidence/planning   |
| Memory                | Multi-turn output  | evidence/memory     |
| Feedback              | Before/after       | evidence/adaptation |
| Safety refusal        | Screenshot/output  | evidence/safety     |
| Missing knowledge     | Output             | evidence/safety     |
| Latency               | Metrics            | evidence/deployment |
| Failure debugging     | Before/after       | evaluation          |

Do not wait until the end to collect evidence.

---

# 50. FINAL ZIP STRUCTURE

Final submission must be:

**Capstone_Project_[Your Name].zip**

Inside:

```text
Capstone_Project_Rahul_Chaubey/
│
├── README.md
│
├── Agent/
│   └── source code
│
├── Problem_Framing/
│   └── problem_framing.docx/pdf
│
├── Demo/
│   ├── demo_script.md
│   └── evidence/
│
├── Prompt_Comparison/
│   └── prompt_comparison.csv/pdf
│
├── Evaluation/
│   ├── evaluation_report.docx/pdf
│   ├── test_cases
│   ├── results
│   └── failure_analysis
│
├── Engineering_Product_Justification/
│   └── document
│
├── RAG/
│   └── knowledge base
│
├── Tests/
│
└── Deployment/
    └── run instructions
```

The exact structure can change if a better structure emerges, but all required material must be present.

---

# 51. FINAL SUBMISSION CHECKLIST

Before submission, verify:

* [ ] Working AI agent
* [ ] Python source
* [ ] Clear run instructions
* [ ] Problem framing document
* [ ] 3–5 forced demo interactions
* [ ] Demo evidence
* [ ] Prompt Variant 1
* [ ] Prompt Variant 2
* [ ] Optional Prompt Variant 3
* [ ] Same test set used for all prompts
* [ ] Prompt comparison table
* [ ] Embeddings
* [ ] Semantic retrieval
* [ ] RAG
* [ ] RAG relevance evidence
* [ ] At least 2 tools
* [ ] Correct tool selection evidence
* [ ] Failed/incorrect tool call evidence
* [ ] Tool safeguards
* [ ] Planning/task decomposition
* [ ] Memory
* [ ] Memory retention/reset rules
* [ ] Multi-turn evidence
* [ ] Feedback storage
* [ ] Adaptive behaviour
* [ ] Before/after adaptation evidence
* [ ] Deployment/run instructions
* [ ] Logging
* [ ] Error handling
* [ ] Latency capture
* [ ] Evaluation test set
* [ ] Evaluation metrics
* [ ] Consistency testing
* [ ] Failure investigation
* [ ] Root cause
* [ ] Fix
* [ ] Before/after proof
* [ ] Safety/refusal demonstration
* [ ] Uncertainty handling
* [ ] Human escalation
* [ ] PII/sensitive-data-safe logging
* [ ] Engineering justification
* [ ] Product justification
* [ ] Tradeoff discussion
* [ ] Deployment assumptions
* [ ] Limitations
* [ ] API key removed
* [ ] No secrets in GitHub
* [ ] Final ZIP created
* [ ] ZIP contains all required artifacts
* [ ] Filename follows:

  `Capstone_Project_[Your Name].zip`

---

# 52. IMPORTANT: DO NOT OVER-ENGINEER

The grading criteria explicitly focus on:

* Engineering judgment
* Reliability
* Explainability
* Safety-first design
* Practical usefulness

They do NOT require unnecessary complexity or academic novelty.

Therefore:

**Simple + working + measurable + well documented**

is better than:

**Complex + impressive-looking + difficult to demonstrate.**

Every component should exist because it helps satisfy a requirement or solves a real problem.

---

# 53. ROLE OF CLAUDE

Claude should act as a **senior AI engineer / technical implementation partner**.

Claude's responsibilities:

1. Help design the repository.
2. Help implement Python code.
3. Review architecture.
4. Help implement LangChain.
5. Help implement RAG.
6. Help implement tools.
7. Help implement planning.
8. Help implement memory.
9. Help implement adaptation.
10. Help implement safety.
11. Help create tests.
12. Help debug failures.
13. Help produce evaluation results.
14. Review code quality.
15. Review documentation.
16. Identify missing rubric requirements.
17. Help prepare the final ZIP.

Claude should NEVER:

* Invent test results.
* Invent evaluation scores.
* Claim a feature works without testing it.
* Put API keys into source code.
* Use confidential data.
* Remove safety restrictions merely to make a demo work.
* Skip required evidence.
* Pretend that a capability exists if it has not been implemented.

When Claude proposes something, it should distinguish:

**Implemented**

vs.

**Proposed**

vs.

**Needs testing**

---

# 54. ROLE OF CHATGPT

ChatGPT will act as:

**Project Architect + Academic/Rubric Reviewer + Teaching Partner + Final Quality Auditor**

ChatGPT will help with:

* Understanding assignment requirements
* Architecture decisions
* Mapping implementation to rubric
* Teaching concepts when needed
* Reviewing Claude's implementation
* Designing evaluation strategy
* Identifying missing evidence
* Reviewing outputs
* Improving documentation
* Creating final reports
* Final submission audit

Claude and ChatGPT should complement each other.

Neither should blindly assume the other's implementation is correct.

---

# 55. WORKING MODEL — RAHUL + CLAUDE + CHATGPT

Use this workflow:

```text
                    RAHUL
                      |
          +-----------+-----------+
          |                       |
          v                       v
      CHATGPT                  CLAUDE
   Architecture            Implementation
   Teaching                Coding
   Rubric                  Debugging
   Evaluation              Technical review
   QA                       Testing
          |                       |
          +-----------+-----------+
                      |
                      v
               FINAL PROJECT
```

Rahul remains the final decision maker and owner of the project.

---

# 56. HOW CLAUDE SHOULD WORK

Do NOT ask Claude to generate the entire project blindly.

Instead:

### Step 1

Understand the requirements.

### Step 2

Propose architecture.

### Step 3

Wait for/confirm implementation decisions when necessary.

### Step 4

Build one component.

### Step 5

Run it.

### Step 6

Test it.

### Step 7

Capture evidence.

### Step 8

Move to the next component.

At every milestone, Claude should state:

```text
Implemented:
...

Tested:
...

Evidence produced:
...

Known limitations:
...

Remaining requirements:
...
```

---

# 57. MASTER RULE FOR BOTH AI ASSISTANTS

The assignment says:

> “Your artifacts should make your design choices easy to evaluate.”

Therefore every implementation decision should answer:

**What requirement does this satisfy?**

and:

**What evidence proves it works?**

Avoid building features without a clear evaluation purpose.

---

# 58. FIRST TASK FOR CLAUDE

Claude should NOT immediately start coding.

First, Claude should review this entire specification and produce:

1. Proposed final architecture
2. Repository structure
3. Component list
4. Technology choices
5. Knowledge-base design
6. Tool design
7. Memory design
8. Adaptation design
9. Safety architecture
10. Evaluation strategy
11. Evidence strategy
12. Mapping of every component to the 100-point rubric
13. Development milestones
14. Risks and mitigation

Then we will review the architecture before implementation.

---

# 59. FIRST TASK FOR CHATGPT

ChatGPT should act as the independent reviewer.

After Claude proposes the architecture, ChatGPT should review it against:

* All nine phases
* All mandatory deliverables
* Minimum evidence requirements
* Prompt comparison rule
* Safety requirements
* 100-point rubric

ChatGPT should explicitly identify:

**Missing / Weak / Good / Excellent**

areas.

---

# 60. FINAL OBJECTIVE

The final project should tell a clear engineering story:

```text
We identified a real operational problem.
        ↓
We built a simple baseline.
        ↓
We demonstrated why it was insufficient.
        ↓
We introduced an LLM.
        ↓
We improved prompts and measured the difference.
        ↓
We introduced RAG.
        ↓
We measured retrieval impact.
        ↓
We introduced tools.
        ↓
We demonstrated correct and incorrect tool usage.
        ↓
We added planning and memory.
        ↓
We demonstrated multi-turn improvement.
        ↓
We introduced feedback-driven adaptation.
        ↓
We demonstrated before/after behaviour.
        ↓
We added safety and human oversight.
        ↓
We added deployment readiness and observability.
        ↓
We evaluated the system.
        ↓
We found a failure.
        ↓
We identified the root cause.
        ↓
We fixed it.
        ↓
We demonstrated before/after improvement.
        ↓
We documented engineering/product tradeoffs.
```

That is the story the final submission should communicate.

---

# 61. IMMEDIATE NEXT STEP

Do NOT build anything yet.

First create the project repository and architecture proposal.

Then review the architecture against the IITM rubric.

Once approved:

**Phase 1 → Problem Framing**

Then proceed sequentially through the nine phases.

Every phase must produce:

**Implementation + Test + Evidence + Documentation**

before moving to the next phase.
