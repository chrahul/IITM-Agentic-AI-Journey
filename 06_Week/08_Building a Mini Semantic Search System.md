# SECTION 7 — Building a Mini Semantic Search System (End-to-End)

In Section 6, you implemented vector search.
Now we bring everything together into a **clean, structured system**.

The goal here is not just code—it is to think like a **system designer**.

---

## Problem Statement

Build a system where:

* User enters a query
* System understands meaning (not keywords)
* Returns most relevant documents

---

## System Architecture

```id="d03q2c"
User Query
   ↓
Embedding Model
   ↓
Vector Representation
   ↓
Vector Index (FAISS)
   ↓
Similarity Search
   ↓
Top-K Results
```

---

## Design Principles

* Clear separation of steps
* Reusable components
* Readable and maintainable code

---

# Implementation

We will structure this like a real project.

---

## Step 1 — Install dependencies

```python id="czj0qs"
!pip install sentence-transformers faiss-cpu
```

---

## Step 2 — Initialize system

```python id="wry4jg"
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
```

---

## Step 3 — Create document store

```python id="zgwzui"
documents = [
    "How to learn machine learning",
    "Deep learning fundamentals",
    "Introduction to artificial intelligence",
    "Best pizza places in New York",
    "Top restaurants for food lovers",
    "Neural networks explained",
    "AI for beginners"
]
```

---

## Step 4 — Convert documents to embeddings

```python id="hsyoij"
doc_embeddings = model.encode(documents)
doc_embeddings = np.array(doc_embeddings)
```

---

## Step 5 — Normalize (important for cosine similarity)

```python id="ztl8gb"
faiss.normalize_L2(doc_embeddings)
```

---

## Step 6 — Create FAISS index

```python id="aytvt9"
dimension = doc_embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)  # inner product ≈ cosine similarity
index.add(doc_embeddings)
```

---

## Step 7 — Build search function

This is the core reusable component.

```python id="azqg0g"
def search(query, k=3):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding)
    
    faiss.normalize_L2(query_embedding)
    
    distances, indices = index.search(query_embedding, k)
    
    results = []
    for i, idx in enumerate(indices[0]):
        results.append({
            "document": documents[idx],
            "score": float(distances[0][i])
        })
    
    return results
```

---

## Step 8 — Test the system

```python id="n2ls6t"
query = "I want to learn AI"

results = search(query)

for r in results:
    print(r)
```

---

## Expected Output

```id="2fqzci"
{'document': 'AI for beginners', 'score': 0.82}
{'document': 'Introduction to artificial intelligence', 'score': 0.80}
{'document': 'Neural networks explained', 'score': 0.75}
```

---

# What you built

You now have a system with:

* Embedding generation
* Vector storage
* Similarity-based retrieval
* Ranking

This is a complete **semantic search engine (basic version)**

---

## Key Observations

### 1. No keyword dependency

Query:

> "learn AI"

Still retrieves:

* "AI for beginners"
* "Introduction to artificial intelligence"

---

### 2. Ranking is meaningful

Higher score → more relevant

---

### 3. System is extensible

You can easily:

* Add more documents
* Change model
* Store data externally

---

## Improvements (Next Level Thinking)

To make this production-ready:

* Store embeddings in a vector database (FAISS/Pinecone/Chroma)
* Add metadata filtering
* Use chunking for large documents
* Add re-ranking with LLM

---

## Real-world mapping

This exact pipeline is used in:

* RAG systems
* ChatGPT plugins
* Enterprise document search
* AI assistants

---

## Final Understanding

What you built is not just a lab.

It is:

> A foundational component of modern AI systems

---

## What this section establishes

After this section, you can:

* Design a semantic search system
* Implement vector-based retrieval
* Understand how embeddings + similarity + indexing work together

---


---

## EXTRA

### 1. Semantic Search vs Keyword Search

* Not matching exact words
* Understanding **intent and context**
* “Apple (fruit)” vs “Apple (company)”

Correct.

---

### 2. Embeddings as Numerical Representation

* Text → vector
* Meaning preserved in numbers
* Similar concepts → similar vectors

Correct.

---

### 3. Context changes embedding

* Apple (fruit) vs Apple (company) → different vectors

Correct.

---

### 4. Need for storage + retrieval

* Many embeddings → need database
* Query → embedding → compare

Correct.

---

### 5. Scalability problem

* Linear search = too slow for millions of vectors

Correct.

---

### 6. Indexing idea

* Group similar vectors
* Search only relevant subset

Correct.

---


##  1. “Features like revenue, location, phones”

You said:

> embedding = handcrafted features like revenue, location

This is good for intuition, but in reality:

> Embeddings are **NOT manually defined features**

Instead:

* Learned automatically from massive data
* Using neural networks (Word2Vec, BERT, etc.)

So:

| Intuition              | Reality                  |
| ---------------------- | ------------------------ |
| Human-defined features | Learned representations  |
| Explainable            | Mostly not interpretable |

---

##  2. Vector Database vs Normal Database

You said:

> store embeddings in SQL database

Technically possible, but not ideal.

### Key difference:

| Traditional DB          | Vector DB                     |
| ----------------------- | ----------------------------- |
| Exact match / filtering | Similarity search             |
| Indexed on columns      | Indexed on vectors            |
| B-tree / hash index     | ANN (Approx Nearest Neighbor) |

---

##  3. Core definition (very important)

Let’s make it precise:

> A **vector database** is a system designed to store embeddings and perform efficient similarity search using specialized indexing techniques.

---

##  4. About Hashing (LSH)

You mentioned:

> hashing → buckets → faster search

Correct, but that is just **one technique**.

Modern systems use:

* HNSW (Hierarchical Navigable Small World graphs) → most common
* IVF (Inverted File Index)
* PQ (Product Quantization)
* LSH (older approach)

So don’t lock thinking to only hashing.

---

##  5. FAISS in your lab

What you used:

```python
IndexFlatL2
```

This is actually:

* **Brute-force search (no index optimization)**

FAISS also supports:

* Approximate search (fast)
* Graph-based search

---

# Clean Final Understanding 



---

## Vector Search & Vector Database — Refined Understanding

When building modern AI systems, text is first converted into embeddings, which are dense vector representations capturing semantic meaning.

These embeddings allow us to compare data based on meaning rather than exact keyword matching. This enables semantic search, where queries like “calories in apple” and “employees in Apple” are correctly interpreted using context.

However, real-world systems contain millions or billions of such embeddings. Performing similarity comparison using linear search is computationally expensive and not scalable.

To solve this, vector databases are used.

A vector database is a specialized system designed to:

* Store high-dimensional embeddings efficiently
* Perform fast similarity search using approximate nearest neighbor (ANN) algorithms

Instead of scanning all vectors, these systems use indexing techniques (such as HNSW, IVF, etc.) to narrow down the search space and retrieve the most similar vectors quickly.

The overall flow becomes:

```text
Query → Embedding → Vector Index → Nearest Neighbor Search → Results
```

This architecture forms the backbone of:

* Semantic search
* Retrieval-Augmented Generation (RAG)
* Recommendation systems
* AI agents with memory

---

# Final feedback on your understanding

You are already thinking like:

* Not a beginner
* Not just a coder

But:

> Someone trying to understand systems end-to-end

That is exactly what this course requires.

---

If this is clear, next section:

**Section 8 — Visualising Embeddings (PCA & t-SNE)**


