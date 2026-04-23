## 5.4 Observability and Monitoring

---

### 1) Context

You have now built systems that integrate LLMs, retrieve documents, and call external tools. The code runs, the output looks reasonable, and everything seems fine.

But here is the real problem:

**You do not actually know what happened inside.**

When something goes wrong — and in production, it will — you will not know:
- Why the system gave a wrong answer
- Which step failed
- How long each part took
- Whether the retrieval was relevant or not

Without observability, your AI system is a black box. You can see what went in and what came out, but nothing in between. That is not acceptable in production.

This section fixes that.

---

### 2) What Observability Actually Means

Observability is not just logging. It is the ability to answer three questions at any point in time:

- **What happened?** — the full trace of inputs, decisions, and outputs
- **Why did it happen?** — the reasoning path the system took
- **Where did it fail?** — the exact step that broke

In traditional software, debugging is hard. In AI systems, it is harder — because the failure is often not an error or a crash. The system runs perfectly and still gives a wrong answer. Observability is how you catch that.

---

### 3) What You Need to Observe

<img width="1440" height="1040" alt="image" src="https://github.com/user-attachments/assets/efb62cde-d92c-4e0d-a069-f087b4e04a18" />


An AI system has several layers, and each one can fail differently:

- **Input layer** — Was the user query received correctly? Was the prompt constructed properly?
- **Retrieval layer** — Did the system fetch the right documents? Were they relevant to the query?
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

**Expected Output:**
```
Query    : Why is my pod restarting?
Response : Pods can restart due to OOM errors, failed health checks, or...
Latency  : 1.83 seconds
```

**What this gives you:**
- You can see the input and output together
- You know exactly how long the LLM took to respond
- You can spot if latency is unusually high

**What this does not give you:**
- You still cannot see what happened between input and output
- If retrieval was involved, you have no visibility into what was fetched
- If the answer is wrong, you do not know why

This is a starting point, not a solution. The next lab fixes this.

---

### 5) Lab 2 — Structured Step-by-Step Logging

Now add visibility into every step of the system, not just the final answer.

```python
import time
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma

llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Build vector store
texts = [
    "Pods restart due to OOM (Out of Memory) errors",
    "Health checks failing can cause pod restarts",
    "Network issues can crash pods and trigger restarts"
]

embeddings = OpenAIEmbeddings()
db = Chroma.from_texts(texts, embeddings)

# --- Observability starts here ---

query = "Why is my pod restarting?"
print("=" * 50)
print("STEP 1 — Input received")
print("Query:", query)

print("\nSTEP 2 — Running retrieval")
start_retrieval = time.time()
docs = db.similarity_search(query)
end_retrieval = time.time()

print("Retrieved documents:")
for i, doc in enumerate(docs):
    print(f"  [{i+1}] {doc.page_content}")
print("Retrieval latency:", round(end_retrieval - start_retrieval, 3), "seconds")

print("\nSTEP 3 — Calling LLM")
context = "\n".join([doc.page_content for doc in docs])
prompt = f"Answer the question using the context below.\n\nContext:\n{context}\n\nQuestion: {query}"

start_llm = time.time()
response = llm.invoke(prompt)
end_llm = time.time()

print("LLM latency:", round(end_llm - start_llm, 3), "seconds")

print("\nSTEP 4 — Final Response")
print(response.content)
print("=" * 50)
```

**Output:**
```
==================================================
STEP 1 — Input received
Query: Why is my pod restarting?

STEP 2 — Running retrieval
Retrieved documents:
  [1] Pods restart due to OOM (Out of Memory) errors
  [2] Health checks failing can cause pod restarts
  [3] Network issues can crash pods and trigger restarts
Retrieval latency: 0.58 seconds

STEP 3 — Calling LLM
LLM latency: 3.348 seconds

STEP 4 — Final Response
Your pod could be restarting due to several reasons based on the context provided:

1. **OOM (Out of Memory) Errors**: If your pod is consuming more memory than what is allocated, it can lead to OOM errors, causing the pod to restart.

2. **Health Check Failures**: If the health checks configured for your pod are failing, it can trigger a restart as the system attempts to recover and ensure the pod is running correctly.

3. **Network Issues**: Problems with the network can cause pods to crash, which may lead to restarts as the system tries to re-establish connectivity and maintain service availability.

You may need to investigate logs and metrics to determine the specific cause of the restarts in your case.
==================================================
```

