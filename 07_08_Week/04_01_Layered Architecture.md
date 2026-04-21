## 4.1 Layered Architecture

<img width="1106" height="740" alt="image" src="https://github.com/user-attachments/assets/94a086dd-e03e-4f70-be3e-a1a5cdeb5b19" />

---

### 1) Context

In Section 3, you learned individual components such as LLM, prompts, memory, retrieval, and agents.

However, real-world systems are not built by using these components in isolation. They are organized into layers so that each part of the system has a clear responsibility.

This layered approach helps in:

* scalability
* maintainability
* clear separation of concerns

Without this structure, systems become tightly coupled and difficult to manage.

---

### 2) Concept

A GenAI system can be designed using a layered architecture where each layer performs a specific role.

---

#### Layers and Responsibilities

Input Layer
Handles user interaction. This can be a UI, API, or chat interface where the request enters the system.

Orchestration Layer
This is the control layer. It decides how to process the request. It determines whether to use memory, retrieval, tools, or directly call the LLM.

Memory Layer
Stores past interactions or session context. It enables continuity in conversations.

Data Layer
Contains external knowledge such as documents, embeddings, and vector databases. Used for retrieval.

Model Layer
The LLM processes the input and generates a response. It does reasoning but does not control the system.

Output Layer
Formats and returns the response to the user. This may include formatting, filtering, or structuring the output.

---

#### Flow of Execution

User Input
→ Orchestration Layer
→ Decision making
→ (Optional) Memory Layer
→ (Optional) Data Layer
→ Model Layer (LLM)
→ Output Layer

---

#### Key Understanding

* The orchestration layer is the central decision-maker
* Not every request uses all layers
* The system selects only what is needed

---

#### Example Scenarios

Simple query
User asks: Explain Kubernetes

Flow:
Input → Orchestration → LLM → Output

Conversation query
User asks follow-up question

Flow:
Input → Orchestration → Memory → LLM → Output

Data-driven query
User asks: Why did my pod crash

Flow:
Input → Orchestration → Data retrieval → LLM → Output

---

### 3) Labs

This lab simulates a layered system in a simple way.

---

#### Step 1: Setup

```python
!pip install langchain langchain-openai
```

---

#### Step 2: Basic Layer Simulation

```python
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "your_api_key_here"

llm = ChatOpenAI(temperature=0)

# Input Layer
user_input = "Explain Kubernetes"

# Orchestration Layer (simple decision)
use_memory = False
use_retrieval = False

# Memory Layer (skipped)
# Data Layer (skipped)

# Model Layer
response = llm.invoke(user_input)

# Output Layer
print(response.content)
```

---

#### Step 3: Add Data Layer (Simple Retrieval Simulation)

```python
docs = [
    "Kubernetes manages containers",
    "Pods restart due to memory issues"
]

query = "Why do pods restart"

# Simulate retrieval
context = " ".join(docs)

# Orchestration adds context
final_input = f"Answer using context: {context}"

response = llm.invoke(final_input)

print(response.content)
```

---

### Final Understanding

A layered architecture helps you design AI systems in a structured way.

* Input layer receives the request
* Orchestration layer decides the flow
* Memory and data layers provide context
* LLM performs reasoning
* Output layer returns the result

Most important idea:

You are not interacting with just an LLM
You are interacting with a system built around the LLM

---
