# Building Production-Grade Agentic AI Systems

> A senior engineer's notebook on what it actually takes to ship AI agents in production — beyond the demos, into the operational layer.

---

## The thesis

I was at AWS when Lambda took off. Teams pushed business-critical workflows into it fast — without failure handling, without execution boundaries, without asking what happens when it breaks at 2 a.m. Failures became invisible. Debugging became guesswork. The abstraction felt complete, until production proved otherwise.

Kubernetes, same era, same hype, worked at scale because it was a system: control plane, failure recovery, observability built in. Lambda was never a system. It was a component that needed one. Most teams skipped that part.

The same pattern is repeating with GenAI agents. Teams are wiring agents into logs, APIs, and live infrastructure, getting impressive early results, and skipping the uncomfortable questions: What happens when the agent acts on bad data? Who defines where it must not act? Where is the validation layer? Where does the model stop and the system take over?

> **A powerful component is not a complete system.**

This repository is my structured attempt to build out the system part — week by week, in the open — so that engineers and architects building Agentic AI in production have a reference for the parts most courses skip.

---

## About me

I'm **[Rahul Chaubey](https://www.linkedin.com/in/chaubeyrahul/)**, Director — Cloud Strategy at CloudX.
For over a decade I've worked across **AWS, Azure, OCI, AI/ML, GenAI, DevOps, and Cloud Infrastructure**, helping enterprises design and operate cloud platforms at scale.

This is my hands-on extension of that craft into Agentic AI and LLMOps engineering — applying the operational rigor cloud teams have refined for fifteen years to a workload type that's barely two years old.

---

## What's inside

The journey is organized week by week. Each week follows the same structure:

```
Context  →  Concepts  →  Intuition  →  System Design  →  Labs  →  Mini Project  →  Reflections
```

Notes capture what I learned. **Mini-projects capture what I built.** Reflections capture what actually clicked versus what only looked clear in the lecture.

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

## The system layer (parallel build track)

Alongside the IITM Pravartak curriculum, I'm running a parallel build track focused on the operational layer — the parts that turn an agent demo into a system you can run at 2 a.m.:

- **Observability** — Langfuse, OpenTelemetry GenAI conventions
- **Evaluation as a CI gate** — Ragas, Promptfoo, LLM-as-judge with bias controls
- **LLM gateways** — LiteLLM, semantic caching, fallback routing, per-tenant cost limits
- **Guardrails** — input/output filtering, prompt injection defense, secrets scanning
- **Multi-cloud deployment** — AWS Bedrock and Azure AI Foundry, side by side
- **Infrastructure as Code** — Terraform modules for the full LLM platform stack

These are the components most "build an AI agent" courses leave out, and they're exactly where my cloud and DevOps background carries over directly.

---

## Tech and tools

**Languages:** Python
**Frameworks:** LangChain, LangGraph, FastAPI, Pydantic
**Vector stores:** pgvector, FAISS, ChromaDB
**Models / APIs:** Anthropic Claude, OpenAI, AWS Bedrock, Azure OpenAI
**LLMOps:** Langfuse, LiteLLM, Ragas, Promptfoo
**Cloud and infra:** AWS, Azure, OCI, Kubernetes, Docker, Terraform

---

## How to navigate

- Browse week folders in order to follow the journey end to end.
- Each week's `README.md` summarizes what was built and what was learned that week.
- Mini-projects inside each week contain runnable code — that's where the actual systems live, not the notes.

---

## Connect

If you're building production Agentic AI systems, designing LLMOps platforms, or making a similar transition from cloud and DevOps into GenAI engineering, I'd be glad to compare notes.

📍 **LinkedIn:** [linkedin.com/in/chaubeyrahul](https://www.linkedin.com/in/chaubeyrahul/)

---

*Last updated: May 2026 · Active development*
