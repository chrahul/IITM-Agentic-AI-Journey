# Module 1.5 Lab Guide: Two Fundamental Tasks

## What You Will Build

Two complete supervised learning pipelines with proper evaluation:

- A regression model that predicts movie opening weekend ticket sales (BookMyShow)
- A classification model that detects fraudulent transactions (Paytm)
- A live demonstration of overfitting and why it matters

---

## Setup

```
pip install pandas scikit-learn numpy
python fundamental_tasks_lab.py
```

---

## What Each Part Shows

### Part 1: Regression

Predicts a continuous number: how many tickets will a new Bollywood movie sell
on its opening weekend?

Key output to study:
- MAE and RMSE: two different ways to measure how wrong you are
- Feature weights: which factors actually drive ticket sales most
  (holiday week matters more than number of screens)
- Error as a percentage of the total range: puts raw error in context

### Part 2: Classification

Predicts a category: is this Paytm transaction fraudulent or legitimate?

Key output to study:
- The confusion matrix: four cells telling you four very different stories
- Precision vs Recall: why 88.5% accuracy hides important information
- Feature importance: failed verification attempts are the strongest fraud signal
- Business interpretation: 29 missed frauds vs 17 blocked legitimate users

### Part 3: Overfitting demonstration

Same classification problem, same data, but with trees of increasing depth.

Watch what happens:
- Depth 1: 80.8% train, 79.0% test. Consistent. Good.
- Depth 5: 90.0% train, 87.0% test. Still consistent. Good.
- Depth 10: 98.1% train, 85.8% test. Gap appearing. Caution.
- Unlimited: 100.0% train, 84.8% test. Memorizing. Useless in production.

The unlimited depth model literally memorized every training example.
On new data, it performs no better than the simple depth-5 model.

---

## Key Questions for Students

1. Our regression MAE is 166,433 tickets. The range is 3.1M to 7.4M tickets.
   Is this error acceptable?
   (It is 3.9% of the range. Context determines if that is good enough.)

2. Our fraud model has 88.5% accuracy. Is that enough to deploy?
   (No. 29 missed fraud cases out of 166 real cases means 17.5% of fraud
   slips through. Whether that is acceptable is a business decision.)

3. If Paytm wants to catch more fraud even if it means blocking more
   legitimate users, which direction should we adjust the threshold?
   (Lower the classification threshold. This increases recall, lowers precision.)

4. The unlimited depth tree scores 100% on training data. Should we deploy it?
   (Absolutely not. It memorized noise and has no ability to generalize.)

---

## The One-Sentence Rule for Each Metric

MAE: on average, how many units are we off by?
RMSE: same as MAE but large errors count more, squared.
Accuracy: what fraction did we get right? (use with caution on imbalanced data)
Precision: of all our alerts, what fraction were actually correct?
Recall: of all actual positives, what fraction did we catch?
F1: harmonic mean of precision and recall, useful when both matter equally.

---

## Experiments to Try

Experiment 1: Change the test size from 0.2 to 0.4 in the regression model.
Does MAE go up or down? Why?

Experiment 2: In the fraud classifier, try LogisticRegression instead of
RandomForestClassifier. Compare their recall scores.

Experiment 3: Add a new engineered feature to the fraud dataset:
is_late_night = (hour < 5) or (hour > 22)
Does recall improve?

---

## Next: Section 2

With Section 1 complete, you now understand:
- Why traditional programming fails at complex problems
- How ML learns from data instead of rules
- Why data quality matters more than algorithm choice
- The three types of ML: supervised, unsupervised, reinforcement
- The two fundamental tasks: regression and classification
- How to evaluate models honestly beyond simple accuracy

Section 2 opens with the question:
If ML works so well, why did we need something new?
The answer is what broke open the modern AI era.
