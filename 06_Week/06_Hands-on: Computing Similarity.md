
# SECTION 5 — Hands-on: Computing Similarity

This section will not introduce new theory.
Instead, it will **reinforce everything you learned in Section 2 and 4 through code**.

We will do this step-by-step:

1. Generate embeddings
2. Compute cosine similarity
3. Compare with Euclidean distance
4. Build a mini real-world use case

---

# LAB 1 — Cosine Similarity (Deep Understanding)

## Goal

Understand how similarity behaves with real sentences

---

### Step 1 — Setup

```python
!pip install sentence-transformers scikit-learn
```

---

### Step 2 — Code

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "I love machine learning",
    "I enjoy artificial intelligence",
    "Machine learning is amazing",
    "The weather is very hot today"
]

embeddings = model.encode(sentences)

sim_matrix = cosine_similarity(embeddings)

print(sim_matrix)
```

---

### What to observe

* Sentence 0,1,2 → high similarity cluster
* Sentence 3 → isolated

---

### Key learning

You are not matching words—you are comparing **meaning**

---

# LAB 2 — Cosine vs Euclidean (Very Important)

## Goal

See the difference between two metrics

---

### Code

```python
from sklearn.metrics.pairwise import euclidean_distances

cos_sim = cosine_similarity(embeddings)
euc_dist = euclidean_distances(embeddings)

print("Cosine Similarity:\n", cos_sim)
print("\nEuclidean Distance:\n", euc_dist)
```

---

### What to observe

* Cosine → higher = more similar
* Euclidean → lower = more similar

---

### Insight

Two sentences may:

* Have similar direction → high cosine
* But different magnitude → higher Euclidean

This is why cosine is preferred.

---

# LAB 3 — Ranking Based on Similarity (Core Concept)

## Goal

Understand how systems rank results

---

### Code

```python
query = "I want to learn AI"

query_embedding = model.encode([query])

scores = cosine_similarity(query_embedding, embeddings)[0]

for i, score in enumerate(scores):
    print(f"{sentences[i]} --> {score:.3f}")
```

---

### Expected behavior

Top matches:

* AI / ML sentences

Lowest:

* Weather sentence

---

### Key learning

This is exactly how:

* Search engines
* RAG systems
* Chatbots

retrieve relevant data

---

# LAB 4 — Threshold-Based Filtering

## Goal

Understand practical decision making

---

### Code

```python
threshold = 0.5

for i, score in enumerate(scores):
    if score > threshold:
        print(f"Relevant: {sentences[i]} ({score:.2f})")
```

---

### Insight

In real systems:

* You don’t take all results
* You filter based on similarity

---

# LAB 5 — Real Use Case: Duplicate Detection

## Goal

Detect similar sentences

---

### Code

```python
pairs = [
    ("I love AI", "I enjoy artificial intelligence"),
    ("I like pizza", "The weather is hot"),
]

for s1, s2 in pairs:
    emb1 = model.encode([s1])
    emb2 = model.encode([s2])
    
    score = cosine_similarity(emb1, emb2)[0][0]
    
    print(f"{s1} | {s2} --> {score:.2f}")
```

---

### Expected output

* First pair → high similarity
* Second pair → low similarity

---

### Real-world usage

* Duplicate question detection
* Resume matching
* FAQ systems

---

# What you should feel after this section

After running these labs, the following should become intuitive:

* Similarity is not abstract—it is measurable
* Cosine similarity reflects semantic closeness
* Euclidean distance behaves differently
* Ranking = sorting by similarity
* Threshold = filtering relevance

---

# One final connection (important)

Everything you just did is exactly what happens in:

* Semantic search
* RAG pipelines
* AI agents memory retrieval

Just at a larger scale.

---

Next step:

**Section 6 — Vector Search: The Real Power Layer**
