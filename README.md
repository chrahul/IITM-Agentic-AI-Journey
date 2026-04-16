

# GitHub Repo Structure )

## Repo Philosophy

This is NOT:

> “notes repo”

This is:

> “AI Systems Learning + Implementation Repository”

Each week follows:

```
Context → Concept → Intuition → System → Lab → Reflection
```

---

#  ROOT STRUCTURE

```bash
IITM-Agentic-AI-Journey/
│
├── README.md
├── 00_Foundations/
├── 01_Python_Refresher/
├── 02_AI_ML_Basics/
├── 03_LLM_Fundamentals/
├── 04_Prompt_Engineering/
├── 05_LangChain_Intro/
├── 06_Embeddings_Vector_Search/   👈 (Current Week)
├── 07_Agents_Tools/
├── 08_Agent_Architecture/
├── 09_Memory_RAG/
├── 10_Advanced_RAG/
├── 11_Evaluation_Observability/
├── 12_Ethics_Governance/
├── 13_Capstone_Project/
│
├── assets/          # images, diagrams
├── utils/           # reusable code
├── requirements.txt
└── LICENSE
```

---

#  WEEK-WISE STRUCTURE (STANDARD TEMPLATE)

Every week folder (like Week 6) will follow SAME structure:

```bash
06_Embeddings_Vector_Search/
│
├── README.md                # Week Overview
│
├── 01_Context/
│   └── overview.md
│
├── 02_Concepts/
│   ├── embeddings.md
│   ├── similarity.md
│   ├── vector_search.md
│   └── visualization.md
│
├── 03_Intuition/
│   └── analogies.md
│
├── 04_System_Design/
│   └── architecture.md
│
├── 05_Labs/
│   ├── lab1_embeddings.ipynb
│   ├── lab2_similarity.py
│   ├── lab3_vector_search_faiss.py
│   └── lab4_visualization.ipynb
│
├── 06_Mini_Project/
│   ├── semantic_search_engine.py
│   └── README.md
│
├── 07_Reflections/
│   └── learnings.md
│
└── assets/
    ├── diagrams.png
    └── outputs.png
```

---

# HOW EACH FOLDER SHOULD BE WRITTEN

##  Context (overview.md)

Explain in **your own words**:

* What this week is about
* Why it matters
* Where it fits in GenAI

---

##  Concepts

Each file = one topic

Example:

### `embeddings.md`

* Definition
* Mathematical intuition
* Example
* Real-world usage
* 
---

## System Design

Example (Week 6):

```id="zqevvy"
User Query → Embedding → Vector DB → Similarity → Top Results
```

Explain like:

* Architect
* Not student

---

## Labs

VERY IMPORTANT

Each lab should:

* Solve one concept
* Be clean
* Be reproducible

---

## Mini Project

For Week 6:

 **Semantic Search Engine**

Features:

* Input query
* Convert to embedding
* Search top K results

---

## Reflection

This is what makes your repo **elite**

Write:

* What clicked
* What was confusing
* Where this is used in real world

---
