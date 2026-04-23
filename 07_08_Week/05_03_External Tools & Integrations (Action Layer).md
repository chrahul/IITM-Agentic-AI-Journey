# SECTION 5.3: External Tools & Integrations (Action Layer)

---

## 1) What Problem We Are Solving

Till now:

* LLM can explain
* LLM can summarize
* LLM can reason

But it **cannot**:

* check real CPU usage
* restart a pod
* query a database
* fetch live data

---

So we add:

**Tool Layer = Ability to take action**

---

## 2) Real-World Example

User asks:

> “Why is my Kubernetes pod slow?”

System should:

* fetch metrics
* check logs
* maybe trigger scaling

 That requires **tools**, not just LLM

---

## 3) Types of Tools (Real Integration Layer)

---

### A) APIs (Most Common)

* REST APIs
* GraphQL

Example:

* Kubernetes API
* AWS CloudWatch
* Payment APIs

---

### B) Databases

* SQL (Postgres, MySQL)
* NoSQL (MongoDB, DynamoDB)

Use case:

* fetch user data
* query logs

---

### C) Web / External Data

* scraping
* external APIs
* third-party services

---

### D) Cloud Services

* AWS (CloudWatch, Lambda)
* Azure
* GCP

---

## 4) Lab 1: Simple Tool Integration (Manual)

---

### Step 1: Define Tool

```python
def get_cpu_usage():
    return "CPU usage is 85%"
```

---

### Step 2: Use with LLM

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4.1-mini")

tool_output = get_cpu_usage()

response = llm.invoke(f"Analyze this: {tool_output}")

print(response.content)
```

---

## Output

Example:

> CPU usage is high, system may be overloaded...

---

## Learning

* LLM is **not fetching data**
* You fetched → LLM interpreted

 Separation of roles

---

## 5) Problem with This Approach

Right now:

 You manually decide tool usage

But real systems need:

 LLM decides WHEN to use tool

---

## 6) Lab 2: Tool Calling Pattern

---

```python
from langchain.agents import initialize_agent, load_tools
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4.1-mini")

tools = load_tools(["llm-math"], llm=llm)

agent = initialize_agent(tools, llm)

response = agent.run("What is 25 * 4")

print(response)
```

---

## Output

LLM decides:

* Needs math
* Calls tool
* Returns result

---

## Learning

LLM becomes **decision maker**

---

## 7) Tool Calling vs API Orchestration (CRITICAL)

---

### Approach 1: Tool Calling (LLM decides)

Flow:

Input
→ LLM decides
→ Calls tool
→ Returns output

---

### Approach 2: API Orchestration (System decides)

Flow:

Input
→ System logic decides
→ Calls API
→ LLM processes

---

## Key Difference

| Aspect         | Tool Calling | API Orchestration |
| -------------- | ------------ | ----------------- |
| Control        | LLM          | System            |
| Flexibility    | High         | Medium            |
| Reliability    | Lower        | Higher            |
| Predictability | Low          | High              |

---

## Architect Decision

Use:

* Tool calling → dynamic tasks
* API orchestration → critical systems

---

## 8) Lab 3: Real API Simulation

---

```python
def get_pod_status():
    return "Pod restarted 5 times due to OOM"

query = "Why is my pod unstable?"

context = get_pod_status()

response = llm.invoke(f"{query} Context: {context}")

print(response.content)
```

---

## Output

* Explanation of OOM
* Suggestions

---

## Learning

This is **real RAG + Tool hybrid**

---

## 9) What to Measure (IMPORTANT)

Now your key focus:

---

### Metrics

| Metric             | Meaning                     |
| ------------------ | --------------------------- |
| Correct tool usage | Did system call right tool? |
| Latency            | Time taken                  |
| Accuracy           | Is answer correct?          |
| Failure rate       | Tool failures               |
| Cost               | API + LLM                   |

---

## 10) Real Failure Cases (Very Important)

---

### Case 1: Wrong Tool

LLM calls:

* DB instead of API

Wrong answer

---

### Case 2: No Tool Used

LLM guesses instead of fetching

Hallucination

---

### Case 3: Too Many Calls

LLM calls tool repeatedly

Cost + latency issue

---

## 11) Real System Design (Production Thinking)

---

### Pattern 1: Controlled Tool Usage

* System validates LLM decisions
* Guardrails before execution

---

### Pattern 2: Hybrid Control

* System decides critical tools
* LLM decides optional tools

---

### Pattern 3: Retry + Fallback

* Tool fails → retry
* fallback to LLM

---

## 12) Final Insight (CRITICAL)

Without tools:

AI can only talk

With tools:

AI can act

---

## 13) One Line Architect Insight

“LLM provides reasoning, tools provide real-world capability.”

---

## 14) What Reader Learns

After this section:

* How AI connects to real systems
* Difference between tool calling vs orchestration
* How to measure tool usage
* How to design reliable systems

---

## Next

5.4 Observability & Monitoring

This is where systems become debuggable and production-ready

