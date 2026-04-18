# SECTION 9 — Advanced Concepts (Evaluation, Multi-Vector, Hybrid Search)

Up to this point, you have built a working understanding of:

* Embeddings
* Similarity
* Vector search
* Semantic retrieval systems

Now we move one level deeper.

This section focuses on **how real-world systems improve quality, scale, and accuracy**.

---

## Why this section matters

A basic system works, but in production:

* Not all embeddings are equally good
* Single-vector representation may lose information
* Pure semantic search may miss exact matches

So we need better techniques.

---

# 9.1 Embedding Evaluation (How good is your model?)

## The problem

You generate embeddings—but how do you know they are good?

> “Good” means: similar things are close, different things are far

---

## Key evaluation idea

We test whether embeddings reflect **true semantic similarity**

---

## Example

Given:

```text id="epq4tn"
Query: "learn AI"
```

Expected results:

* "machine learning tutorial" → relevant
* "pizza recipe" → not relevant

If your model ranks correctly → good embedding

---

## Common evaluation approaches

### 1. Similarity ranking

* Check if relevant items rank higher
* Used in search systems

---

### 2. Clustering quality

* Similar items form clusters
* Different topics are separated

---

### 3. Benchmark datasets

There are standard benchmarks like:

* MTEB (Massive Text Embedding Benchmark)

These evaluate models across:

* Retrieval
* Classification
* Clustering

---

## Practical takeaway

You don’t blindly pick a model.

You evaluate based on:

* Your use case
* Your data

---

# 9.2 Multi-Vector vs Single-Vector Retrieval

## The problem

So far:

```text id="zzg4d2"
One document → One embedding
```

But real documents:

* Have multiple topics
* Contain different sections

One vector may not capture everything.

---

## Example

Document:

> "AI is used in healthcare and finance"

Query:

> "AI in finance"

A single embedding might dilute meaning.

---

## Solution: Multi-vector representation

Instead of:

```text id="gnm7fh"
Document → One vector
```

We do:

```text id="m4r6bp"
Document → multiple chunks → multiple vectors
```

---

## How it works

* Split document into chunks
* Generate embedding for each chunk
* Store all embeddings

During search:

* Match query with all chunks
* Retrieve best matching ones

---

## Why this is powerful

* Better recall
* More precise retrieval
* Works well for RAG systems

---

## LAB — Chunking + Multi-vector search

```python id="ymg7bj"
documents = [
    "AI is transforming healthcare by improving diagnostics",
    "AI is also widely used in finance for fraud detection"
]

# Split into chunks
chunks = []
for doc in documents:
    chunks.extend(doc.split("."))

# Generate embeddings
chunk_embeddings = model.encode(chunks)

# Store in FAISS
import faiss, numpy as np

faiss.normalize_L2(chunk_embeddings)

index = faiss.IndexFlatIP(chunk_embeddings.shape[1])
index.add(np.array(chunk_embeddings))

# Query
query = "AI in finance"
query_emb = model.encode([query])
faiss.normalize_L2(query_emb)

distances, indices = index.search(query_emb, 2)

for i in indices[0]:
    print(chunks[i])
```

---

## Expected output

You should retrieve:

* Finance-related chunk first

---

# 9.3 Hybrid Search (Best of Both Worlds)

## The problem

Pure semantic search has limitations:

* May miss exact keyword matches
* May retrieve loosely related content

Example:

Query:

> "Python list comprehension"

Semantic search might return:

* "Python loops tutorial"
  But miss exact phrase

---

## Solution: Hybrid search

Combine:

```text id="c85r9j"
Keyword search + Vector search
```

---

## How it works

1. Run keyword search (BM25, TF-IDF)
2. Run vector search
3. Combine results

---

## Why this works

* Keyword → precision
* Embedding → meaning

Together:

> Better accuracy

---

## Real-world usage

Almost all production systems use hybrid search:

* Google
* Enterprise search engines
* RAG pipelines

---

## Conceptual pipeline

```text id="tzp2zw"
Query
  ↓
Keyword Search (exact match)
  +
Vector Search (semantic match)
  ↓
Combine & Rank
  ↓
Final Results
```

---

## Practical takeaway

Do not rely only on embeddings.

Best systems combine:

* Symbolic methods (keywords)
* Semantic methods (vectors)

---

# What this section establishes

After this section, you should understand:

* How to evaluate embedding quality
* Why single-vector representation is limited
* How multi-vector (chunking) improves retrieval
* Why hybrid search is used in production systems

---

## Final insight

You are now moving from:

* “Building a working system”

to:

* “Improving system quality and performance”

---