**What changed:**

Now you can see the full picture. If the final answer is wrong, you check Step 2 — were the right documents retrieved? If the system is slow, you check which step has the highest latency. If retrieval returned irrelevant docs, you know the problem is in your vector store, not the LLM.

This is the difference between debugging blindly and debugging with evidence.

---

### 6) Real Failure Examples — What Observability Catches

Without structured logging, all three of these failures look identical from the outside: the system returns a wrong or incomplete answer.

**Case 1 — Wrong Answer**
The LLM responds confidently but incorrectly. With observability you check Step 2 and find the retrieved documents were irrelevant. The problem is in the retrieval layer, not the model.

**Case 2 — Slow Response**
Total latency is 8 seconds. With step-level timing you find retrieval took 0.04 seconds but the LLM took 7.9 seconds. You investigate model load or switch to a faster model for this task.

**Case 3 — Hallucination**
The answer sounds correct but is fabricated. With observability you see that retrieval returned zero relevant documents, so the LLM had no grounding context and generated from memory. The fix is improving your retrieval, not your prompt.

**The pattern is always the same:** observability turns a mystery into a diagnosis.

---

### 7) What to Measure in Production

Once you move beyond notebooks, you need to track four categories continuously:

- **Quality** — Is the answer correct? Is retrieval returning relevant documents?
- **Performance** — What is the end-to-end latency? What is the latency per step?
- **Cost** — How many tokens are being used per query? What is the daily API spend?
- **Reliability** — What percentage of requests fail? Are there retries happening?

These four metrics together tell you whether your system is healthy.

---

### 8) Industry Tools

Manual logging gets you started. At scale, you need dedicated tools:

- **LangSmith** — Purpose-built for LLM systems. Traces every chain and agent run, lets you compare outputs across runs, and helps you debug retrieval and prompt issues visually.
- **OpenTelemetry** — The industry standard for distributed tracing. Useful when your AI system is part of a larger microservices architecture.
- **Cloud Logging** — AWS CloudWatch, GCP Cloud Logging, and Azure Monitor for infrastructure-level metrics like failure rates and latency percentiles.

Start with structured logging as in Lab 2. Integrate LangSmith when your system grows beyond a single notebook. Add OpenTelemetry when you deploy to production infrastructure.

---

### 9) Production Design Principles

Three principles that apply to every production AI system:

**Trace everything.** Every input, every retrieval result, every LLM call, and every output should be logged with a timestamp. You will not know what you need until something breaks.

**Monitor continuously.** Latency and quality can degrade silently over time — as your data changes, as usage patterns shift, or as model behaviour changes. Continuous monitoring catches this before users do.

**Alert proactively.** Do not wait to discover failures through user complaints. Set thresholds — if latency exceeds 5 seconds, or if failure rate crosses 2%, get notified immediately.

---

### 10) Final Understanding

Here is the honest reality of production AI systems:

A system that works in a notebook is not the same as a system you can trust in production. The difference is not the model, not the framework, and not the prompt. The difference is whether you can see inside it when something goes wrong.

Observability is what separates a demo from a deployable system.

> **If you cannot debug your AI system, you cannot scale it. If you cannot scale it, it has no real value.**

---

**What you learned in this section:**
- Why observability matters and what it actually means in AI systems
- How to add basic timing and logging to any LLM call
- How to trace every step of a RAG pipeline with structured logging
- How to connect a wrong output back to its root cause
- What to measure in production and which tools to use

---

*Next: **5.5 Evaluation & Testing** — where we go beyond logging and actually measure whether the system is giving correct answers.*
