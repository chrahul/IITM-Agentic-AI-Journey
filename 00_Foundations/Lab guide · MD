# Module 1.2 Lab: Building Your First Machine Learning Model

## Objective
Build a spam email classifier from scratch to understand the Machine Learning paradigm in action.

## Prerequisites
- Python 3.7 or higher installed
- Basic command line knowledge
- Text editor or IDE (VS Code, PyCharm, or Jupyter Notebook)

---

## Setup Instructions

### Step 1: Create Project Directory
```bash
mkdir ml-spam-classifier
cd ml-spam-classifier
```

### Step 2: Install Required Libraries
```bash
pip install scikit-learn pandas numpy
```

These libraries provide:
- **scikit-learn**: Machine learning algorithms
- **pandas**: Data manipulation
- **numpy**: Numerical computations

### Step 3: Create the Python Script

Create a file named `spam_classifier.py` and copy the code from this repository.

---

## Understanding the Code

### Part 1: The Three Ingredients

#### Ingredient 1: DATA
```python
emails = [
    "Congratulations! You won a FREE iPhone",  # spam
    "Hi John, can we schedule a meeting",      # not spam
    # ... more examples
]

labels = [1, 1, 1, 0, 0, 0]  # 1=spam, 0=not spam
```

**Key concept**: We provide examples with correct answers. The model learns from these.

#### Ingredient 2: MODEL
```python
vectorizer = CountVectorizer()  # Converts text to numbers
model = MultinomialNB()         # The learning algorithm
```

**Key concept**: The model is initially untrained (random guessing).

#### Ingredient 3: FEEDBACK LOOP
```python
model.fit(X_train_vectors, y_train)  # This is where training happens
```

**Key concept**: The model adjusts its internal parameters by:
1. Making predictions
2. Comparing to correct labels
3. Calculating error
4. Adjusting weights
5. Repeating

---

## Running the Demo

### Step 1: Execute the Script
```bash
python spam_classifier.py
```

### Step 2: Observe the Output

You will see:
1. **Data Loading**: How many examples we have
2. **Model Setup**: Vocabulary size and features
3. **Training**: The learning process
4. **Evaluation**: Accuracy on test data
5. **Live Predictions**: Testing on brand new emails

---

## Expected Output Explanation

### Accuracy Metrics
```
Accuracy: 75.0%
```
This means the model correctly classified 75% of test emails.

**Note**: With only 20 training examples, this is decent! Real-world models use millions of examples and achieve 99%+ accuracy.

### Predictions on New Emails
The model will classify new emails it has never seen before:
- "Free gift card..." → SPAM (correct!)
- "Team meeting tomorrow?" → NOT SPAM (correct!)

---

## Experiments to Try

### Experiment 1: Add More Training Data
Add 10 more spam and 10 more legitimate emails to the training set.

**Question**: Does accuracy improve?

### Experiment 2: Test Different Email Patterns
Create your own test emails:
```python
new_emails = [
    "Your custom test email here",
    "Another test email",
]
```

**Question**: Can you trick the model? What patterns does it recognize?

### Experiment 3: View What the Model Learned
Add this code after training:
```python
feature_names = vectorizer.get_feature_names_out()
spam_word_probs = model.feature_log_prob_[1]

# Get top 10 spam indicators
top_spam_words = sorted(zip(feature_names, spam_word_probs), 
                        key=lambda x: x[1], 
                        reverse=True)[:10]

print("Top spam indicator words:")
for word, prob in top_spam_words:
    print(f"  {word}")
```

**Question**: Which words did the model learn are strong spam indicators?

---

## Key Takeaways

1. **No Manual Rules**: We did not write "if email contains X then spam"
2. **Learning from Examples**: The model discovered patterns automatically
3. **Automatic Improvement**: More data = better accuracy
4. **Generalization**: The model works on emails it has never seen

---

## Common Issues and Solutions

### Issue 1: ImportError for sklearn
**Solution**: Make sure scikit-learn is installed:
```bash
pip install scikit-learn --upgrade
```

### Issue 2: Low Accuracy
**Reason**: Very small training set (20 examples)
**Solution**: In real projects, we use thousands/millions of examples

### Issue 3: Model Always Predicts One Class
**Reason**: Imbalanced data or too few examples
**Solution**: Ensure equal spam and non-spam examples

---

## Next Steps

After completing this lab, you should understand:
- How ML learns from examples instead of rules
- The three ingredients: Data, Model, Feedback Loop
- Why ML scales better than traditional programming

**Next Module**: We will explore different types of machine learning (Supervised, Unsupervised, Reinforcement)

---

## Additional Resources

- Scikit-learn documentation: https://scikit-learn.org
- Understanding Naive Bayes: Simple probabilistic classifier
- Real spam datasets: SpamAssassin public corpus

---

## Challenge Exercise

Build a sentiment analyzer that classifies movie reviews as positive or negative using the same approach:

1. Collect 20 movie reviews (10 positive, 10 negative)
2. Label them (1=positive, 0=negative)
3. Train a model
4. Test on new reviews

This reinforces the ML paradigm with a different problem!
