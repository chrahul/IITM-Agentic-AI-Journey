# IITM Agentic AI Journey

> **Documenting my transition from Cloud Strategy & DevOps leadership into production-grade Agentic AI / LLMOps engineering.**

---

## About

I'm **[Rahul Chaubey](https://www.linkedin.com/in/chaubeyrahul/)**, Director — Cloud Strategy at CloudX.
For over a decade, I've worked across **AWS, Azure, OCI, AI/ML, GenAI, DevOps and Cloud Infrastructure**, helping enterprises design and operate cloud platforms.

This repository is my structured 6-month journey to extend that craft into **Agentic AI and LLMOps** — building, deploying, and operating LLM-powered systems with the same rigor we apply to traditional cloud workloads.

---

## Why this repository exists

GenAI today is chaotic. Teams want to ship LLM-powered solutions, but very few engineers have **end-to-end** clarity on what it actually takes to run one in production. Most treat the LLM as the system. It isn't.

> *A powerful abstraction is not a complete system.*

A model behind an API is just one component. Real production GenAI requires retrieval, memory, evaluation, observability, guardrails, cost control, IaC, and the operational discipline that cloud and DevOps engineers have been refining for fifteen years.

This repository is my attempt to build that complete picture — week by week, in the open — so that it eventually serves as a reference others can use to build production-grade Agentic AI systems, not just demos.

---

## What's inside

The journey is organized week-by-week. Each week follows the same structure:

```
Context  →  Concepts  →  Intuition  →  System Design  →  Labs  →  Mini Project  →  Reflections
```

Notes capture what I learned. **Mini-projects capture what I built.** Reflections capture what actually clicked versus what looked clearer than it was.

| # | Week / Module | Status |
|---|---|---|
| 00 | Foundations | Pending |
| 01 | Python Refresher | ✅ Complete |
| 02 | AI / ML Basics | ✅ Complete |
| 03 | LLM Fundamentals | ✅ Complete |
| 04 | Prompt Engineering | ✅ Complete |
| 05 | LangChain Intro | ✅ Complete |
| 06 | Embeddings & Vector Search | 🔨 In Progress |
| 07 | Agents & Tools | Upcoming |
| 08 | Agent Architecture | Upcoming |
| 09 | Memory & RAG | Upcoming |
| 10 | Advanced RAG | Upcoming |
| 11 | Evaluation & Observability | Upcoming |
| 12 | Ethics & Governance | Upcoming |
| 13 | Capstone Project | Upcoming |

---

## Parallel build track: LLMOps focus

Alongside the IITM Pravartak curriculum, I'm running a parallel build track focused on the operational layer most courses skim past:

- LLM observability (Langfuse, OpenTelemetry GenAI)
- Evaluation as a CI gate (Ragas, Promptfoo, LLM-as-judge)
- LLM gateways, semantic caching, cost control (LiteLLM)
- Guardrails and prompt-injection defense
- Multi-cloud deployment on AWS Bedrock and Azure AI Foundry
- IaC for LLM platforms (Terraform modules)

This is the layer that turns a notebook demo into a production system — and the layer where my cloud and DevOps background carries over directly.

---

## Tech & tools used

**Languages:** Python
**Frameworks:** LangChain, LangGraph, FastAPI, Pydantic
**Vector stores:** pgvector, FAISS, ChromaDB
**Models / APIs:** Anthropic Claude, OpenAI, AWS Bedrock, Azure OpenAI
**LLMOps:** Langfuse, LiteLLM, Ragas, Promptfoo
**Cloud & infra:** AWS, Azure, OCI, Kubernetes, Docker, Terraform

---

## How to navigate this repo

- Browse week folders in order if you're following the journey end-to-end.
- Each week's `README.md` summarizes what was built and what was learned.
- `06_Mini_Project/` inside each week contains runnable code — that's where the actual systems live, not the notes.

---

## Connect

If you're working on production Agentic AI systems, designing LLMOps platforms, or making a similar transition from cloud/DevOps into GenAI engineering — I'd be glad to compare notes.

📍 **LinkedIn:** [linkedin.com/in/chaubeyrahul](https://www.linkedin.com/in/chaubeyrahul/)

---

*Last updated: May 2026 · Active development*
