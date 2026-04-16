

# SECTION 3 — Types of Embeddings (Token vs Contextual vs Sentence)

Now that you understand what embeddings are, the next important step is to understand:

> Not all embeddings are the same.

Different types of embeddings are designed for different purposes. Using the wrong type leads to incorrect results, especially in real systems like search or RAG.


<img width="691" height="364" alt="image" src="https://github.com/user-attachments/assets/cdecd71b-3f4d-491a-b2cd-38f0a2ef9bf5" />


---

## Why this distinction matters

So far, we treated embeddings as a single concept. But in practice:

* Some embeddings represent **individual words**
* Some represent **words in context**
* Some represent **entire sentences**

Each type answers a different problem.

---

## 3.1 Token Embeddings (Static Embeddings)

These were the first successful embedding models.

Examples:

* Word2Vec
* GloVe

### What they do

They assign a fixed vector to each word.

Example:

```id="sux8yx"
"bank" → [0.21, -0.33, ..., 0.78]
```

This vector is always the same, no matter the sentence.

---

### Limitation

This is the key issue:

```id="fxo1dr"
"I deposited money in the bank"
"The river bank is beautiful"
```

Both use the same vector for **“bank”**

So:

> No understanding of context

---

### When they are useful

* Basic NLP tasks
* Low-resource environments
* When context is not critical

---

## 3.2 Contextual Embeddings

This is a major improvement.

Examples:

* BERT
* Transformer-based models

### What they do

The embedding of a word changes depending on its context.

Example:

```id="k99n3i"
bank (financial context) → vector A  
bank (river context) → vector B
```

So:

> Same word → different vectors based on meaning

---

### Why this is powerful

Now the model understands:

* Polysemy (multiple meanings of a word)
* Sentence-level context
* Relationships between words in a sentence

---

### Where this is used

* Question answering
* Named entity recognition
* Language understanding tasks

---

## 3.3 Sentence Embeddings

This is what you used in your labs.

Examples:

* Sentence-BERT
* Models from sentence-transformers

---

### What they do

Convert the **entire sentence into a single vector**

```id="e9sx5n"
"I love AI" → [0.12, -0.44, ..., 0.67]
```

---

### Why this is important

Instead of comparing words, you compare:

> Meaning of full sentences

---

### Where this is used

* Semantic search
* Document retrieval
* Clustering
* Recommendation systems

This is the most practical type for real-world systems.

---

## Key Comparison

| Type       | Context Awareness | Output Level | Use Case               |
| ---------- | ----------------- | ------------ | ---------------------- |
| Token      | No                | Word         | Basic NLP              |
| Contextual | Yes               | Word         | Deep language tasks    |
| Sentence   | Yes               | Sentence     | Search, RAG, retrieval |

---

## Common mistake (important)

Many beginners assume:

> “All embeddings understand context”

This is not true.

* Word2Vec → no context
* BERT → context-aware
* Sentence-BERT → context-aware + sentence-level

---

## Practical intuition

Think like this:

* Token embeddings → dictionary
* Contextual embeddings → sentence understanding
* Sentence embeddings → meaning summary

---

## What this section establishes

After this, you should clearly know:

* There are different types of embeddings
* Context is not always captured (depends on model)
* Sentence embeddings are most useful for search and retrieval
* Choosing the right embedding type is critical in system design

---

Next:

**Section 4 — Similarity & Distance: The Language of Meaning**
