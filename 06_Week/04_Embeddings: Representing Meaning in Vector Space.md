# SECTION 2 — Embeddings: Representing Meaning in Vector Space

In the previous section, we saw why traditional methods fail—they cannot capture meaning.
This section introduces embeddings as a solution, but more importantly, explains **how meaning is encoded mathematically**.

---

## What is an embedding?

An embedding is a way of representing text (word, sentence, or document) as a vector of numbers such that:

* Similar meanings → similar vectors
* Different meanings → distant vectors

Unlike earlier methods, these vectors are:

* Dense (not sparse)
* Continuous (not just 0/1)
* Learned from data (not manually defined)

A simple way to state it:

> An embedding is a mapping from language to a structured numerical space where semantic relationships are preserved.

---

## From text to vector

When you pass text into an embedding model, it outputs a vector like:

```
"I love AI" → [0.21, -0.44, 0.78, ..., 0.13]
```

This vector may have:

* 100 dimensions
* 384 dimensions
* 768 or more

Each number by itself has no direct human meaning.

The meaning comes from:

> The **relative position of this vector compared to others**

---

## High-dimensional vector space

Embeddings exist in a high-dimensional space.

* Each dimension = one axis
* A vector = one point in that space

You cannot visualize 768 dimensions, but the concept is the same as 2D or 3D:

* Close points → similar
* Far points → different

So instead of asking:

* “What does this word mean?”

We ask:

* “Where is this word located in relation to others?”

---

## Meaning as geometry

This is the most important idea in this section.

Meaning is not stored explicitly.
It is encoded geometrically.

### Example:

* “king” and “queen” are close
* “king” and “apple” are far

But more interestingly:

```
king - man + woman ≈ queen
```

This shows:

* Relationships are encoded as **directions in space**
* Not just similarity, but structure exists

So:

> Embeddings capture both **proximity (similarity)** and **direction (relationships)**

---

## The distributional hypothesis

This is the foundation of embeddings.

> “You shall know a word by the company it keeps”

Meaning:

* Words used in similar contexts tend to have similar meanings

Example:

* “dog” appears near “bark”, “pet”, “animal”
* “cat” appears near similar words

So the model learns:

* dog ≈ cat (close in vector space)

This learning happens over massive text data.

---

## Why embeddings work

Embeddings work because they convert an abstract problem (language) into a mathematical one (geometry).

This enables:

* Similarity → distance calculation
* Search → nearest neighbor lookup
* Clustering → grouping nearby vectors
* Reasoning → vector arithmetic

Instead of rules, we rely on:

> Mathematical structure learned from data

---

## Important clarification

A common misconception is:

> “Each dimension represents something meaningful”

In most cases, this is not true.

* Individual dimensions are not interpretable
* Meaning is distributed across the entire vector

So:

> Meaning is not in individual numbers, but in the overall pattern

---

## Types of embedding inputs

Embeddings can be created for different levels:

* Word embeddings → single words
* Sentence embeddings → full sentences
* Document embeddings → large text blocks

Each has different use cases, which we will explore in the next section.

---

## What this section establishes

After this section, the key understanding should be:

* Embeddings map text into a high-dimensional vector space
* Meaning is encoded as position and distance
* Relationships are captured through geometry
* Similarity and reasoning can be performed using mathematical operations

This is the foundation for everything that follows—especially similarity measures and vector search.

---

Next, we will move to:

**Section 3 — Types of Embeddings (Token vs Contextual vs Sentence)**
