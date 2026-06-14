# Agents to CrewAI: 
---

## What is this

The Week 12 mini-project asks you to design a 4-agent banking resolution system. To build it *well* (not just pass), you need a working mental model of three things:

1. What an *agent* actually is — versus a chatbot, versus an LLM call.
2. Why *multi-agent* is a different beast from chaining LLM calls.
3. How *CrewAI* expresses these ideas in code — and where it hides decisions that you should be making explicitly.

This course gets you there. It uses your existing knowledge of embeddings and transformers as the floor and walks you up to architecture-review confidence.

**You will not write code in Modules 0–8.** That is intentional. The grading rubric rewards architecture and collaboration logic, not framework trivia. Code happens in Module 9, once the mental model is in place.

---

## Course principles

- **Bottleneck-first.** Every module opens with "what was broken in the previous approach." If you can't name the bottleneck, you don't understand why the thing exists.
- **Teach-It-Back is mandatory.** At the end of each module, you explain the concept in your own words before we move on. If it comes out fuzzy, we go back.
- **Banking domain throughout.** Every analogy and example uses the assignment domain, so the mental model maps directly when you sit down to code.
- **Production-shaped where it matters.** We flag what a toy version misses — cost, observability, failure modes — even when the assignment doesn't require it.

---

## Map of the course

| # | Module | Hours | Key skill for Week 12 |
|---|---|---|---|
| 0 | The Bottleneck Map | 0.5 | Frames why agents exist at all |
| 1 | Anatomy of an Agent | 1.0 | Rubric 2.1 — agent role clarity |
| 2 | Tools — how agents touch the world | 0.75 | Rubric 2.4 — tool use & decision making |
| 3 | Memory and State | 0.5 | How task outputs flow between agents |
| 4 | The Multi-Agent Leap | 1.0 | Rubric 2.2 — collaboration logic |
| 5 | Agent Framework Landscape | 0.5 | Defending your choice of CrewAI |
| 6 | CrewAI Deep Dive | 2.5 | Everything in code |
| 7 | Designing the Assignment Architecture | 1.5 | Rubric 2.1–2.4 — the whole graded surface |
| 8 | Production Polish | 0.75 | Rubric 2.5 + your own bar |
| 9 | Implementation Sprint | self-paced | The actual submission |
| 10 | Teach-It-Back Capstone | 0.5 | Mastery check before you ship |

Total trainer-led time: ~10 hours, split across whatever cadence you want.

---

## Module 0: The Bottleneck Map

**Why this module exists**
"Agent" is a loaded word — RL researchers, enterprise vendors, and the LangChain crowd all use it differently. Before learning specifics, fix where this concept lives in the AI stack.

