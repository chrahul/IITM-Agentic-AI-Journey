# SECTION 9 — Deep Dive (Practical Problems + Solutions + Labs)

We will structure this as:

```text
Problem → Why it happens → Solution → Code
```

---

# 9.1 Problem 1 — “My search results are not relevant”

## Scenario

You built a semantic search (like Section 7), but results are:

* Slightly related
* Sometimes irrelevant
* Not ranked properly

---

## Why this happens

* Embedding model may not match your domain
* Generic models don’t understand domain-specific language

Example:

* “margin call” in finance vs general English

---

## Solution — Better Embedding Model

### Option 1 — Try different models

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "How to learn machine learning",
    "Deep learning fundamentals",
    "Introduction to artificial intelligence",
    "Best pizza places in New York",
    "Top restaurants for food lovers",
    "Neural networks explained",
    "AI for beginners"
]

models = [
    'all-MiniLM-L6-v2',
    'all-mpnet-base-v2'
]

query = "I want to learn AI"

for m in models:
    model = SentenceTransformer(m)
    
    emb_docs = model.encode(documents)
    emb_query = model.encode([query])
    
    scores = cosine_similarity(emb_query, emb_docs)[0]
    
    print(f"\nModel: {m}")
    for i, s in enumerate(scores):
        print(documents[i], "-->", round(s, 3))
```

<img width="430" height="166" alt="image" src="https://github.com/user-attachments/assets/b1f703e4-0384-4ef0-aaf5-6c19d9ebcecc" />



## Explanation


---

# What was the purpose of this lab?

We were trying to prove:

> **Different embedding models produce different similarity scores → which affects search quality**

---

# Step 1 — What stayed the same?

* Same **documents**
* Same **query**
* Same **similarity function (cosine)**

Only thing changed:

```text
Embedding model
```

---

# Step 2 — What did you observe?

Let’s focus only on top results.

## Model 1: all-MiniLM-L6-v2

```text
AI for beginners → 0.813
How to learn machine learning → 0.583
Introduction to artificial intelligence → 0.55
```

---

## Model 2: all-mpnet-base-v2

```text
AI for beginners → 0.753
How to learn machine learning → 0.538
Introduction to artificial intelligence → 0.417
```

---

# Step 3 — What is the key difference?

At first glance:

> “Both look similar”

Correct — but look deeper.

---

## Insight 1 — Score distribution changes

* MiniLM → higher scores overall
* MPNet → more conservative scores

This means:

> Different models have different “confidence calibration”

---

## Insight 2 — Relative importance shifts

Look at:

```text
Neural networks explained
MiniLM → 0.404
MPNet → 0.307
```

MPNet is more strict in saying:

> “This is less relevant”

---

## Insight 3 — Noise handling

Look at irrelevant docs:

```text
Pizza doc:
MiniLM → 0.009
MPNet → 0.011
```

Both reject correctly, but:

> Better models usually separate relevant vs irrelevant more cleanly at scale

---

# Step 4 — What are we actually proving?

This lab is NOT about:

> “Which model gives higher number”

It is about:

> “Which model ranks results better for your use case”

---

# Step 5 — Real-world interpretation

Imagine:

You build a system for:

* Legal documents
* Finance
* DevOps logs

Now:

* Generic model → average results
* Better model → domain-aligned results

---

# Step 6 — The real takeaway (very important)

The core learning is:

> Embedding model = brain of your search system

Everything depends on it:

* What is “similar”
* What is “relevant”
* What gets retrieved

---

# Step 7 — Why your output looks similar

Because:

* Your dataset is very small
* Documents are simple
* Both models are good

So difference is subtle.

---

# Step 8 — When difference becomes obvious

You’ll see real impact when:

* Large dataset
* Complex queries
* Domain-specific language

Example:

* Medical
* Legal
* Financial

---

# Step 9 — conclusion


> This experiment demonstrates that different embedding models produce different similarity scores and ranking behavior. While both models correctly identify relevant documents, their scoring patterns and sensitivity to semantic relationships vary. In real-world systems, selecting the right embedding model is critical for retrieval quality.

---

# Final clarity

This lab was NOT about:

* Getting different answers

It was about understanding:

> The **model you choose defines your system’s intelligence**

---
---

### Option 2 — Compare models (practical lab)

```python
models = [
    'all-MiniLM-L6-v2',
    'all-mpnet-base-v2'
]

query = "I want to learn AI"

for m in models:
    model = SentenceTransformer(m)
    
    emb_docs = model.encode(documents)
    emb_query = model.encode([query])
    
    from sklearn.metrics.pairwise import cosine_similarity
    scores = cosine_similarity(emb_query, emb_docs)[0]
    
    print(f"\nModel: {m}")
    for i, s in enumerate(scores):
        print(documents[i], "-->", round(s, 3))
