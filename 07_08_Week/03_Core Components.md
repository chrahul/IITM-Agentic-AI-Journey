## SECTION 3: Core Components (Deep Dive)

This section explains the core building blocks of a GenAI system. Each component plays a specific role, and together they form a complete AI system.

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/ff5a119f-30a9-48df-99f8-8f80db5df6f1" />


---

### 3.1 LLM Integration Layer

#### 1) Context

To use an LLM in any application, the first step is integration. Modern LLMs are accessed through APIs, where your application sends input and receives output.

Direct API usage works for simple cases but becomes difficult to manage as systems grow.

#### 2) Concept

LLM integration means connecting your application to a language model.

Basic flow:

User input
→ Application calls LLM API
→ LLM processes input
→ Response returned

Important clarification:

* LLM does not call APIs
* Your system calls the LLM API
* LLM only processes and generates text

LangChain provides a standard interface to interact with LLMs, making it easier to integrate with other components like memory, retrieval, and tools.

Control parameters:

* Temperature controls randomness
* Tokens control input and output size

Cost:

* Depends on tokens and number of API calls
* LangChain does not reduce cost directly

#### 3) Labs

```python
!pip install langchain langchain-openai openai
```

```python
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "your_api_key_here"

llm = ChatOpenAI(temperature=0)

response = llm.invoke("Explain Kubernetes")

print(response.content)
```

---

### 3.2 Prompt Engineering Layer

#### 1) Context

Raw prompts often produce inconsistent results. In real applications, you need predictable and structured outputs.

#### 2) Concept

Prompt engineering is the process of designing instructions for the LLM.

A prompt template is a reusable structure with variables.

Example:

"You are a DevOps expert. Explain {topic} in simple terms."

Key ideas:

* Prompt quality directly impacts output quality
* Templates ensure consistency
* Variables enable reuse

Context injection:

External data can be added to prompts before sending them to the LLM.

Flow:

User input
→ Inject into template
→ Final prompt
→ LLM

#### 3) Labs

```python
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "your_api_key_here"

llm = ChatOpenAI(temperature=0)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="You are a DevOps expert. Explain {topic} in simple terms."
)

final_prompt = prompt.format(topic="Kubernetes")

response = llm.invoke(final_prompt)

print(response.content)
```

---

### 3.3 Chains (Workflow Engine)

#### 1) Context

Many real-world problems require multiple steps. A single LLM call is not enough.

#### 2) Concept

Chains define structured workflows for executing multiple steps.

Example flow:

Input
→ Process
→ Transform
→ Output

Chains help break complex problems into manageable steps.

Types:

* Sequential chains
* Multi-step reasoning workflows

#### 3) Labs

```python
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in one paragraph"
)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("Kubernetes"))
```

---

### 3.4 Memory Systems

#### 1) Context

LLMs do not retain memory between requests. Every call is independent.

#### 2) Concept

Memory systems store and reuse past interactions.

Types:

* Short-term memory: conversation history
* Long-term memory: stored in vector databases

Purpose:

* Maintain context across interactions
* Enable conversational continuity

Important:

Memory is not inside the LLM
It is managed externally by the system

#### 3) Labs

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm, memory=memory)

print(conversation.run("My app runs on Kubernetes"))
print(conversation.run("Why is it slow"))
```

---

### 3.5 Vector Stores (Knowledge Layer)

#### 1) Context

LLMs cannot process large datasets directly. A system is needed to store and retrieve relevant information efficiently.

#### 2) Concept

Vector stores store embeddings of text data for semantic search.

Process:

Text
→ Convert to embedding
→ Store in vector database
→ Retrieve based on similarity

Examples:

* FAISS
* Pinecone
* Chroma

Purpose:

* Enable semantic search
* Retrieve relevant information efficiently

#### 3) Labs

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

texts = [
    "Kubernetes manages containers",
    "Pods restart due to errors"
]

embeddings = OpenAIEmbeddings()

db = Chroma.from_texts(texts, embeddings)

results = db.similarity_search("Why do pods restart")

for r in results:
    print(r.page_content)
```

---

### 3.6 Retrieval (RAG Systems)

#### 1) Context

LLMs may lack specific knowledge or produce incorrect answers. Retrieval improves accuracy by providing real data.

#### 2) Concept

RAG combines retrieval with generation.

Flow:

User query
→ Retrieve relevant documents
→ Add to prompt
→ LLM generates response

Benefits:

* Reduces hallucination
* Improves factual accuracy
* Uses external knowledge

#### 3) Labs

```python
query = "Why do pods restart"

docs = db.similarity_search(query)

context = " ".join([d.page_content for d in docs])

response = llm.invoke(f"Answer using this context: {context}")

print(response.content)
```

---

### 3.7 Agents (Decision Layer)

#### 1) Context

Some tasks require decision-making and action, not just answering questions.

#### 2) Concept

Agents are systems that decide what actions to take.

Capabilities:

* Select tools
* Plan steps
* Execute actions

Flow:

User input
→ Decide next action
→ Call tool or API
→ Process result
→ Respond

Multi-agent systems:

Multiple agents collaborate to solve complex problems.

#### 3) Labs

```python
from langchain.agents import initialize_agent, load_tools
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

tools = load_tools(["llm-math"], llm=llm)

agent = initialize_agent(tools, llm)

response = agent.run("What is 25 * 4")

print(response)
```

---

### Final Understanding of Section 3

A complete AI system is built by combining these components:

* LLM provides reasoning
* Prompts control behavior
* Chains define workflows
* Memory maintains context
* Vector stores manage knowledge
* Retrieval improves accuracy
* Agents enable decision-making

Most important takeaway:

LLM is not the system
It is one component inside a larger system

---

<img width="1440" height="1440" alt="image" src="https://github.com/user-attachments/assets/3017fc0b-f18d-4d50-aa0b-685d5f4ba6d0" />

Read it top to bottom — that is one complete request cycle.

The User asks something. It goes into the Prompt Template which gives it structure. Memory feeds into the prompt too — so the LLM knows what was said before.

The formatted prompt goes to the LLM, which thinks about it. The LLM hands control to the Agent, which decides: can I answer this directly, or do I need a tool? If it needs a tool — calculator, search, API — it calls Tools and gets the result back.

Meanwhile, the Vector Store holds your documents. RAG searches that store, pulls the relevant chunks, and sends them back up to the LLM as enriched context — that is the dashed line going back up the right side.

Finally, the Output goes to the user — and is also saved back into Memory via the dashed line on the left, so the next question remembers this one.

