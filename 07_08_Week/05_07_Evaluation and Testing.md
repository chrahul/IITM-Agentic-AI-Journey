## 5.7 Evaluation and Testing

---

### 1) Context

Up to this point, your system can generate answers, retrieve relevant documents, use memory, call tools, and be monitored through observability. From an engineering perspective, everything is in place.

But one critical question remains unanswered:

**How do you actually know the system is correct?**

In traditional software, you write a unit test. The function either returns the right value or it does not. Pass or fail — the answer is binary.

In AI systems, correctness is not binary. The same input can produce slightly different outputs on different runs. A response can sound completely confident and be entirely wrong. A retrieval step can return documents that seem relevant but miss the most important one. An agent can take the right final action through the wrong sequence of steps.

This is why evaluation is not a final quality check you do before shipping. It is a core part of system design — something you build alongside the system, not after it.

---

### 2) What Evaluation Actually Means

In traditional software, you ask: *does the system run?*

In AI systems, you ask four different questions:

- Is the answer **correct** — does it reflect reality?
- Is it **grounded** — is it based on retrieved data, not fabricated?
- Is it **complete** — does it fully address the question?
- Is it **consistent** — does it produce reliable results across runs?

Evaluation is the process of answering these questions systematically, using evidence instead of intuition. Without it, you are guessing whether your system works. With it, you can prove it.

---

### 3) Three Areas You Must Evaluate

Every AI system has three distinct areas of evaluation, and each one can fail independently.

**Prompt evaluation** measures how well the LLM responds to a given instruction. The same question, asked with different prompt structure, can produce dramatically different outputs. Evaluation tells you which version actually performs better — not which one looks better to you.

**RAG evaluation** measures whether your retrieval layer is surfacing the right documents before the LLM ever sees them. This is the most commonly skipped evaluation step, and the most dangerous to skip. If retrieval is wrong, the final answer will be wrong regardless of how good your model is. The LLM cannot compensate for bad retrieval — it can only work with what it is given.

**Agent evaluation** goes beyond the final answer. In agent-based systems, the model makes decisions — which tool to call, in what order, with what parameters. You need to evaluate not just whether the answer was correct, but whether the agent took the right path to get there.

---

### 4) Lab 1 — Prompt Evaluation

This lab shows how prompt design directly impacts output quality — and how to evaluate the difference objectively.

```python
import os
os.environ["OPENAI_API_KEY"] = "sk-..."

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)

query = "Explain Kubernetes"

prompt1 = query

prompt2 = "Explain Kubernetes in simple terms with one real-world analogy and three key concepts"

response1 = llm.invoke(prompt1)
response2 = llm.invoke(prompt2)

print("=" * 50)
print("PROMPT 1 OUTPUT:")
print(response1.content)

print("=" * 50)
print("PROMPT 2 OUTPUT:")
print(response2.content)
```

**What to observe after running this:**

Do not just read both outputs and pick the one that sounds better. Evaluate them across specific dimensions:

| Dimension | Prompt 1 | Prompt 2 |
|---|---|---|
| Clarity | Rate 1–5 | Rate 1–5 |
| Structure | Rate 1–5 | Rate 1–5 |
| Usefulness | Rate 1–5 | Rate 1–5 |
| Appropriate depth | Rate 1–5 | Rate 1–5 |

**What you learn:** Prompt 2 will almost certainly score higher — not because the model is smarter, but because you gave it clearer instructions. This is the point. Evaluation makes that difference visible and measurable, instead of just felt.

---

### 5) Lab 2 — RAG Evaluation (Retrieval Quality)

This is the most important evaluation lab. Before you evaluate the LLM's answer, you must evaluate what it was given to work with.

```python
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma

llm = ChatOpenAI(model="gpt-4o", temperature=0)

documents = [
    "Pods restart due to OOM (Out of Memory) errors",
    "Health checks failing can cause pod restarts",
    "Network issues can crash pods and trigger restarts",
    "Kubernetes scheduler moves pods when nodes are under pressure",
    "Liveness probe failures trigger automatic pod restarts"
]

db = Chroma.from_texts(documents, OpenAIEmbeddings())

query = "Why is my pod restarting?"

print("Evaluating retrieval quality...")
retrieved_docs = db.similarity_search(query, k=3)

print("\nRetrieved documents:")
for i, doc in enumerate(retrieved_docs):
    print(f"  [{i+1}] {doc.page_content}")

print("\nRetrieval evaluation questions:")
print("  1. Are all retrieved documents relevant to the query?")
print("  2. Is any important document missing from the results?")
print("  3. Is there noise — documents that are not useful?")
```