```


This example demonstrates that representing documents as multiple smaller chunks (multi-vector approach) significantly improves retrieval accuracy. Instead of a single diluted representation, each chunk captures a focused meaning, allowing the system to retrieve the most relevant portion of the document for a given query.


---

## Learning

> Embedding model choice directly affects search quality

---

# 9.2 Problem 2 — “Large document not retrieved correctly”

## Scenario

Document:

```text
"AI is used in healthcare... AI is used in finance..."
```

Query:

```text
"AI in finance"
```

But system fails to retrieve correct part.

---

## Why this happens

* Whole document → one embedding
* Mixed topics → diluted meaning

---

## Solution — Chunking (Multi-vector approach)

---

## LAB — Chunking Implementation

```python
documents = [
    "AI is transforming healthcare by improving diagnostics. AI is also used in finance for fraud detection."
]

# Step 1: Split into chunks
chunks = documents[0].split(".")

chunks = [c.strip() for c in chunks if c.strip()]

print(chunks)
```

---

### Generate embeddings

```python
chunk_embeddings = model.encode(chunks)
```

---

### Store in FAISS

```python
import faiss
import numpy as np

faiss.normalize_L2(chunk_embeddings)

index = faiss.IndexFlatIP(chunk_embeddings.shape[1])
index.add(np.array(chunk_embeddings))
```

---

### Query

```python
query = "AI in finance"

query_emb = model.encode([query])
faiss.normalize_L2(query_emb)

distances, indices = index.search(query_emb, 2)

for i in indices[0]:
    print(chunks[i])
```

---

## Learning

> Smaller chunks → better semantic precision

---

# 9.3 Problem 3 — “Semantic search misses exact matches”

## Scenario

Query:

```text
"Python list comprehension"
```

Semantic search returns:

* “Python loops tutorial”

But misses:

* Exact phrase match

---

## Why this happens

* Embeddings focus on meaning
* Not exact keyword presence

---

## Solution — Hybrid Search

---

## LAB — Hybrid Search (Simple Version)

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Keyword search
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

query = "Python list comprehension"
tfidf_query = vectorizer.transform([query])

keyword_scores = cosine_similarity(tfidf_query, tfidf_matrix)[0]

# Semantic search
emb_docs = model.encode(documents)
emb_query = model.encode([query])

semantic_scores = cosine_similarity(emb_query, emb_docs)[0]
```

---

### Combine scores

```python
final_scores = 0.5 * keyword_scores + 0.5 * semantic_scores

for i, score in enumerate(final_scores):
    print(documents[i], "-->", round(score, 3))
```

---

## Learning

> Hybrid = precision (keyword) + meaning (semantic)

---

# 9.4 Problem 4 — “Search is too slow at scale”

## Scenario

* Millions of embeddings
* Query takes too long

---

## Why this happens

* Brute-force comparison

---

## Solution — Approximate Nearest Neighbor (ANN)

You already used FAISS, but let’s upgrade it.

---

## LAB — Faster Index (IVF)

```python
dimension = doc_embeddings.shape[1]

nlist = 2  # number of clusters
quantizer = faiss.IndexFlatIP(dimension)

index = faiss.IndexIVFFlat(quantizer, dimension, nlist)

index.train(doc_embeddings)
index.add(doc_embeddings)

index.nprobe = 1  # search clusters
```

---

### Query same as before

```python
distances, indices = index.search(query_embedding, 3)
```

---

## Learning

> ANN = faster search with slight approximation

---

# 9.5 Problem 5 — “Top results are not perfectly ranked”

## Scenario

Top results are relevant but not in perfect order.

---

## Why this happens

* Embeddings give rough similarity
* Not perfect ranking

---

## Solution — Re-ranking (Advanced)

---

## LAB — Simple Re-ranking

```python
top_k = 3

distances, indices = index.search(query_embedding, top_k)

candidates = [documents[i] for i in indices[0]]

# Re-rank using cosine again (or better model)
scores = cosine_similarity(
    model.encode([query]),
    model.encode(candidates)
)[0]

sorted_results = sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)

for doc, score in sorted_results:
    print(doc, "-->", round(score, 3))
```

---

## Learning

> First retrieve → then refine ranking

---

# Final Deep Insight

Now you should see the progression:

```text
Basic System
   ↓
Better Model
   ↓
Chunking (multi-vector)
   ↓
Hybrid Search
   ↓
ANN Index
   ↓
Re-ranking
```

---

# What you have now achieved

You are no longer just learning:

* Embeddings
* Vector search

You are understanding:

> How real-world AI systems are engineered and improved

---

If this is clear, next:

**Section 10 — Limitations, Risks & Trade-offs**