**What we cover**
- The evolution: tokens → embeddings → transformers → LLMs → tool-using LLMs → agents → multi-agent → agentic platforms
- What each layer can and cannot do
- The four bottlenecks a vanilla LLM hits: stale knowledge, no actions, no memory beyond context, no task decomposition
- Where Week 12 sits on the map (and where it doesn't go — no RAG, no long-term memory, no learning loops)

**Teach-It-Back checkpoint**
Define "agent" in two sentences without using the word "agent." Then name the four bottlenecks of a plain LLM call.

**Time:** ~30 min

---

## Module 1: Anatomy of an Agent

**The bottleneck**
A single LLM call is a stateless function: text in, text out. Useful for summarization, hopeless for "go figure out why this transaction failed."

**Core concept**
An agent is a **loop**, not a call. The canonical shape (the ReAct pattern, Yao et al. 2023):

```
Thought → Action → Observation → Thought → ... → Final Answer
```

- The LLM is the *brain* — decides what to do.
- Tools are the *hands* — actually do it.
- Memory is the *notebook* — remember what happened.
- The loop is the *body* — keeps everything running until a stopping condition.

**Key questions answered**
- Why ReAct outperformed plain Chain-of-Thought
- What "stopping condition" means — and why infinite loops happen in practice
- The difference between an agent and a chatbot (a chatbot has no tools and no autonomous loop)

**Teach-It-Back checkpoint**
Explain ReAct to a junior engineer using a banking example. Use the words Thought / Action / Observation correctly.

**Where this shows up in Week 12:** Each of your 4 agents internally runs a small ReAct-style loop — CrewAI handles it, but you should know what's running under the hood.

**Time:** ~1 hour

---

## Module 2: Tools — how agents touch the world

**The bottleneck**
LLMs hallucinate facts and cannot perform actions. They cannot check whether ₹50,000 actually left the account. Without tools, an "agent" is just a wordier chatbot.

**Core concept**
Function calling: a structured contract where the LLM, instead of generating prose, produces JSON specifying *which tool* to call with *which arguments*. The runtime executes the tool, appends the result to the conversation, and the LLM continues.

A tool is defined by four things: **name, description, parameter schema, return value**. The description is what the LLM "reads" to decide whether to use it. Writing tool descriptions is a real skill — most failures are bad descriptions, not bad code.

**Key questions answered**
- Why function calling beat earlier "please respond in this JSON format" prompt tricks
- When to use a tool versus letting the LLM reason
- How to design a tool's interface so the LLM picks it correctly

**Teach-It-Back checkpoint**
Design three tools for the Resolution Agent in Week 12. For each, write: name, one-line description as the LLM will see it, parameters, return type.

**Where this shows up in Week 12:** Rubric 2.4 (Tool Use & Decision Making, 15 marks) explicitly grades this. You'll likely write at least one custom tool — probably a policy lookup or a risk scoring tool.

**Time:** ~45 min

---

## Module 3: Memory and State

**The bottleneck**
LLMs are amnesiac between calls. In a 4-agent pipeline, if Agent 2 forgets what Agent 1 said, the chain breaks.

**Core concept**
Four memory types worth knowing:

1. **Short-term (conversational):** the running message history
2. **Long-term (semantic):** vector store + embeddings — this is where your existing knowledge applies
3. **Structured:** databases, key-value stores
4. **Episodic:** "things that happened in past sessions"

For Week 12 you mostly use type 1. CrewAI passes outputs between tasks via a `context` parameter, which is short-term memory in action. The other types matter when you scale to a real system.

**Teach-It-Back checkpoint**
Which memory type would you use for: (a) remembering this conversation, (b) recalling that ₹50,000+ unauthorized transactions always escalate to L2 support, (c) the customer's account number for this session?

**Where this shows up in Week 12:** The `context=[task_1]` parameter on a CrewAI Task is exactly how Agent 2 reads Agent 1's output. Module 6 makes this concrete.

**Time:** ~30 min

---

## Module 4: The Multi-Agent Leap

**The bottleneck**
You *can* build a single "god agent" with 17 tools and a 4000-token system prompt. It will be brittle, expensive per call, hard to debug, and will misclassify because it's trying to be everything at once. This is the engineering equivalent of one person doing requirements, architecture, coding, testing, and ops — possible, but not how grown-up systems work.

**Core concept**
Specialization. Adam Smith's pin factory: one person can make 20 pins a day; ten people each doing one step can make 48,000. Same idea applied to LLM reasoning.

Coordination patterns to know:

- **Sequential pipeline** (assembly line): A → B → C → D. *This is what Week 12 uses.*
- **Hierarchical** (manager-worker): a planner agent delegates to specialists, collects results.
- **Parallel + merge:** multiple specialists work concurrently, a synthesizer combines.
- **Debate / critic:** agents argue or critique each other's output to converge on quality.

**Key questions answered**
- When multi-agent is overkill (more often than the hype suggests)
- Why the sequential pattern fits the banking resolution problem so cleanly
- The cost and latency tradeoffs — each agent is at least one LLM call

**Teach-It-Back checkpoint**
Argue why the Week 12 problem is a sequential pipeline and not a parallel or hierarchical pattern. Then argue the other side: when would hierarchical be better?

**Where this shows up in Week 12:** Rubric 2.1 (role clarity) + 2.2 (collaboration logic) — 50 of the 100 marks.

**Time:** ~1 hour

---

## Module 5: Agent Framework Landscape

**The bottleneck**
You could build all of the above from raw `anthropic` or `openai` SDK calls in a `while` loop. People do. It's painful past two agents — you end up writing your own framework. Better to pick one that's already paid that cost.

**Core concept**

| Framework | Mental model | Strengths | Weaknesses |
|---|---|---|---|
| LangChain agents | General-purpose, chain-of-everything | Mature, huge ecosystem | Heavy abstractions, fast-moving API |
| LangGraph | Explicit state machine (graph of nodes) | Fine-grained control, great for complex flows | More boilerplate, steeper learning curve |
| AutoGen | Conversation between agents | Natural for debate/critic patterns | Less structured for pipelines |
| CrewAI | Team of specialists with roles and tasks | Maps cleanly to "team of experts," low ceremony | Opinionated, less flexible than LangGraph |

**Why Week 12 uses CrewAI:** the assignment is literally "a team of specialists with defined roles passing work down a line." This is CrewAI's sweet spot.

**Teach-It-Back checkpoint**
Name one scenario where you would *not* pick CrewAI, and what you would pick instead. Be specific.

**Time:** ~30 min

---

## Module 6: CrewAI Deep Dive

This is the longest module. We'll do it in three sub-sessions.

### 6.1 Setup and the four primitives (45 min)
- Installation, environment variables, LLM provider config (OpenAI, Anthropic, local Ollama)
- The four primitives: **Agent, Task, Crew, Process**
- A ten-line "hello crew" mental model

### 6.2 Agent and Task in depth (1 hour)
- **Agent attributes:** `role`, `goal`, `backstory`, `tools`, `verbose`, `allow_delegation`, `llm`, `max_iter`
- The role/goal/backstory triple — what each one actually does in the prompts CrewAI generates for you
- **Task attributes:** `description`, `expected_output`, `agent`, `context` (the dependency mechanism), `tools`, `output_file`
- Why `expected_output` matters more than people give it credit for
- How `context=[task1, task2]` creates the dependency graph

### 6.3 Crew, Process, and custom tools (45 min)
- `Crew(agents=[...], tasks=[...], process=Process.sequential)`
- `Process.sequential` versus `Process.hierarchical` (manager agent)
- Writing a custom tool with the `@tool` decorator
- Lifting the hood: inspecting what CrewAI actually sends to the LLM on your behalf

**Teach-It-Back checkpoint** (after 6.3)
Explain to a junior engineer: what's the difference between an Agent and a Task in CrewAI? Why are they separate concepts at all?

**Where this shows up in Week 12:** Everything from this module shows up in Section 8 (CrewAI Implementation Plan) of the assignment.

**Time:** ~2.5 hours total

---

## Module 7: Designing the Assignment Architecture

This is where we treat Week 12 as a design problem, not a coding problem. You'll walk away with a one-page design doc you can hand to a reviewer.

**Design questions we work through:**
1. Where does the escalation rule logic live — in the agent's prompt, in a tool, or in post-processing code? (There's a defensible answer either way; pick one and own it.)
2. How do you make the Risk Agent's output structured — so downstream code can act on `escalate: yes/no` — instead of free-form prose?
3. What test cases beyond the four given will exercise edge cases the evaluator respects?
4. How granular should the agent prompts be? (Spoiler: less granular than you think; over-specification hurts.)
5. Where do sample customer queries come from — hardcoded list, CSV file, generated?

