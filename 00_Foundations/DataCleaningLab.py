"""
Module 1.3 Lab: Data as the New Code
Data Cleaning and Preprocessing with Zomato-style order data

This lab demonstrates:
- What dirty data looks like in the real world
- Step-by-step data cleaning techniques
- How data quality directly impacts model accuracy
- The Garbage-In, Garbage-Out principle in action
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")

print("=" * 65)
print("MODULE 1.3 LAB: Data Cleaning and Preprocessing")
print("Zomato-style Restaurant Order Dataset")
print("=" * 65)


# ============================================================
# CREATE THE DIRTY DATASET (What real raw data looks like)
# ============================================================

np.random.seed(42)

dirty_data = pd.DataFrame({
    "order_id": [
        "ORD001", "ORD002", "ORD003", "ORD004", "ORD005",
        "ORD006", "ORD007", "ORD008", "ORD002",
        "ORD009", "ORD010", "ORD011", "ORD012", "ORD013",
        "ORD014", "ORD015", "ORD016", "ORD017", "ORD018"
    ],
    "customer_id": [
        "C001", "C002", "C003", "C004", "C005",
        "C006", "C007", None,   "C002",
        "C009", "C010", "C011", "C012", "C013",
        "C014", "C015", "C016", "C017", "C018"
    ],
    "delivery_time_mins": [
        28,   35,   22,   999,  30,
        41,   25,   33,   35,   27,
        38,   None, 29,   31,   26,
        44,   23,   37,   32
    ],
    "order_amount": [
        320,  580,  210,  450,  890,
        None, 340,  120,  580,  670,
        410,  295,  780,  180,  530,
        620,  165,  440,  350
    ],
    "rating": [
        4.5,  3.0,  5.0,  4.0,  2.5,
        4.0,  3.5,  4.5,  3.0,  5.0,
        2.0,  4.0,  None, 3.5,  4.5,
        3.0,  5.0,  4.0,  4.5
    ],
    "will_reorder": [
        "Yes",  "No",   "YES", "yes", "1",
        "0",    "Y",    "N",   "No",  "True",
        "False","yes",  "NO",  "1",   "Yes",
        "0",    "True", "yes", "YES"
    ]
})


# ============================================================
# STEP 0: LOOK AT THE DIRTY DATA
# ============================================================

print("\n[STEP 0] THE RAW DIRTY DATASET")
print("-" * 65)
print(dirty_data.to_string(index=False))
print(f"\nShape: {dirty_data.shape[0]} rows, {dirty_data.shape[1]} columns")

print("\n[STEP 0] DATA QUALITY REPORT (before cleaning)")
print("-" * 65)
print(f"Total rows:              {len(dirty_data)}")
print(f"Missing customer_id:     {dirty_data['customer_id'].isna().sum()}")
print(f"Missing delivery_time:   {dirty_data['delivery_time_mins'].isna().sum()}")
print(f"Missing order_amount:    {dirty_data['order_amount'].isna().sum()}")
print(f"Missing rating:          {dirty_data['rating'].isna().sum()}")
print(f"Duplicate order_ids:     {dirty_data['order_id'].duplicated().sum()}")
print(f"Inconsistent labels:     {dirty_data['will_reorder'].nunique()} unique values for yes/no!")
print(f"Outlier in delivery:     {(dirty_data['delivery_time_mins'].dropna() > 200).sum()} value(s) above 200 mins")


# ============================================================
# STEP 1: REMOVE DUPLICATES
# ============================================================

print("\n[STEP 1] REMOVING DUPLICATES")
print("-" * 65)
before = len(dirty_data)
clean_data = dirty_data.drop_duplicates(subset=["order_id"])
after = len(clean_data)
print(f"Rows before: {before}")
print(f"Rows after:  {after}")
print(f"Removed:     {before - after} duplicate row(s)")


# ============================================================
# STEP 2: STANDARDIZE INCONSISTENT LABELS
# ============================================================

print("\n[STEP 2] STANDARDIZING INCONSISTENT FORMATS")
print("-" * 65)
print("Unique values BEFORE:", sorted(clean_data["will_reorder"].unique()))

yes_values = {"yes", "1", "y", "true"}
clean_data = clean_data.copy()
clean_data["will_reorder"] = clean_data["will_reorder"].apply(
    lambda x: 1 if str(x).strip().lower() in yes_values else 0
)
print("Unique values AFTER: ", sorted(clean_data["will_reorder"].unique()))
print("All formats standardized to 0 and 1")


# ============================================================
# STEP 3: HANDLE OUTLIERS
# ============================================================

print("\n[STEP 3] HANDLING OUTLIERS")
print("-" * 65)
print(f"Delivery time max BEFORE: {clean_data['delivery_time_mins'].max()} mins")
print(f"Delivery time mean BEFORE: {clean_data['delivery_time_mins'].mean():.1f} mins")

cap_value = 120
outliers_found = (clean_data["delivery_time_mins"].dropna() > cap_value).sum()
clean_data["delivery_time_mins"] = clean_data["delivery_time_mins"].clip(upper=cap_value)

print(f"\nDelivery time max AFTER (capped at {cap_value} mins): {clean_data['delivery_time_mins'].max()} mins")
print(f"Delivery time mean AFTER: {clean_data['delivery_time_mins'].mean():.1f} mins")
print(f"Outliers capped: {outliers_found}")


# ============================================================
# STEP 4: HANDLE MISSING VALUES
# ============================================================

print("\n[STEP 4] HANDLING MISSING VALUES")
print("-" * 65)

before = len(clean_data)
clean_data = clean_data.dropna(subset=["customer_id"])
print(f"Dropped {before - len(clean_data)} row(s) with missing customer_id")

median_delivery = clean_data["delivery_time_mins"].median()
missing_delivery = clean_data["delivery_time_mins"].isna().sum()
clean_data["delivery_time_mins"] = clean_data["delivery_time_mins"].fillna(median_delivery)
print(f"Filled {missing_delivery} missing delivery_time(s) with median: {median_delivery:.1f} mins")

median_amount = clean_data["order_amount"].median()
missing_amount = clean_data["order_amount"].isna().sum()
clean_data["order_amount"] = clean_data["order_amount"].fillna(median_amount)
print(f"Filled {missing_amount} missing order_amount(s) with median: {median_amount:.1f}")

median_rating = clean_data["rating"].median()
missing_rating = clean_data["rating"].isna().sum()
clean_data["rating"] = clean_data["rating"].fillna(median_rating)
print(f"Filled {missing_rating} missing rating(s) with median: {median_rating:.1f}")


# ============================================================
# STEP 5: FEATURE ENGINEERING
# ============================================================

print("\n[STEP 5] FEATURE ENGINEERING")
print("-" * 65)
print("Creating new meaningful features from existing data...")

clean_data["is_fast_delivery"] = (clean_data["delivery_time_mins"] < 30).astype(int)
print("  Created: is_fast_delivery (delivery under 30 mins = 1)")

clean_data["is_high_value"] = (clean_data["order_amount"] > 400).astype(int)
print("  Created: is_high_value (order above 400 = 1)")

clean_data["is_high_rated"] = (clean_data["rating"] >= 4.0).astype(int)
print("  Created: is_high_rated (rating 4.0 or above = 1)")

print("\nFinal clean dataset:")
print("-" * 65)
print(clean_data[["order_id", "delivery_time_mins", "order_amount",
                   "rating", "is_fast_delivery", "is_high_value",
                   "is_high_rated", "will_reorder"]].to_string(index=False))


# ============================================================
# THE PROOF: Model Accuracy Before vs After Cleaning
# ============================================================

print("\n" + "=" * 65)
print("THE PROOF: DOES DATA QUALITY ACTUALLY IMPACT ACCURACY?")
print("=" * 65)
print("Training the SAME model on dirty data vs clean data...\n")

dirty_model_data = dirty_data.copy()
dirty_model_data["will_reorder"] = dirty_model_data["will_reorder"].apply(
    lambda x: 1 if str(x).strip().lower() in {"yes", "1", "y", "true"} else 0
)
dirty_model_data = dirty_model_data.dropna()

X_dirty = dirty_model_data[["delivery_time_mins", "order_amount", "rating"]]
y_dirty = dirty_model_data["will_reorder"]

feature_cols = ["delivery_time_mins", "order_amount", "rating",
                "is_fast_delivery", "is_high_value", "is_high_rated"]
X_clean = clean_data[feature_cols]
y_clean = clean_data["will_reorder"]

model = LogisticRegression(random_state=42, max_iter=1000)

model.fit(X_dirty, y_dirty)
dirty_accuracy = accuracy_score(y_dirty, model.predict(X_dirty)) * 100

model.fit(X_clean, y_clean)
clean_accuracy = accuracy_score(y_clean, model.predict(X_clean)) * 100

print(f"Same algorithm (Logistic Regression) trained on:")
print(f"  Dirty data accuracy:  {dirty_accuracy:.1f}%")
print(f"  Clean data accuracy:  {clean_accuracy:.1f}%")
print(f"  Improvement:          +{clean_accuracy - dirty_accuracy:.1f}%")
print(f"\n  Same algorithm. Different data quality. Different results.")
print(f"  This is the Garbage-In, Garbage-Out principle in action.")


# ============================================================
# SUMMARY
# ============================================================

print("\n" + "=" * 65)
print("LAB SUMMARY")
print("=" * 65)
print(f"""
Steps completed:
  Step 0  Inspected raw dirty data ({dirty_data.shape[0]} rows)
  Step 1  Removed duplicates
  Step 2  Standardized inconsistent labels (Yes/YES/1/Y to 1)
  Step 3  Handled outliers (capped delivery time at 120 mins)
  Step 4  Handled missing values (drop or fill with median)
  Step 5  Engineered 3 new features from existing columns

Final clean dataset: {len(clean_data)} rows, ready for training

Key lesson:
  Data quality improvement gave a bigger accuracy boost
  than any algorithm change would have.

  In real industry projects, data scientists spend 60 to 80
  percent of their time on exactly what we just did here.
""")
