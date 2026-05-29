"""
Module 1.4 Lab: The ML Taxonomy
Supervised, Unsupervised, and Reinforcement Learning in action

All three types demonstrated with the same theme: customer behavior data
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)

print("=" * 65)
print("MODULE 1.4 LAB: The ML Taxonomy")
print("All three types of ML on customer behavior data")
print("=" * 65)


# ============================================================
# SHARED DATASET: Paytm-style customer data
# ============================================================

n = 80

transactions_per_month = np.random.randint(1, 50, n)
avg_transaction_value  = np.random.randint(50, 5000, n)
account_age_months     = np.random.randint(1, 60, n)
failed_verifications   = np.random.randint(0, 10, n)

# Delivery time: realistic function of distance and prep time
delivery_time = (
    transactions_per_month * 0.4 +
    avg_transaction_value * 0.003 +
    account_age_months * 0.5 +
    np.random.normal(0, 3, n)
).astype(int).clip(10, 90)

# Fraud: high-risk pattern (many failed verifications, low account age)
fraud_score = (
    failed_verifications * 2.5
    - account_age_months * 0.3
    + np.random.normal(0, 1, n)
)
is_fraud = (fraud_score > fraud_score.mean()).astype(int)

df = pd.DataFrame({
    "transactions_per_month": transactions_per_month,
    "avg_transaction_value":  avg_transaction_value,
    "account_age_months":     account_age_months,
    "failed_verifications":   failed_verifications,
    "monthly_spend":          delivery_time,
    "is_fraud":               is_fraud,
})

print(f"\nDataset: {len(df)} Paytm-style customer records")
print(df.head(5).to_string(index=False))


# ============================================================
# PART 1: SUPERVISED LEARNING - REGRESSION
# Predict monthly spend from customer features
# ============================================================

print("\n" + "=" * 65)
print("PART 1: SUPERVISED LEARNING - REGRESSION")
print("Goal: predict a customer's monthly spend (a number)")
print("=" * 65)

features = ["transactions_per_month", "avg_transaction_value", "account_age_months"]
X = df[features]
y = df["monthly_spend"]

split = int(0.8 * len(df))
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

mae = np.mean(np.abs(y_test.values - y_pred))

print(f"\nModel trained on {len(X_train)} examples")
print(f"Tested on {len(X_test)} unseen examples")
print(f"\nSample predictions vs actual values:")
print(f"{'Actual':>10}  {'Predicted':>10}  {'Diff':>6}")
print("-" * 32)
for actual, predicted in list(zip(y_test.values[:8], y_pred[:8])):
    diff = abs(actual - predicted)
    print(f"{actual:>10}  {predicted:>10.1f}  {diff:>6.1f}")

print(f"\nMean Absolute Error: {mae:.1f} units")
print("Interpretation: on average, predictions are off by this many units")
print("\nKey takeaway: the OUTPUT is a number (monthly spend)")
print("That is what makes this REGRESSION")


# ============================================================
# PART 2: SUPERVISED LEARNING - CLASSIFICATION
# Predict whether a customer is fraudulent (yes/no)
# ============================================================

print("\n" + "=" * 65)
print("PART 2: SUPERVISED LEARNING - CLASSIFICATION")
print("Goal: predict if a transaction is fraud (a category: yes/no)")
print("=" * 65)

features_clf = ["transactions_per_month", "account_age_months", "failed_verifications"]
X_clf = df[features_clf]
y_clf = df["is_fraud"]

X_tr, X_te = X_clf.iloc[:split], X_clf.iloc[split:]
y_tr, y_te = y_clf.iloc[:split], y_clf.iloc[split:]

clf = LogisticRegression(random_state=42, max_iter=500)
clf.fit(X_tr, y_tr)
y_pred_clf = clf.predict(X_te)
acc = accuracy_score(y_te, y_pred_clf) * 100

print(f"\nModel trained on {len(X_tr)} labeled examples")
print(f"Tested on {len(X_te)} unseen examples")
print(f"\nSample predictions vs actual labels:")
print(f"{'Actual':>10}  {'Predicted':>10}  {'Correct?':>10}")
print("-" * 36)
labels = {0: "legit", 1: "fraud"}
for actual, predicted in list(zip(y_te.values[:8], y_pred_clf[:8])):
    correct = "yes" if actual == predicted else "no"
    print(f"{labels[actual]:>10}  {labels[predicted]:>10}  {correct:>10}")

print(f"\nClassification accuracy: {acc:.1f}%")
print("\nKey takeaway: the OUTPUT is a category (fraud or legit)")
print("That is what makes this CLASSIFICATION")


# ============================================================
# PART 3: UNSUPERVISED LEARNING - CLUSTERING
# Discover natural customer segments with no labels
# ============================================================

print("\n" + "=" * 65)
print("PART 3: UNSUPERVISED LEARNING - CLUSTERING")
print("Goal: discover hidden customer groups (no labels provided)")
print("=" * 65)

features_clust = ["transactions_per_month", "avg_transaction_value",
                  "account_age_months", "failed_verifications"]
X_clust = df[features_clust]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_clust)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_scaled)
df["cluster"] = cluster_labels

print("\nNo labels were provided to the model.")
print("The algorithm discovered 3 natural groups on its own:\n")

cluster_summary = df.groupby("cluster")[features_clust].mean().round(1)
print(cluster_summary.to_string())

print("\nHuman interpretation of discovered clusters:")
for cluster_id in sorted(df["cluster"].unique()):
    group = df[df["cluster"] == cluster_id]
    freq  = group["transactions_per_month"].mean()
    val   = group["avg_transaction_value"].mean()
    age   = group["account_age_months"].mean()
    risk  = group["failed_verifications"].mean()
    size  = len(group)

    if risk > 4:
        name = "High-risk accounts"
    elif freq > 25:
        name = "Power users"
    else:
        name = "Casual users"

    print(f"  Cluster {cluster_id} ({size} customers): {name}")
    print(f"    Freq={freq:.0f}/mo  Val=Rs{val:.0f}  Age={age:.0f}mo  Fails={risk:.1f}")

print("\nKey takeaway: no labels were given. The model found structure on its own.")
print("That is what makes this UNSUPERVISED LEARNING")


# ============================================================
# PART 4: REINFORCEMENT LEARNING - DEMONSTRATION
# Simplified multi-armed bandit (no external library needed)
# ============================================================

print("\n" + "=" * 65)
print("PART 4: REINFORCEMENT LEARNING - SIMPLIFIED DEMO")
print("Goal: learn best price tier through trial and reward")
print("=" * 65)

print("""
Scenario: PayTM wants to learn the best cashback offer to show users.
Three options: 5%, 10%, 15% cashback.
Each has a different real acceptance probability (unknown to the model).
The RL agent tries each option and learns from user responses.
""")

true_acceptance = {0: 0.20, 1: 0.50, 2: 0.35}
option_names    = {0: "5% cashback", 1: "10% cashback", 2: "15% cashback"}

counts  = [0, 0, 0]
rewards = [0.0, 0.0, 0.0]
total_reward = 0
history_log  = []

print(f"{'Round':>6}  {'Action':>14}  {'Result':>10}  {'Running total':>14}")
print("-" * 50)

for round_num in range(1, 31):
    if round_num <= 3:
        action = round_num - 1
    else:
        avg = [rewards[i] / counts[i] if counts[i] > 0 else 0 for i in range(3)]
        action = int(np.argmax(avg))

    result = 1 if np.random.random() < true_acceptance[action] else 0
    counts[action]  += 1
    rewards[action] += result
    total_reward    += result

    if round_num <= 10 or round_num % 5 == 0:
        outcome = "accepted" if result == 1 else "declined"
        print(f"{round_num:>6}  {option_names[action]:>14}  {outcome:>10}  {total_reward:>14}")

print(f"\nAfter 30 rounds:")
for i in range(3):
    avg = rewards[i] / counts[i] if counts[i] > 0 else 0
    print(f"  {option_names[i]}: tried {counts[i]} times, avg acceptance {avg:.0%}")

best = max(range(3), key=lambda i: rewards[i]/counts[i] if counts[i] > 0 else 0)
print(f"\nAgent learned: '{option_names[best]}' is the best offer")
print(f"True best option: '{option_names[1]}' (50% acceptance)")
print("\nKey takeaway: no dataset. The model learned by trying actions and")
print("observing rewards. That is what makes this REINFORCEMENT LEARNING")


# ============================================================
# FINAL COMPARISON
# ============================================================

print("\n" + "=" * 65)
print("SIDE-BY-SIDE COMPARISON")
print("=" * 65)
print(f"""
{'Type':<28} {'Has Labels?':<14} {'Output type':<20} {'Real example'}
{'-'*85}
{'Regression (supervised)':<28} {'Yes':<14} {'A number':<20} Predict monthly spend
{'Classification (supervised)':<28} {'Yes':<14} {'A category':<20} Detect fraud yes/no
{'Clustering (unsupervised)':<28} {'No':<14} {'Group IDs':<20} Find customer segments
{'Reinforcement learning':<28} {'No dataset':<14} {'A policy':<20} Learn best cashback offer
""")