**Teach-It-Back checkpoint**
Present a one-page architecture doc covering: agent roles (one line each), input/output contracts, dependency graph, where escalation logic lives, and one design tradeoff you considered and rejected.

**Where this shows up in Week 12:** Rubric 2.1, 2.2, 2.3, 2.4 — 85 of the 100 marks.

**Time:** ~1.5 hours

---

## Module 8: Production Polish

The assignment doesn't *require* production polish — but you do (your principle: production-shaped from day one). This module is short and aimed at making the submission look like something a senior engineer wrote, not a student.

- Project structure: not a single notebook cell — modules for `agents/`, `tools/`, `tasks/`, `config/`
- A README that opens with the architecture diagram, not the install command
- Logging agent decisions for auditability (this matters for banking, and matters to the evaluator)
- Cost estimation per run: back-of-envelope — 4 agents × ~2 LLM calls each × per-token cost
- Token-budget awareness: what happens if a customer query is 2000 tokens?
- Error handling: what if Agent 1 returns "I don't know" for intent?

**Teach-It-Back checkpoint**
Without looking, list five things your submission will have that a typical student submission won't.

**Time:** ~45 min

---

## Module 9: Implementation Sprint (self-paced)

Now you write. Suggested order:

1. Environment up; verify one LLM call works
2. Minimal `Crew` with 1 agent and 1 task — "hello crew" baseline
3. Add Agent 1 (Intent Classifier) only; test on all 4 sample queries
4. Add Agent 2 (Policy); verify it reads Agent 1's output via `context`
5. Add Agents 3 and 4
6. Wire in escalation logic per your Module 7 decision
7. Run all 4 test cases; capture outputs
8. Polish per Module 8
9. README + architecture diagram

I will not write this code for you. I will help with bugs, design pivots, and code reviews on what you've written. End-of-day check-ins require you show the actual code, as usual.

---

## Module 10: Teach-It-Back Capstone

Before submission, record (written or video — your call) a five-minute walkthrough covering:

- The architecture and why it's a sequential pipeline
- Where each rubric criterion is satisfied in the code
- One thing you'd change with another week
- One thing that would break in real production, and how you'd fix it

If this comes out cleanly, you ship. If it doesn't, we found a gap.

---

## How we run this

- **One module = one focused session.** Some are 30 min, some are an hour. Module 6 spans three sessions.
- **You drive the pace.** Tell me which module to start, we go.
- **No code from me until Module 9.** That's the mastery rule.
- **Teach-It-Back is non-negotiable.** It's the only signal that the module actually landed.
- **All examples in the banking domain** unless you say otherwise.

---

When you're ready, say "start Module 0" (or any module) and we begin.
