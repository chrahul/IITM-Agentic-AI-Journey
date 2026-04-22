## 4.4 System Design Patterns

---

### 1) Context

In 4.3 you learned **how systems execute (patterns of flow)**.

Now we go one level higher:

How do you **design the system itself**?

This section is about **architecture decisions**, not just flow.

These decisions impact:

* scalability
* reliability
* cost
* maintainability

---

### 2) Concept

System design patterns define **how your GenAI system is structured at a higher level**.

---

## Pattern 1: Stateless vs Stateful Systems

---

### Stateless System

#### Definition

Each request is independent. No memory is stored.

#### Flow

Input → LLM → Output

#### Characteristics

* Simple
* Scalable
* No context retention

#### Example

Explain Kubernetes

---

### Stateful System

#### Definition

System maintains memory across interactions.

#### Flow

Input → Memory → LLM → Output

#### Characteristics

* Context-aware
* Better user experience
* More complex

#### Example

User: My app runs on Kubernetes
User: Why is it slow

---

### Key Decision

Stateless → simpler and cheaper
Stateful → richer but complex

---

## Pattern 2: Single-Agent vs Multi-Agent Systems

---

### Single-Agent System

#### Definition

One agent handles all decisions and actions.

#### Characteristics

* Simple
* Easier to control
* Limited scalability for complex tasks

#### Example

Chatbot that answers and calls APIs

---

### Multi-Agent System

#### Definition

Multiple agents collaborate, each with a role.

#### Types of agents

* Planner
* Researcher
* Executor
* Validator

#### Characteristics

* Modular
* Scalable
* Complex coordination

#### Example

A system that:

* fetches logs
* analyzes root cause
* suggests fix
* executes action

---

### Key Insight

Multi-agent is not always better
Use it only when complexity demands it

---

## Pattern 3: Synchronous vs Asynchronous Systems

---

### Synchronous

#### Definition

User waits for response

#### Flow

Request → Process → Response

#### Example

ChatGPT response

---

### Asynchronous

#### Definition

Processing happens in background

#### Flow

Request → Queue → Process → Notify

#### Example

Generate report and send later

---

### Key Insight

Long-running tasks → asynchronous

---

## Pattern 4: Centralized vs Distributed Orchestration

---

### Centralized

#### Definition

Single orchestration layer controls everything

#### Characteristics

* Easy to manage
* Single point of failure

---

### Distributed

#### Definition

Multiple orchestrators or services

#### Characteristics

* Scalable
* Complex coordination

---

## Pattern 5: RAG vs Fine-Tuning

---

### RAG (Retrieval)

#### Approach

Fetch external data dynamically

#### Pros

* Up-to-date
* No retraining

---

### Fine-Tuning

#### Approach

Train model on custom data

#### Pros

* Faster inference
* Better domain adaptation

---

### Key Decision

Dynamic knowledge → RAG
Static domain → Fine-tuning

---

## Pattern 6: Human-in-the-Loop Systems

---

### Definition

Humans validate or intervene in AI decisions

---

### Use cases

* High-risk decisions
* Financial / medical systems
* Deployment approvals

---

### Flow

Input
→ AI suggestion
→ Human validation
→ Final action

---

## Pattern 7: Cost-Aware Architecture

---

### Concept

Design system to optimize cost

---

### Techniques

* Use smaller models when possible
* Use RAG instead of large context
* Cache responses
* Limit token usage

---

## Key Summary Table

| Pattern                    | Decision Factor  |
| -------------------------- | ---------------- |
| Stateless vs Stateful      | Need for context |
| Single vs Multi-agent      | Task complexity  |
| Sync vs Async              | Response time    |
| Centralized vs Distributed | Scale            |
| RAG vs Fine-tune           | Data dynamics    |
| Human-in-loop              | Risk level       |
| Cost-aware                 | Budget           |

---

### 3) Labs

---

#### Lab 1: Stateless vs Stateful

```python
# Stateless
print(llm.invoke("Explain Kubernetes").content)
```

```python
# Stateful
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm, memory=memory)

print(conversation.run("My app runs on Kubernetes"))
print(conversation.run("Why is it slow"))
```

---

#### Lab 2: Async Simulation (concept)

```python
import time

def long_task():
    time.sleep(3)
    return "Report generated"

print("Task submitted")
print(long_task())
```

---

### Final Understanding

System design patterns define:

* how your system behaves at scale
* how it handles complexity
* how it balances cost vs performance

Most important takeaway:

There is no perfect architecture
There is only a **right architecture for a given problem**

---

You’ve now completed:

Section 4 — Architecture

You are no longer just learning tools
You are thinking like a system designer

---

Next section is:

Section 5: Ecosystem and Integrations

This is where we map real tools like:

* LangChain
* LlamaIndex
* Vector DBs
* APIs
* Cloud services

into this architecture.
