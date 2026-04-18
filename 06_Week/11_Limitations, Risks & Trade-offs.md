# SECTION 10 — Limitations, Risks & Trade-offs

So far, everything looked powerful: embeddings, vector search, FAISS, semantic retrieval.

Now we look at the **other side**:

> Where do these systems fail?
> Why do they fail?
> How do we detect and fix those failures?

We will follow:

```text
Concept → Problem → Lab → Interpretation
```

---

# 10.1 Limitation 1 — Semantic Drift (Wrong but “similar” results)

## Concept

Embeddings sometimes return results that are:

* Semantically related
* But not actually relevant

This is called **semantic drift**

---

## Problem Example

Query:

```text
"Python list"
```

System may return:

* "Python snake habitat" ❌
* "Python programming loops" ✅

Because:

> “Python” has multiple meanings

---

## LAB — Semantic Drift

```python
documents = [
    "Python is a programming language",
    "Python is a large snake found in forests",
    "List comprehension in Python is powerful",
    "Snakes are reptiles"
]

emb_docs = model.encode(documents)

query = "Python list"
emb_query = model.encode([query])

from sklearn.metrics.pairwise import cosine_similarity
scores = cosine_similarity(emb_query, emb_docs)[0]

for i, s in enumerate(scores):
    print(documents[i], "-->", round(s, 3))
```

<img width="457" height="88" alt="image" src="https://github.com/user-attachments/assets/d01ac216-e06d-48d8-8dbf-1ccf7c302dd7" />



---

## What you may observe

* Snake-related sentence may still get some score
* Not completely filtered out

---

## Why this happens

Embeddings capture:

* General similarity
  Not:
* Exact intent

---

## Fix

* Add keyword filtering
* Use hybrid search

---

# 10.2 Limitation 2 — Loss of Detail (Single Vector Problem)

## Concept

One embedding = compressed meaning

So:

> Fine-grained details may be lost

---

## Problem Example

Document:

```text
"AI is used in healthcare and finance"
```

Query:

```text
"AI in finance"
```

Single embedding → weak match

---

## LAB — Without vs With Chunking

### Without chunking

```python
doc = ["AI is used in healthcare and finance"]
doc_emb = model.encode(doc)

query = "AI in finance"
query_emb = model.encode([query])

score = cosine_similarity(query_emb, doc_emb)[0][0]
print("Without chunking:", score)
```

---

### With chunking

```python
chunks = [
    "AI is used in healthcare",
    "AI is used in finance"
]

chunk_emb = model.encode(chunks)
query_emb = model.encode([query])

scores = cosine_similarity(query_emb, chunk_emb)[0]

for i, s in enumerate(scores):
    print(chunks[i], "-->", round(s, 3))
```

<img width="483" height="527" alt="image" src="https://github.com/user-attachments/assets/f3dd2d36-b2ce-46e7-b3b8-22552b63e67b" />


---

## What you will observe

* Finance chunk → higher score
* Healthcare chunk → lower score

---

## Interpretation

> Chunking preserves detail → better retrieval

---

# 10.3 Limitation 3 — Embedding Model Bias

## Concept

Embeddings inherit bias from training data

---

## Problem Example

Query:

```text
"doctor"
```

Results may lean toward:

* Certain demographics
* Certain assumptions

---

## LAB — Bias Observation

```python
words = ["doctor", "nurse", "engineer", "teacher"]

emb = model.encode(words)

sim = cosine_similarity(emb)

print(sim)
```

---

## What to observe

* Some professions may appear closer than expected
* Hidden patterns exist

---

## Interpretation

> Embeddings reflect patterns from data, not objective truth

---

## Fix

* Use better datasets
* Fine-tune models
* Add fairness checks

---

# 10.4 Limitation 4 — Approximate Search Trade-off

## Concept

FAISS often uses **approximate search**

Trade-off:

```text
Speed ↑ → Accuracy ↓
```

---

## LAB — Exact vs Approximate

### Exact

```python
index_exact = faiss.IndexFlatIP(doc_embeddings.shape[1])
index_exact.add(doc_embeddings)
```

---

### Approximate

```python
quantizer = faiss.IndexFlatIP(doc_embeddings.shape[1])
index_ivf = faiss.IndexIVFFlat(quantizer, doc_embeddings.shape[1], 2)

index_ivf.train(doc_embeddings)
index_ivf.add(doc_embeddings)
index_ivf.nprobe = 1
```

---

### Compare results

```python
dist1, ind1 = index_exact.search(query_embedding, 3)
dist2, ind2 = index_ivf.search(query_embedding, 3)

print("Exact:", ind1)
print("Approx:", ind2)
```

---

## What you may observe

* Slight difference in ranking

---

## Interpretation

> Faster search may slightly reduce accuracy

---

# 10.5 Limitation 5 — No Understanding, Only Similarity

## Concept

Embeddings do NOT “understand” like humans

They only:

> Measure similarity

---

## Problem Example

Query:

```text
"Is AI dangerous?"
```

Search may return:

* “AI benefits”
* “AI applications”

Not necessarily:

* “AI risks”

---

## LAB — Try it

```python
documents = [
    "AI improves productivity",
    "AI is used in automation",
    "Risks of artificial intelligence",
    "Benefits of machine learning"
]

emb_docs = model.encode(documents)
query = "Is AI dangerous?"

emb_query = model.encode([query])

scores = cosine_similarity(emb_query, emb_docs)[0]

for i, s in enumerate(scores):
    print(documents[i], "-->", round(s, 3))
```

---

## What you may observe

* “Benefits” may score high
* “Risks” may not always be top

---

## Interpretation

> Embeddings don’t reason—they match patterns

---

# Final Summary

## What you learned in this section

* Embeddings are powerful but imperfect
* They can drift, lose detail, and carry bias
* Speed vs accuracy trade-offs exist
* They do similarity—not true reasoning

---

## System thinking (very important)

Real-world systems solve these using:

```text
Embeddings
+ Chunking
+ Hybrid search
+ Re-ranking
+ Evaluation
```

---

## Final Insight

You have now reached a level where you understand:

* Not just how to build systems
* But also how they fail and how to improve them

---

This completes the core of Week 6.

