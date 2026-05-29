"""
Module 1.5 Lab: Two Fundamental Tasks
Regression and Classification with proper evaluation metrics

Demonstrates:
- Regression: predict movie ticket sales (BookMyShow)
- Classification: detect fraud (Paytm)
- Evaluation metrics: MAE, RMSE, confusion matrix, precision, recall
- Overfitting: why train score alone is meaningless
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error, mean_squared_error,
    accuracy_score, confusion_matrix,
    precision_score, recall_score, f1_score
)
import warnings
warnings.filterwarnings("ignore")

np.random.seed(42)
SEP = "=" * 65
DIV = "-" * 65

print(SEP)
print("MODULE 1.5 LAB: Two Fundamental Tasks")
print("Regression and Classification with real evaluation")
print(SEP)


# ============================================================
# DATASET 1: BookMyShow movie ticket sales (REGRESSION)
# ============================================================

n = 200

movie_rating      = np.round(np.random.uniform(5.0, 9.5, n), 1)
screens           = np.random.randint(500, 5000, n)
lead_popularity   = np.random.randint(30, 100, n)
is_holiday_week   = np.random.choice([0, 1], n, p=[0.7, 0.3])
marketing_spend   = np.random.randint(1, 50, n)

tickets_sold = (
    movie_rating       * 350000
    + screens          * 500
    + lead_popularity  * 15000
    + is_holiday_week  * 800000
    + marketing_spend  * 20000
    + np.random.normal(0, 200000, n)
).astype(int).clip(100000, 10000000)

df_reg = pd.DataFrame({
    "movie_rating":    movie_rating,
    "screens":         screens,
    "lead_popularity": lead_popularity,
    "is_holiday_week": is_holiday_week,
    "marketing_spend": marketing_spend,
    "tickets_sold":    tickets_sold
})


# ============================================================
# DATASET 2: Paytm transactions (CLASSIFICATION)
# ============================================================

m = 2000

amount       = np.random.exponential(1500, m).astype(int).clip(50, 50000)
hour         = np.random.randint(0, 24, m)
new_device   = np.random.choice([0, 1], m, p=[0.75, 0.25])
failed_tries = np.random.randint(0, 8, m)
account_age  = np.random.randint(1, 60, m)

fraud_score = (
    (hour < 5) * 2.5
    + new_device * 1.8
    + failed_tries * 0.9
    - account_age * 0.06
    + (amount > 15000) * 1.2
    + np.random.normal(0, 0.8, m)
)
is_fraud = (fraud_score > fraud_score.mean() + 0.5).astype(int)

df_clf = pd.DataFrame({
    "amount":       amount,
    "hour":         hour,
    "new_device":   new_device,
    "failed_tries": failed_tries,
    "account_age":  account_age,
    "is_fraud":     is_fraud
})

fraud_rate = is_fraud.mean() * 100
print(f"\nDatasets created:")
print(f"  Regression dataset : {len(df_reg)} movies")
print(f"  Classification dataset: {len(df_clf)} transactions ({fraud_rate:.1f}% fraud)")


# ============================================================
# PART 1: REGRESSION
# ============================================================

print(f"\n{SEP}")
print("PART 1: REGRESSION")
print("Predict opening weekend ticket sales (BookMyShow)")
print(SEP)

feat_reg = ["movie_rating", "screens", "lead_popularity",
            "is_holiday_week", "marketing_spend"]
X_r = df_reg[feat_reg]
y_r = df_reg["tickets_sold"]

X_tr, X_te, y_tr, y_te = train_test_split(X_r, y_r, test_size=0.2, random_state=42)
print(f"\nTrain size: {len(X_tr)} | Test size: {len(X_te)}")

lr = LinearRegression()
lr.fit(X_tr, y_tr)

y_pred_train = lr.predict(X_tr)
y_pred_test  = lr.predict(X_te)

mae_train  = mean_absolute_error(y_tr, y_pred_train)
mae_test   = mean_absolute_error(y_te, y_pred_test)
rmse_train = mean_squared_error(y_tr, y_pred_train) ** 0.5
rmse_test  = mean_squared_error(y_te, y_pred_test)  ** 0.5

print(f"\n{'Metric':<20} {'Train':>12} {'Test':>12}  {'Meaning'}")
print(DIV)
print(f"{'MAE':<20} {mae_train:>12,.0f} {mae_test:>12,.0f}  avg absolute error")
print(f"{'RMSE':<20} {rmse_train:>12,.0f} {rmse_test:>12,.0f}  penalizes large errors")

print(f"\nSample predictions (test set):")
print(f"  {'Actual':>12}  {'Predicted':>12}  {'Error':>12}")
print(f"  {DIV[:42]}")
for a, p in list(zip(y_te.values[:6], y_pred_test[:6])):
    err = abs(a - p)
    print(f"  {a:>12,}  {p:>12,.0f}  {err:>12,.0f}")

print(f"\nKey feature weights (what drives ticket sales):")
for feat, coef in sorted(zip(feat_reg, lr.coef_), key=lambda x: abs(x[1]), reverse=True):
    direction = "increases" if coef > 0 else "decreases"
    print(f"  {feat:<22}: {direction} sales by {abs(coef):,.0f} per unit")

print(f"\nInterpretation:")
print(f"  On average, our predictions are off by {mae_test:,.0f} tickets.")
print(f"  Total range of ticket sales: {y_te.min():,} to {y_te.max():,}")
print(f"  Error as % of range: {mae_test/(y_te.max()-y_te.min())*100:.1f}%")


# ============================================================
# PART 2: CLASSIFICATION
# ============================================================

print(f"\n{SEP}")
print("PART 2: CLASSIFICATION")
print("Detect fraudulent transactions (Paytm)")
print(SEP)

feat_clf = ["amount", "hour", "new_device", "failed_tries", "account_age"]
X_c = df_clf[feat_clf]
y_c = df_clf["is_fraud"]

X_tc, X_ec, y_tc, y_ec = train_test_split(X_c, y_c, test_size=0.2, random_state=42)
print(f"\nTrain size: {len(X_tc)} | Test size: {len(X_ec)}")
print(f"Fraud rate in test set: {y_ec.mean()*100:.1f}%")

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_tc, y_tc)
y_pred_c = clf.predict(X_ec)

acc    = accuracy_score(y_ec, y_pred_c) * 100
prec   = precision_score(y_ec, y_pred_c, zero_division=0) * 100
rec    = recall_score(y_ec, y_pred_c, zero_division=0) * 100
f1     = f1_score(y_ec, y_pred_c, zero_division=0) * 100
cm     = confusion_matrix(y_ec, y_pred_c)

tn, fp, fn, tp = cm.ravel()

print(f"\nConfusion matrix:")
print(f"  {'':20} {'Predicted LEGIT':>16} {'Predicted FRAUD':>16}")
print(f"  {'Actual LEGIT':20} {tn:>16,} {fp:>16,}")
print(f"  {'Actual FRAUD':20} {fn:>16,} {tp:>16,}")

print(f"\nEvaluation metrics:")
print(f"  {'Accuracy':20}: {acc:>6.1f}%  (correct out of total - misleading alone!)")
print(f"  {'Precision':20}: {prec:>6.1f}%  (of fraud alerts fired, % actually fraud)")
print(f"  {'Recall':20}: {rec:>6.1f}%  (of real fraud, % we actually caught)")
print(f"  {'F1 score':20}: {f1:>6.1f}%  (balance of precision and recall)")

print(f"\nBusiness interpretation:")
print(f"  Real fraud cases in test:  {tp + fn}")
print(f"  Fraud we caught:           {tp} ({tp/(tp+fn)*100:.0f}% recall)")
print(f"  Fraud we missed:           {fn} (false negatives - dangerous!)")
print(f"  Legit blocked by mistake:  {fp} (false positives - annoying)")
print(f"  Legit correctly cleared:   {tn}")

print(f"\nFeature importance (what signals fraud most):")
importances = sorted(zip(feat_clf, clf.feature_importances_),
                     key=lambda x: x[1], reverse=True)
for feat, imp in importances:
    bar = int(imp * 40)
    print(f"  {feat:<15} {'|' * bar} {imp:.3f}")


# ============================================================
# PART 3: OVERFITTING DEMONSTRATION
# ============================================================

print(f"\n{SEP}")
print("PART 3: OVERFITTING DEMONSTRATION")
print("Why train score alone tells you nothing")
print(SEP)

from sklearn.tree import DecisionTreeClassifier

print(f"\nTraining decision trees of increasing depth on fraud data:")
print(f"\n  {'Max depth':>10} {'Train accuracy':>16} {'Test accuracy':>15} {'Status'}")
print(f"  {DIV[:60]}")

for depth in [1, 3, 5, 10, 20, None]:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_tc, y_tc)

    train_acc = accuracy_score(y_tc, dt.predict(X_tc)) * 100
    test_acc  = accuracy_score(y_ec, dt.predict(X_ec)) * 100
    gap       = train_acc - test_acc
    label     = str(depth) if depth else "unlimited"

    if gap > 8:
        status = "OVERFIT - memorizing"
    elif train_acc < 70:
        status = "underfit - too simple"
    else:
        status = "good fit"

    print(f"  {label:>10} {train_acc:>14.1f}% {test_acc:>14.1f}%  {status}")

print(f"""
Key lesson:
  Unlimited depth tree: near-perfect train accuracy, collapses on test data.
  The model memorized every training example.

  Shallow trees: low train accuracy but consistent on test.
  They learned the actual pattern, not the noise.

  Always evaluate on data the model has NEVER seen during training.
""")


# ============================================================
# SUMMARY
# ============================================================

print(SEP)
print("MODULE 1.5 SUMMARY")
print(SEP)
print("""
Regression:
  Output is a continuous number
  Metrics: MAE (average error), RMSE (punishes big errors)
  Algorithm: start with Linear Regression, escalate if needed

Classification:
  Output is a category from a fixed set
  Metrics: accuracy is misleading alone. Use confusion matrix.
  Precision: of all alerts, how many were real?
  Recall: of all real cases, how many did we catch?
  Algorithm: start with Logistic Regression, escalate if needed

Overfitting:
  High train score + low test score = your model memorized, not learned
  Always hold out a test set and never touch it until final evaluation

The practitioner mindset:
  Start simple. Measure correctly. Escalate only when you have evidence.
""")
