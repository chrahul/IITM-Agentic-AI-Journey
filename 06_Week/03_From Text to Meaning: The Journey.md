# SECTION 1 — From Text to Meaning: The Journey

Before embeddings were introduced, machines already had ways to represent text. However, those approaches were limited because they treated language as a collection of symbols rather than as carriers of meaning.

This section traces that evolution—from simple counting methods to the need for semantic representations.

---

## The core problem

Language is inherently ambiguous and context-driven.

* The same word can have different meanings
* Different words can express the same idea
* Meaning depends on relationships, not just presence

Traditional methods struggled because they focused on **what words appear**, not **what they mean**.

---

## Step 1 — Bag of Words (BoW)

Bag of Words is one of the earliest approaches.

It represents a document as a vector based on word counts.

Example:

Sentence:

> "AI is powerful"

Vocabulary:
[AI, is, powerful]

Vector:
[1, 1, 1]

If another sentence is:

> "AI is very powerful"

Vector becomes:
[1, 1, 1, 1] (depending on vocabulary expansion)

### What it does well:

* Simple and easy to implement
* Captures word presence

### Limitations:

* Ignores word order
* No understanding of meaning
* “AI is powerful” and “powerful is AI” are identical
* “car” and “automobile” are unrelated

So:

> BoW treats text as a **bag of tokens**, not as structured language

---

## Step 2 — One-Hot Encoding

In one-hot encoding, each word is represented as a vector where:

* Only one position is 1
* All others are 0

Example vocabulary:
[cat, dog, car]

Vectors:

* cat → [1, 0, 0]
* dog → [0, 1, 0]
* car → [0, 0, 1]

### What it does well:

* Unique representation for each word
* No ambiguity in identity

### Limitations:

* No relationship between words
* All vectors are equally distant
* High dimensional and sparse

So:

> One-hot encoding captures **identity**, but not **similarity**

---

## Step 3 — TF-IDF (Term Frequency–Inverse Document Frequency)

TF-IDF improves on Bag of Words by weighting words based on importance.

* Words that appear frequently in a document → higher weight
* Words that appear in many documents → lower importance

This helps reduce the impact of common words like “the”, “is”, etc.

### What it does well:

* Highlights important words
* Improves document comparison over BoW

### Limitations:

* Still based on frequency
* No semantic understanding
* Cannot detect synonym relationships
* Context is ignored

So:

> TF-IDF captures **importance**, but still not **meaning**

---

## The breaking point

All these methods share a common limitation:

* They treat words as independent symbols
* They do not understand relationships between words
* They fail at capturing semantic similarity

Example:

Sentence 1:

> "I love machine learning"

Sentence 2:

> "I enjoy AI"

Traditional methods may treat these as very different, even though the intent is similar.

This is the point where a new approach becomes necessary.

---

## The shift: From counting to learning

Instead of manually defining how text should be represented, researchers moved toward **learning representations from data**.

The key idea:

> Words that appear in similar contexts tend to have similar meanings

This is known as the **distributional hypothesis**.

Example:

* “king” appears near “queen”, “royal”, “palace”
* “apple” appears near “fruit”, “tree”, “eat”

By learning from these patterns, we can assign vectors that reflect meaning.

---

## Why dense representations were needed

Earlier methods created:

* Large vectors
* Mostly zeros (sparse)
* No meaningful structure

Embeddings introduced:

* Dense vectors (compact representation)
* Continuous values (not just 0/1)
* Structured relationships

This enables:

* Similar words → similar vectors
* Analogies → vector arithmetic
* Better generalization across tasks

---

## What this section establishes

After this journey, the key understanding should be:

* Early methods (BoW, One-hot, TF-IDF) rely on frequency and presence
* They fail to capture semantic relationships
* Language requires representation based on context and usage
* This leads naturally to embeddings, where meaning is learned and encoded in vector space

---

This sets up the next section, where we will formally define embeddings and understand how meaning is represented mathematically in vector space.
