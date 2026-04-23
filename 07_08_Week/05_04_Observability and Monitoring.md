## 5.4 Observability and Monitoring

---

### 1) Context

At this stage, your system is no longer a simple LLM call. It retrieves information, uses memory, calls external tools, and makes decisions across multiple steps.

From the outside, everything still looks simple. A user asks a question and gets a response.

Internally, however, the system is doing much more — and when something goes wrong, it does not crash. It still returns an answer. The problem is that the answer may be incorrect, incomplete, slow, or unnecessarily expensive.

This creates a new challenge. You are no longer asking *"Does it work?"*

You are asking: **"Can I explain what happened inside the system?"**

Without that ability, your system is a black box. You can see input and output, but you cannot understand the process in between. That is not acceptable in production. Observability is what solves this.

---

### 2) What Observability Actually Means

Observability is the ability to reconstruct the full execution of any request. For any user query, you should be able to answer:

- What input was received and how was the prompt constructed?
- What data was retrieved — and was it relevant?
- Which tools were called and what did they return?
- Which model was used and how long did it take?
- What output was generated and why?

In traditional software, failures are visible as errors and crashes. In AI systems, failures are subtle. The system runs perfectly and still gives the wrong answer. Observability is how you detect, diagnose, and fix those silent failures.

---

### 3) What You Need to Observe

An AI system has several layers, and each one can fail differently:

- **Input layer** — Was the query received correctly? Was the prompt constructed properly?
- **Retrieval layer** — Did the system fetch the right documents? Were they relevant?
- **Orchestration layer** — Did the system make the right decision — which tool to call, which model to use?
- **LLM layer** — What was the final response? How many tokens were used? How long did it take?
- **System layer** — What is the overall latency, failure rate, and cost?

Each of these layers needs to be visible. If even one is a black box, you cannot fully trust the system.

---

### 4) Lab 1 — Basic Logging (Start Simple)

Before using any tools, start with the simplest form of observability: timing and printing.

```python
import time
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)

query = "Why is my pod restarting?"

start = time.time()
response = llm.invoke(query)
end = time.time()

print("Query    :", query)
print("Response :", response.content)
print("Latency  :", round(end - start, 2), "seconds")
```

**Expected output:**
```
Query    : Why is my pod restarting?
Response : Pods can restart due to OOM errors, failed health checks...
Latency  : 1.83 seconds
```

**What this gives you:** You can see the input and output together, and you know exactly how long the LLM took to respond.

**What this does not give you:** You still cannot see what happened between input and output. If the answer is wrong, you do not know why. The next lab fixes this.

---

### 5) Lab 2 — Step-Level Observability

Now add visibility into every step of the pipeline, not just the final answer.

```python
import time
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma

llm = ChatOpenAI(model="gpt-4o", temperature=0)

texts = [
    "Pods restart due to OOM (Out of Memory) errors",
    "Health checks failing can cause pod restarts",
    "Network issues can crash pods and trigger restarts"
]

db = Chroma.from_texts(texts, OpenAIEmbeddings())

query = "Why is my pod restarting?"
print("=" * 50)
print("STEP 1 — Input received")
print("Query:", query)

print("\nSTEP 2 — Running retrieval")
start_r = time.time()
docs = db.similarity_search(query)
end_r = time.time()

for i, doc in enumerate(docs):
    print(f"  [{i+1}] {doc.page_content}")
print("Retrieval latency:", round(end_r - start_r, 3), "seconds")

print("\nSTEP 3 — Calling LLM")
context = "\n".join([doc.page_content for doc in docs])
prompt = f"Answer using context below.\n\nContext:\n{context}\n\nQuestion: {query}"

start_l = time.time()
response = llm.invoke(prompt)
end_l = time.time()
print("LLM latency:", round(end_l - start_l, 3), "seconds")

print("\nSTEP 4 — Final response")
print(response.content)
print("=" * 50)
```

**Expected output:**
```
==================================================
STEP 1 — Input received
Query: Why is my pod restarting?

STEP 2 — Running retrieval
  [1] Pods restart due to OOM (Out of Memory) errors
  [2] Health checks failing can cause pod restarts
  [3] Network issues can crash pods and trigger restarts
Retrieval latency: 0.042 seconds

STEP 3 — Calling LLM
LLM latency: 1.76 seconds

STEP 4 — Final response
Pods can restart for several reasons including OOM errors...
==================================================
```

**What changed:** Now you can see the full picture. If the final answer is wrong, you check Step 2 — were the right documents retrieved? If the system is slow, you check which step has the highest latency. This is the difference between debugging blindly and debugging with evidence.

---

### 6) Debugging Real Failures

Without structured logging, these three failures all look identical from the outside — the system returns a wrong or slow answer. With observability, each one has a clear diagnosis.

**Case 1 — Wrong answer.** You inspect Step 2 and find irrelevant documents were retrieved. The problem is not the model — it is the retrieval layer.

**Case 2 — Slow response.** Step-level timing shows retrieval took 0.04 seconds but the LLM took 7.9 seconds. You investigate model load or switch to a faster model for this task.