**Expected output:**
```
Retrieved documents:
  [1] Pods restart due to OOM (Out of Memory) errors
  [2] Health checks failing can cause pod restarts
  [3] Liveness probe failures trigger automatic pod restarts

Retrieval evaluation questions:
  1. Are all retrieved documents relevant to the query?
  2. Is any important document missing from the results?
  3. Is there noise — documents that are not useful?
```

**What you are doing here:** You are evaluating the retrieval layer in isolation — before passing anything to the LLM. Ask yourself: if someone handed you only these three documents and asked you to answer the query, could you give a good answer? If yes, retrieval is working. If not, the problem is here — and no amount of prompt tuning will fix it.

This is the mindset shift that most people miss. **When an AI system gives a wrong answer, the instinct is to fix the prompt or change the model. Most of the time, the real problem is in retrieval.**

---

### 6) Lab 3 — End-to-End Pipeline Evaluation

Now evaluate the full system — retrieval plus LLM — as a single unit.

```python
context = "\n".join([doc.page_content for doc in retrieved_docs])

response = llm.invoke(
    f"Use only the context below to answer the question. "
    f"If the context does not contain enough information, say so.\n\n"
    f"Context:\n{context}\n\n"
    f"Question: {query}"
)

print("Final answer:")
print(response.content)

print("\nEnd-to-end evaluation questions:")
print("  1. Does the answer use the retrieved context?")
print("  2. Does it introduce any information not in the context?")
print("  3. Is it complete — does it address all aspects of the query?")
print("  4. Is it useful to the person who asked?")
```

**What to look for:** The phrase *"use only the context below"* in the prompt is deliberate. It forces the model to stay grounded and makes hallucination easier to detect — if the answer contains something that is not in the retrieved documents, it was fabricated. That is your signal to improve retrieval, tighten the prompt, or both.

---

### 7) Accuracy Measurement

Accuracy in AI systems is not a single number. It is a profile across multiple dimensions. A simple but effective approach is to score each output across the dimensions that matter for your use case:

| Dimension | What it measures | Score (1–5) |
|---|---|---|
| Correctness | Is the answer factually accurate? | |
| Groundedness | Is it based on retrieved data, not fabricated? | |
| Completeness | Does it fully answer the question? | |
| Clarity | Is it easy to understand? | |
| Relevance | Does it address what was actually asked? | |

Run this scoring across multiple queries. Over time, patterns emerge — maybe retrieval scores well but groundedness is weak, meaning the model is going beyond its context. Maybe correctness is high but completeness is low, meaning retrieval is missing parts of the answer. Each pattern points to a specific fix.

---

### 8) Hallucination Detection

Hallucination is when the model generates information that is not supported by the context it was given — it sounds plausible, it is stated confidently, and it is wrong.

The practical way to detect it:

- Compare the final answer against the retrieved documents word by word
- Identify any claim in the answer that cannot be traced back to the context
- Flag it as a hallucination

The structural fix is almost always in retrieval or prompt design, not in the model itself. If the retrieved documents are comprehensive and the prompt explicitly instructs the model to stay within them, hallucination drops significantly. The instruction *"if the context does not contain enough information, say so"* is a simple but effective guardrail.

---

### 9) Regression Testing

Once your system is working well, you need to make sure it keeps working well as you make changes — to your prompts, your retrieval system, your model version, or your data.

This is regression testing applied to AI systems.

Build a set of test cases — known queries with known expected characteristics:

```python
test_cases = [
    {
        "query": "Why is my pod restarting?",
        "expected_topics": ["OOM", "health check", "liveness probe"],
        "should_not_contain": ["DNS", "ingress", "service mesh"]
    },
    {
        "query": "How do I scale a deployment?",
        "expected_topics": ["replicas", "kubectl scale", "HorizontalPodAutoscaler"],
        "should_not_contain": ["pod restart", "OOM"]
    }
]
```

Run these test cases after every significant change to your system. If a previously correct answer degrades, you catch it immediately — before it reaches users.

The standard you are aiming for: **any change to the system that degrades evaluation scores should be visible before it ships.**

---

### 10) Tools for Evaluation at Scale

Manual evaluation works when you have ten test cases. It breaks down when you have a hundred. Three tools handle this at scale:

**LangSmith** — already covered in observability. Beyond tracing, it lets you tag and score runs, compare evaluation results across different prompt versions, and build datasets of known queries and expected outputs for automated testing.

**RAGAS** — purpose-built for RAG evaluation. It measures retrieval quality automatically across metrics like context precision (did the retrieved docs contain the answer?) and faithfulness (did the generated answer stay within the retrieved context?). This is the tool to reach for when you need to evaluate retrieval at scale without manually inspecting every result.

