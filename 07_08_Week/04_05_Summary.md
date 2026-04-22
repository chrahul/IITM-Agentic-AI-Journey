# Sections 4.3 & 4.4: Orchestration & System Design Patterns

These two sections are about **how to architect AI systems** — not just use LLMs, but design them properly.

---

## 4.3 — Orchestration Patterns
*"How does the system decide and execute?"*

Think of these as **recipes** for solving different types of problems:

| Pattern | What it does | When to use |
|---|---|---|
| **Simple LLM Call** | Just ask the model | Basic Q&A, no frills |
| **Prompt Template** | Structured input → structured output | When consistency matters |
| **RAG** | Fetch relevant docs → give to LLM | Company data, reduce hallucinations |
| **Memory** | Remember past messages | Chatbots, conversations |
| **Tool Calling** | LLM decides to call an API | Real-time data, taking actions |
| **Agent** | LLM loops, reasons, and acts autonomously | Complex multi-step problems |
| **Hybrid** | Mix of all the above | Most real production systems |

The **key insight** here is: don't pick a framework (LangChain, LlamaIndex) first. **Pick the pattern first**, then use the framework to implement it.

---

## 4.4 — System Design Patterns
*"How is the system itself structured?"* — one level higher than 4.3.

These are **architectural decisions** that affect scalability, cost, and reliability:

- **Stateless vs Stateful** — Does the system need to remember things across turns? Stateless is simpler and cheaper; stateful gives better user experience.
- **Single vs Multi-Agent** — One agent doing everything, or specialized agents (planner, researcher, executor) collaborating? More agents = more power but more complexity.
- **Sync vs Async** — Does the user wait for the answer, or does it process in the background and notify later? Long tasks should be async.
- **Centralized vs Distributed** — One brain controlling everything, or multiple orchestrators? Distributed scales better but is harder to manage.
- **RAG vs Fine-Tuning** — Should you dynamically fetch knowledge (RAG) or bake it into the model (fine-tuning)? RAG for changing data, fine-tuning for stable domains.
- **Human-in-the-Loop** — For high-risk decisions (medical, financial), a human reviews before the AI acts.
- **Cost-Aware Architecture** — Actively designing to reduce token usage, cache responses, use smaller models where possible.

---

## The Big Picture

These two sections together teach you to think like this:

```
Problem
  → What orchestration pattern fits? (4.3)
    → How should the system be structured? (4.4)
      → Now pick your tools and implement
```

The core philosophy throughout both sections is the same: **there's no single right answer — only the right answer for your specific problem**. Complexity should be added only when the problem demands it.
