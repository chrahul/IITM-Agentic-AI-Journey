# Module 1.4 Lab Guide: The ML Taxonomy

## What You Will Build

Four working ML models in a single script, one for each type:
- Supervised regression (predict monthly spend)
- Supervised classification (detect fraud)
- Unsupervised clustering (discover customer segments)
- Reinforcement learning (learn best cashback offer)

All four use the same Paytm-style customer dataset so you can directly feel the difference.

---

## Setup

```
pip install pandas scikit-learn numpy
python ml_taxonomy_lab.py
```

---

## What Each Part Demonstrates

### Part 1: Regression

Labeled data plus a numeric target. Linear Regression learns the mathematical
relationship between customer features and monthly spend.

Output: a number (34.3, 16.5, 40.3...)
What makes it regression: the answer lives on a continuous scale.

### Part 2: Classification

Labeled data plus a categorical target. Logistic Regression learns the
boundary between fraud and legitimate behavior.

Output: a category (fraud or legit)
What makes it classification: the answer is one of a fixed set of labels.

### Part 3: Clustering (Unsupervised)

No labels at all. KMeans discovers the natural groupings hiding in customer
behavioral data. The algorithm found three clusters. Humans named them afterward.

Output: group membership (cluster 0, 1, 2)
What makes it unsupervised: no correct answers were provided during training.

### Part 4: Reinforcement Learning

No static dataset. A simplified bandit agent tries three cashback offers
(5%, 10%, 15%), observes which users accept, and learns the best policy.

Output: a learned policy (which offer to show)
What makes it reinforcement: the model learns from the consequences of its own actions.

---

## Key Questions for Students

1. You want to predict how many days until a customer churns.
   Which type? (Regression - it is a number)

2. You want to group users into budget, mid, and premium segments
   but you have no predefined segments yet.
   Which type? (Unsupervised clustering)

3. You want to classify support tickets as billing, technical, or complaint.
   Which type? (Classification - fixed categories)

4. You want to train a bot to navigate a warehouse autonomously.
   Which type? (Reinforcement learning - learns from movement outcomes)

---

## The One-Question Decision Rule

Ask: does my training data have correct answers already attached?

- Yes, and the answer is a number: Supervised Regression
- Yes, and the answer is a category: Supervised Classification
- No labels at all: Unsupervised Learning
- No static dataset, model learns by acting: Reinforcement Learning

---

## Next Module

Module 1.5: Two Fundamental Tasks

A deeper dive into regression and classification with more algorithms,
evaluation metrics, and hands-on examples.
