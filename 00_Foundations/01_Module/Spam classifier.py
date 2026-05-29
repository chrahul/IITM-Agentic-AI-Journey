"""
Simple Spam Email Classifier - Machine Learning Paradigm Demo
This demonstrates the three ingredients: Data, Model, Feedback Loop
"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

print("=" * 60)
print("MACHINE LEARNING PARADIGM DEMONSTRATION")
print("Building a Spam Classifier from Examples")
print("=" * 60)

# ============================================================
# INGREDIENT 1: DATA (Training Examples with Labels)
# ============================================================
print("\n[INGREDIENT 1: DATA]")
print("Collecting training examples...\n")

# Real email examples (in real projects, you would have thousands)
emails = [
    # SPAM examples
    "Congratulations! You won a FREE iPhone. Click here now to claim",
    "URGENT: Your account will be suspended. Verify immediately",
    "Make money fast! Work from home, earn thousands weekly",
    "Free money waiting for you. Act now, limited time offer",
    "You have been selected for a special prize. Click to claim",
    "Hot singles in your area want to meet you tonight",
    "Get rich quick with this one simple trick doctors hate",
    "Your package is waiting. Pay small fee to release shipment",
    "CONGRATULATIONS winner! Claim your lottery prize now",
    "Lose 20 pounds in 2 weeks with this miracle pill",
    
    # NOT SPAM examples (legitimate emails)
    "Hi John, can we schedule a meeting for tomorrow at 3pm?",
    "Your Amazon order has shipped and will arrive on Friday",
    "Team lunch at the new Italian place on Main Street?",
    "Reminder: Project deadline is next Monday",
    "Thanks for your presentation yesterday. Great insights!",
    "Your Netflix subscription payment was successful",
    "Mom: Remember to call grandma on her birthday",
    "Quarterly report is attached. Please review and provide feedback",
    "Welcome to our platform! Here is your getting started guide",
    "Your appointment with Dr. Smith is confirmed for Tuesday",
]

# Labels: 1 = spam, 0 = not spam
labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # first 10 are spam
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # last 10 are not spam

print(f"Total training examples: {len(emails)}")
print(f"Spam examples: {sum(labels)}")
print(f"Legitimate examples: {len(labels) - sum(labels)}")
print("\nExample spam email:")
print(f"  '{emails[0]}'")
print("\nExample legitimate email:")
print(f"  '{emails[10]}'")

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    emails, labels, test_size=0.2, random_state=42
)

print(f"\nSplit into:")
print(f"  Training set: {len(X_train)} emails")
print(f"  Test set: {len(X_test)} emails")

# ============================================================
# INGREDIENT 2: MODEL (The Pattern Matcher)
# ============================================================
print("\n" + "=" * 60)
print("[INGREDIENT 2: MODEL]")
print("Setting up the pattern-matching machine...\n")

# Convert text to numbers (machines understand numbers, not words)
vectorizer = CountVectorizer()
print("Converting emails to numerical features...")
print("(Counting word frequencies)")

X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

print(f"  Vocabulary size: {len(vectorizer.get_feature_names_out())} unique words")
print(f"  Each email is now represented as {X_train_vectors.shape[1]} numbers")

# Create the model (Naive Bayes classifier - simple but effective)
model = MultinomialNB()
print("\nModel created: Naive Bayes classifier")
print("  Current state: UNTRAINED (random guessing)")

# ============================================================
# INGREDIENT 3: FEEDBACK LOOP (Training Process)
# ============================================================
print("\n" + "=" * 60)
print("[INGREDIENT 3: FEEDBACK LOOP]")
print("Training the model...\n")

print("The model is now:")
print("  1. Looking at each email")
print("  2. Making predictions")
print("  3. Comparing to correct labels")
print("  4. Adjusting internal parameters")
print("  5. Repeating until patterns are learned\n")

# THIS IS WHERE THE MAGIC HAPPENS
model.fit(X_train_vectors, y_train)

print("Training complete!")
print("  The model has learned patterns from examples")
print("  No rules were manually written")

# ============================================================
# EVALUATION: How Good is the Model?
# ============================================================
print("\n" + "=" * 60)
print("[EVALUATION]")
print("Testing on unseen emails...\n")

# Test on the test set
y_pred = model.predict(X_test_vectors)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.1f}%")
print(f"  The model correctly classified {accuracy * 100:.1f}% of test emails\n")

print("Detailed results:")
print(classification_report(y_test, y_pred, 
                          target_names=['Not Spam', 'Spam'],
                          zero_division=0))

# ============================================================
# DEMONSTRATION: Making Predictions on New Emails
# ============================================================
print("=" * 60)
print("[LIVE PREDICTIONS]")
print("Testing on brand new emails the model has never seen...\n")

new_emails = [
    "Free gift card waiting for you. Click now to claim your prize",
    "Hey, are you coming to the team meeting tomorrow?",
    "URGENT: Verify your bank account or it will be closed",
    "The project documentation is attached. Let me know if you have questions"
]

# Convert new emails to same format
new_vectors = vectorizer.transform(new_emails)

# Make predictions
predictions = model.predict(new_vectors)

for email, prediction in zip(new_emails, predictions):
    label = "SPAM" if prediction == 1 else "NOT SPAM"
    print(f"Email: '{email[:60]}...'")
    print(f"Prediction: {label}\n")

# ============================================================
# KEY TAKEAWAY
# ============================================================
print("=" * 60)
print("KEY TAKEAWAY:")
print("=" * 60)
print("""
We did NOT write any rules like:
  - if email contains 'free' → spam
  - if email contains 'urgent' → spam
  
Instead, we:
  1. Provided examples (emails with labels)
  2. Let the machine discover patterns automatically
  3. The model learned which word combinations indicate spam
  
This is the Machine Learning paradigm!
""")