**Case 3 — Hallucination.** Retrieval returned zero relevant documents, so the LLM had no grounding context and generated from memory. The fix is improving your retrieval, not your prompt.

The pattern is always the same: observability turns a mystery into a diagnosis.

---

### 7) What to Track in Every System

As your system grows, four dimensions become critical:

- **Correctness** — Are answers grounded and relevant? Is retrieval surfacing the right documents?
- **Performance** — How long does each step take? Where is time being spent?
- **Cost** — How many tokens are used per query? How often are models being called?
- **Reliability** — What percentage of requests fail? Are there silent errors or retries?

Together, these four metrics define the health of your system.

---

### 8) Where Basic Logging Stops Being Enough

Simple `print` statements work in a notebook. They break down the moment your system involves:

- multiple tools being called dynamically
- agents making non-deterministic decisions
- parallel LLM calls
- multi-user production traffic

At that point, you need structured tracing — a systematic record of every decision, every step, and every output, linked together into a single execution trace per request.

---

### 9) Advanced Observability — Tools Used in Production

---

#### LangSmith

LangSmith is purpose-built for LLM-based systems. It integrates directly with LangChain and gives you full visibility into every chain and agent run without changing your code significantly.

What it shows you:
- The full execution trace for every request — every prompt, every retrieval result, every tool call, every response
- Per-step latency and token usage — so you know exactly where time and money are going
- Side-by-side comparison of runs — so you can test whether a prompt change improved or degraded quality
- Automatic grouping of agent steps — so multi-step reasoning becomes readable instead of chaotic

In practice, LangSmith turns debugging from guesswork into a systematic process. You do not need to add logging everywhere — you look at the trace and see what happened.

---

#### OpenTelemetry

When your AI system is part of a larger architecture — sitting behind an API gateway, calling microservices, writing to databases — observability must extend beyond a single application.

OpenTelemetry is the industry standard for distributed tracing. It allows you to:
- Track a single user request as it flows across multiple services
- Identify exactly which service or step introduced a bottleneck
- Connect your AI system's traces to your broader infrastructure monitoring

This is essential when your system grows beyond a single Python process into a real production deployment.

---

#### Cloud Logging Systems

Cloud platforms provide centralised, scalable logging that complements tracing tools:

- **AWS CloudWatch** — logs, metrics, and alerts for AWS-hosted systems
- **GCP Cloud Logging** — integrated with Vertex AI and GKE deployments
- **Azure Monitor** — for Azure OpenAI and Azure-hosted services

These are not replacements for LangSmith or OpenTelemetry. They operate at the infrastructure level — tracking CPU, memory, error rates, and uptime — while tracing tools operate at the application level, tracking what your AI system decided and why.

---

### 10) Tracking Decisions and Flows in Agents

In simple RAG systems, the execution path is fixed. In agent-based systems, it is not. The agent decides at runtime:

- whether to retrieve data or use what it already knows
- which tool to call and with what parameters
- whether the result is sufficient or whether to loop again

This makes observability harder and more important at the same time. If the agent takes an unexpected path, you need to see the decision it made at each step — not just the final output.

Without decision-level tracing, a misbehaving agent is nearly impossible to debug. With it, you can see exactly where the reasoning went wrong.

---

### 11) Latency and Token Monitoring in Production

Two metrics become critical as usage grows.

**Latency** determines user experience. A correct answer that takes 15 seconds is not acceptable in most products. Per-step latency tracking lets you identify the bottleneck — whether it is retrieval, the model call, or something else — and optimize specifically for it rather than guessing.

**Token usage** determines cost. Large prompts, excessive context, repeated calls, and unnecessary memory injection all increase token count quietly. Monitoring token usage per step and per user lets you catch runaway costs before they become a problem, and design targeted optimizations — caching, context trimming, model routing — based on real data.

---

### 12) Production Design Principles

Three principles apply to every production AI system:

**Trace everything.** Every input, retrieval result, decision, tool call, and output should be logged with a timestamp and linked to the same request ID. You will not know what you need until something breaks.

**Monitor continuously.** Latency and quality degrade silently over time — as your data changes, as usage patterns shift, as model behavior evolves. Continuous monitoring catches degradation before users report it.

**Alert proactively.** Do not wait to discover failures through user complaints. Set thresholds — if latency exceeds 5 seconds, or failure rate crosses 2%, get notified immediately and investigate before the problem spreads.

---

### 13) Final Understanding

A system that works in a notebook is not the same as a system you can trust in production. The difference is not the model, not the framework, and not the prompt.

The difference is whether you can see inside it when something goes wrong.

Observability is what separates a demo from a deployable system.

> **If you cannot see what your AI system is doing, you cannot trust it. If you cannot trust it, you cannot scale it.**

---

**What you learned in this section:**
- How to move from basic timing to full step-level tracing
- How to diagnose wrong answers, slow responses, and hallucinations using evidence
- What to track in production — correctness, performance, cost, reliability
- How LangSmith, OpenTelemetry, and cloud logging systems work and when to use each
- How to trace agent decisions, not just outputs
- How to monitor latency and token usage as production metrics

---

*Next: **5.5 Evaluation and Testing** — where you stop assuming your system works and start measuring whether it actually does.*