**DeepEval** — a testing framework for LLM systems. It lets you write evaluation assertions in Python — similar to unit tests — that check whether outputs meet specific criteria. This bridges the gap between traditional software testing and AI evaluation.

The approach: start with manual scoring as in the labs above. Integrate LangSmith as your system grows. Add RAGAS when your RAG pipeline is complex enough to need automated retrieval metrics. Use DeepEval when you want evaluation to run as part of your CI/CD pipeline.

---

### 11) A Simple Evaluation Loop for Any System

Regardless of the tools you use, this three-question loop applies to every query in every AI system:

```
1. Did we retrieve the right information?
   → If no: fix the retrieval layer

2. Did the model use it correctly?
   → If no: fix the prompt or add guardrails

3. Is the final answer useful?
   → If no: re-examine both retrieval and prompt together
```

This loop — run systematically across a representative set of test queries — will catch the majority of issues before users ever see them.

---

### 12) Final Understanding

A system that produces answers is not necessarily a good system. A system that can prove its answers are correct is a reliable system.

The difference between the two is evaluation. It is also the difference between a system you demo and a system you deploy with confidence.

Most teams skip evaluation because it feels like extra work. In practice, it is the opposite — it saves time by making problems visible early, when they are cheap to fix, instead of late, when they have already reached users.

> **If you are not measuring your system, you are guessing. And in production, guessing is not a strategy.**

---

**What you learned in this section:**
- Why AI evaluation is fundamentally different from traditional software testing
- How to evaluate prompts, retrieval, and full pipelines independently
- How to measure accuracy across multiple dimensions instead of a single score
- How to detect and reduce hallucination structurally
- How to build regression tests that protect against quality degradation
- When to use LangSmith, RAGAS, and DeepEval

---
Great question. Let me break it down the way you would explain it to a student.

---

## What just happened — plain English

You gave the system **5 documents** (your knowledge base):

```
1. Pods restart due to OOM errors
2. Health checks failing can cause restarts
3. Network issues can crash pods
4. Kubernetes scheduler moves pods when nodes are under pressure
5. Liveness probe failures trigger automatic pod restarts
```

You asked one question:
```
"Why is my pod restarting?"
```

The system returned **3 most relevant documents**:
```
[1] Pods restart due to OOM errors
[2] Health checks failing can cause restarts
[3] Network issues can crash pods
```

---

## How to explain this to a student

Tell them this story:

> Imagine you are a new engineer. Your senior gives you **5 sticky notes** — each one explains a different Kubernetes problem.
>
> A user comes and asks: *"Why is my pod restarting?"*
>
> You don't read all 5 notes out loud. You quickly scan them and pick the **3 most related ones** to answer the question.
>
> That is exactly what this system just did.

---

## Now answer the three evaluation questions together

Walk the student through each question out loud:

---

**Question 1 — Are all retrieved documents relevant?**

Look at what came back:
```
[1] OOM errors         ← directly causes restarts ✓
[2] Health checks      ← directly causes restarts ✓
[3] Network issues     ← can cause pod crashes    ✓
```
Yes — all three are relevant. Retrieval passed this check.

---

**Question 2 — Is anything important missing?**

Look at what did NOT come back:
```
[4] Kubernetes scheduler moves pods  ← not about restarting
[5] Liveness probe failures          ← THIS causes restarts!
```

Document 5 about liveness probes was missed — and liveness probe failures are a very common cause of pod restarts. This is a gap in retrieval.

**This is the most important teaching moment.**

Tell the student:

> "The system missed document 5. If a user's pod is restarting because of a liveness probe failure, the system would give them an incomplete answer — not because the model is bad, but because retrieval didn't surface the right document."

---

**Question 3 — Is there noise?**

Look at document 3:
```
[3] Network issues can crash pods
```

Network issues crash pods — but crashing is slightly different from restarting. This document is borderline. It is not wrong to include it, but it is the weakest of the three.

---

## The lesson to leave with the student

Draw this on a whiteboard or show it as text:

```
Good retrieval  →  LLM has right context  →  Good answer
Bad retrieval   →  LLM has wrong context  →  Wrong answer
                   (even if model is perfect)
```

Then say:

> "This is why we evaluate retrieval first — before we even look at what the LLM said. A great model cannot fix bad retrieval. Garbage in, garbage out."

---

That one phrase — **garbage in, garbage out** — is what students remember. The rest is the evidence that proves it.
---

*Next: **5.8 Security and Guardrails** — where we make the system safe enough to actually put in front of users.*
