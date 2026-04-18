# SECTION 8 — Visualising Embeddings (PCA & t-SNE)

So far, you have understood:

* Text → embeddings
* Embeddings → vectors in high-dimensional space
* Similarity → distance / angle

But there is one challenge:

> We cannot “see” high-dimensional space

If embeddings are 384 or 768 dimensions, how do we understand their structure?

This is where **dimensionality reduction** comes in.

---

## Why visualization is needed

Embeddings contain structure:

* Similar items cluster together
* Different concepts form separate groups

But this structure is hidden in high dimensions.

Visualization helps us:

* See clusters
* Validate model behavior
* Debug embeddings
* Build intuition

---

## The core idea

We take:

```text
High-dimensional vectors (384D, 768D)
```

And convert them into:

```text
2D or 3D representation (for plotting)
```

While trying to preserve relationships.

---

## Two main techniques

* PCA (Principal Component Analysis)
* t-SNE (t-Distributed Stochastic Neighbor Embedding)

---

# 8.1 PCA (Principal Component Analysis)

## What PCA does

PCA reduces dimensions by:

> Preserving maximum variance (global structure)

It finds the directions where data varies the most and projects onto them.

---

## Intuition

Imagine:

* Data spread in many dimensions
* PCA finds the “main axes” where most information lies

---

## Characteristics

* Fast
* Linear method
* Preserves global structure
* Good for initial exploration

---

# LAB 1 — PCA Visualization

## Step 1 — Setup

```python
!pip install sentence-transformers matplotlib scikit-learn
```

---

## Step 2 — Code

```python
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "I love AI",
    "Machine learning is amazing",
    "Deep learning is powerful",
    "I enjoy pizza",
    "Pizza tastes great",
    "I like food"
]

embeddings = model.encode(sentences)
```

---

## Step 3 — Reduce to 2D

```python
pca = PCA(n_components=2)
reduced = pca.fit_transform(embeddings)
```

---

## Step 4 — Plot

```python
plt.figure(figsize=(8,6))

for i, sentence in enumerate(sentences):
    x, y = reduced[i]
    plt.scatter(x, y)
    plt.text(x+0.01, y+0.01, sentence)

plt.title("PCA Visualization of Embeddings")
plt.show()
```

---

## What you will observe

* AI-related sentences close together
* Food-related sentences close together

---

## Limitation of PCA

PCA may not clearly separate clusters if structure is complex.



<img width="880" height="531" alt="image" src="https://github.com/user-attachments/assets/ba86a087-b667-401a-b405-0dda8c030595" />


---

# 8.2 t-SNE (t-Distributed Stochastic Neighbor Embedding)

## What t-SNE does

t-SNE focuses on:

> Preserving local relationships (neighbors)

---

## Intuition

* Points that are close in high dimension → stay close
* Far points → may not preserve exact distances

---

## Characteristics

* Excellent for clustering
* Non-linear
* Slower than PCA
* Better visualization quality

---

# LAB 2 — t-SNE Visualization

## Step 1 — Code

```python
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, perplexity=2, random_state=42)
reduced_tsne = tsne.fit_transform(embeddings)
```

---

## Step 2 — Plot

```python
plt.figure(figsize=(8,6))

for i, sentence in enumerate(sentences):
    x, y = reduced_tsne[i]
    plt.scatter(x, y)
    plt.text(x+0.01, y+0.01, sentence)

plt.title("t-SNE Visualization of Embeddings")
plt.show()
```

---

<img width="868" height="546" alt="image" src="https://github.com/user-attachments/assets/2ab088c0-6346-4525-8b91-bdf607926e68" />


## What you will observe

* Much clearer clusters
* AI group vs Food group distinctly separated

---

# PCA vs t-SNE (Clear Comparison)

| Feature               | PCA              | t-SNE          |
| --------------------- | ---------------- | -------------- |
| Type                  | Linear           | Non-linear     |
| Focus                 | Global structure | Local clusters |
| Speed                 | Fast             | Slower         |
| Visualization quality | Moderate         | High           |

---

## When to use what

* PCA → quick overview, preprocessing
* t-SNE → deep visualization, cluster analysis

---

## Important caution

Visualization is for **intuition**, not exact truth.

* Distances may be distorted
* Especially in t-SNE

So:

> Use it to understand patterns, not to make strict conclusions

---

## What this section establishes

After this section, you should understand:

* Why embeddings cannot be visualized directly
* How PCA and t-SNE help reduce dimensions
* How semantic clusters appear visually
* Difference between global vs local structure

---

## Final insight

You are now able to:

* Generate embeddings
* Compare them
* Search using them
* Visualize them

This is a complete foundational understanding.

---

Next:

**Section 9 — Advanced Concepts (Evaluation, Multi-vector, Hybrid Search)**
