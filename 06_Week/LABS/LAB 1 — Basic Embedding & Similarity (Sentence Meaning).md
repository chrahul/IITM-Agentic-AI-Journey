

# LAB 1 — Basic Embedding & Similarity (Sentence Meaning)

## Goal

See how similar sentences are **close in vector space**

---

### Step 1 — Install library

```python
!pip install sentence-transformers
```

---

### Step 2 — Generate embeddings

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "I love machine learning",
    "I enjoy artificial intelligence",
    "The weather is very hot today"
]

embeddings = model.encode(sentences)

print("Embedding shape:", embeddings.shape)
```

---

### Step 3 — Compare similarity

```python
sim_matrix = cosine_similarity(embeddings)

print(sim_matrix)
```

---

### What you will observe

* Sentence 1 and 2 → high similarity
* Sentence 3 → low similarity

### Interpretation

Even though:

* “love” ≠ “enjoy”
* “machine learning” ≠ “AI”

Model understands:

> These sentences are semantically similar

---

# LAB 2 — Word Meaning vs Context (Bank Example)

## Goal

See how **same word behaves differently based on sentence**

---

```python
sentences = [
    "I deposited money in the bank",
    "The river bank was beautiful",
    "She works at a financial bank",
    "We sat near the river"
]

embeddings = model.encode(sentences)

sim_matrix = cosine_similarity(embeddings)

for i in range(len(sentences)):
    for j in range(len(sentences)):
        print(f"{i}-{j}: {sim_matrix[i][j]:.2f}")
```

---

### What you will observe

* Sentence 1 ↔ Sentence 3 → high similarity (financial context)
* Sentence 2 ↔ Sentence 4 → high similarity (river context)
* Cross comparison → lower similarity

---

### Key Insight

> The word “bank” does NOT have one meaning
> The **sentence embedding captures context**

This is what you explained—and now you will see it numerically.

---

# LAB 3 — Visualizing Embeddings (Make It Visible)

## Goal

See how similar sentences cluster together

---

### Step 1

```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

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

### Step 2 — Reduce dimensions

```python
pca = PCA(n_components=2)
reduced = pca.fit_transform(embeddings)
```

---

### Step 3 — Plot

```python
plt.figure(figsize=(8,6))

for i, sentence in enumerate(sentences):
    x, y = reduced[i]
    plt.scatter(x, y)
    plt.text(x+0.01, y+0.01, sentence)

plt.title("Embedding Visualization")
plt.show()
```

---

### What you will observe

* AI-related sentences cluster together
* Food-related sentences cluster together

---

### Key Insight

> Meaning becomes **clusters in space**

You are literally seeing semantics.

---

# LAB 4 — Semantic Search (Mini Real System)

## Goal

Simulate how search works using embeddings

---

### Step 1 — Data

```python
documents = [
    "How to learn machine learning",
    "Best pizza places in New York",
    "Introduction to deep learning",
    "Top restaurants for food lovers",
    "AI and neural networks basics"
]

doc_embeddings = model.encode(documents)
```

---

### Step 2 — Query

```python
query = "I want to study AI"
query_embedding = model.encode([query])
```

---

### Step 3 — Search

```python
similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

for i, score in enumerate(similarities):
    print(f"{documents[i]} --> {score:.2f}")
```

---

### What you will observe

Top matches:

* AI / ML / Deep Learning related docs

Not matched:

* Pizza / food

---

### Key Insight

> No keyword matching
> Pure meaning-based retrieval

---

# What You Just Achieved

After these labs, you should clearly see:

* Text → vectors
* Meaning → distance
* Context → changes embedding
* Similarity → measurable
* Search → based on vectors

---

# One Important Mental Shift (Final Reinforcement)

Do not think:

> “Embedding = numbers”

Think:

> “Embedding = coordinates in meaning space”

---

# Explanation

## Step 1 — What is `sentence-transformers`?

When you run:

```python
!pip install sentence-transformers
```

You are installing a **Python library (package)**.

* `sentence-transformers` (with `-`) is the **package name** used by pip
* It is a library built on top of transformer models (like BERT)

This library gives you ready-to-use tools to generate **sentence embeddings**

---

## Step 2 — Why `sentence-transformers` vs `sentence_transformers`?

This is where confusion happens.

### Important rule in Python:

* Package name (pip) → can use `-`
* Module name (import in code) → uses `_`

So:

| Usage   | Name                    |
| ------- | ----------------------- |
| Install | `sentence-transformers` |
| Import  | `sentence_transformers` |

---

## Step 3 — What does this line mean?

```python
from sentence_transformers import SentenceTransformer
```

Let’s break it:

### Part 1:

```python
from sentence_transformers
```

You are saying:

> “Go to the module (library) named `sentence_transformers`”

---

### Part 2:

```python
import SentenceTransformer
```

Inside that library, there are many things.

You are importing **one specific class** called:

> `SentenceTransformer`

---

## Step 4 — What is `SentenceTransformer`?

It is a **class (blueprint)**.

Think of it like:

* A ready-made tool
* That knows how to convert text → embeddings

---

## Step 5 — How you use it

```python
model = SentenceTransformer('all-MiniLM-L6-v2')
```

Here:

* `SentenceTransformer(...)` → creates an object (model)
* `'all-MiniLM-L6-v2'` → name of a **pretrained model**

So effectively:

> “Load a pretrained embedding model”

---

## Step 6 — What happens internally

When you do:

```python
model.encode("I love AI")
```

Behind the scenes:

1. Text is tokenized
2. Passed through a transformer model (like BERT variant)
3. Output is converted into a vector

You don’t see this complexity because the library abstracts it.

---

## Step 7 — About “different types of transformers”

You are correct.

There are many transformer-based models:

* BERT → general language understanding
* GPT → text generation
* Sentence-BERT → optimized for similarity and embeddings

This library (`sentence-transformers`) specifically focuses on:

> Models designed for **embedding and similarity tasks**

---

## Final simplified understanding

You can think of this line as:

> “From the sentence embedding library, import the tool that converts sentences into vectors”

---

## One small analogy

* `sentence_transformers` → toolbox
* `SentenceTransformer` → a specific tool inside the toolbox
* `model = SentenceTransformer(...)` → picking and preparing that tool
* `model.encode(text)` → using the tool


Yes — that understanding is correct. Let’s refine it slightly so it’s precise.

---

## What is `"all-MiniLM-L6-v2"`?

It is the **name of a pretrained sentence embedding model**, originally hosted on Hugging Face.

When you write:

```python
model = SentenceTransformer('all-MiniLM-L6-v2')
```

you are telling the library:

> “Download (if needed) and load this specific pretrained embedding model”

---

## What kind of model is it?

`all-MiniLM-L6-v2` is:

* A **Sentence-BERT style model**
* Built on top of a transformer architecture (MiniLM)
* Fine-tuned specifically for:

  * Semantic similarity
  * Sentence embeddings
  * Search / retrieval tasks

---

## Breaking the name (useful intuition)

Even the name has meaning:

* **MiniLM** → lightweight transformer (smaller, faster than BERT)
* **L6** → 6 layers (smaller model)
* **v2** → improved version
* **all** → trained on diverse datasets (general-purpose)

---

## Why this model is used in your labs

Because it is:

* Fast (good for Colab / CPU)
* Small (low memory)
* Good enough quality for semantic tasks

So it’s a **practical engineering choice**, not random.

---

## What happens when you load it

Internally:

1. The library checks if model exists locally
2. If not → downloads from Hugging Face
3. Loads:

   * Tokenizer
   * Transformer model
   * Pooling layer (for sentence embedding)

After that, it is ready:

```python
model.encode("text")
```

---

## Important clarification

You said:

> “pre-trained model of Hugging Face”

More precisely:

> It is a pretrained model **hosted on Hugging Face, but trained by the Sentence-Transformers team**

Hugging Face is the **platform**, not always the creator.

---

## Final mental model

Think like this:

* `sentence-transformers` → library
* `"all-MiniLM-L6-v2"` → pretrained model you choose
* `SentenceTransformer(...)` → loads that model
* `.encode()` → converts text → embedding

---

You now understand:

* Library
* Model
* Execution flow

This is exactly the level of clarity needed before moving deeper.

