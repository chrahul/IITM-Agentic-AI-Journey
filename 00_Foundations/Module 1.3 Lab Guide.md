# Module 1.3 Lab Guide: Data as the New Code

## What You Will Build

A complete data cleaning pipeline using a Zomato-style restaurant order dataset.
You will see exactly how dirty data degrades model performance,
and how cleaning it step by step improves accuracy from 73% to 82%.

---

## Prerequisites

Python 3.7 or higher installed on your machine.

---

## Setup

### Step 1: Create your project folder

```
mkdir data-cleaning-lab
cd data-cleaning-lab
```

### Step 2: Install required libraries

```
pip install pandas scikit-learn numpy
```

### Step 3: Download the lab file

Copy data_cleaning_lab.py from this repository into your project folder.

### Step 4: Run it

```
python data_cleaning_lab.py
```

---

## What the Code Does, Step by Step

### Step 0: Inspect the Dirty Data

Before touching anything, always look at what you have.

The script prints the raw dataset showing all the problems:

- ORD002 appears twice (duplicate)
- C008 customer_id is missing (null)
- delivery_time of 999 mins (impossible outlier)
- order_amount is missing for one row
- will_reorder has 11 different formats for a simple yes/no field

This is normal. Real data almost always looks like this.

---

### Step 1: Remove Duplicates

```python
clean_data = dirty_data.drop_duplicates(subset=["order_id"])
```

We tell pandas: if two rows have the same order_id, keep only the first one.

Result: 19 rows becomes 18 rows. One duplicate removed.

---

### Step 2: Standardize Inconsistent Formats

```python
yes_values = {"yes", "1", "y", "true"}
clean_data["will_reorder"] = clean_data["will_reorder"].apply(
    lambda x: 1 if str(x).strip().lower() in yes_values else 0
)
```

We convert every variation of yes (Yes, YES, Y, 1, True) to 1
and every variation of no (No, NO, N, 0, False) to 0.

Before: 11 unique formats
After: just 0 and 1

---

### Step 3: Handle Outliers

```python
clean_data["delivery_time_mins"] = clean_data["delivery_time_mins"].clip(upper=120)
```

The 999 minute delivery time is clearly a data entry error.
No restaurant delivers in 16 hours. We cap at 120 minutes.

Before mean: 88.2 mins (dragged up by the 999 outlier)
After mean:  36.5 mins (now realistic)

---

### Step 4: Handle Missing Values

Three different strategies used here:

Drop the row when the missing value is critical and cannot be estimated:
```python
clean_data = clean_data.dropna(subset=["customer_id"])
```

Fill with median when we can make a reasonable estimate:
```python
median_delivery = clean_data["delivery_time_mins"].median()
clean_data["delivery_time_mins"] = clean_data["delivery_time_mins"].fillna(median_delivery)
```

We use median rather than mean because median is not affected by outliers.

---

### Step 5: Feature Engineering

We create three new columns from the data we already have:

```python
clean_data["is_fast_delivery"] = (clean_data["delivery_time_mins"] < 30).astype(int)
clean_data["is_high_value"]    = (clean_data["order_amount"] > 400).astype(int)
clean_data["is_high_rated"]    = (clean_data["rating"] >= 4.0).astype(int)
```

These binary features are often more useful to a model than the raw numbers.
A model finds it easier to learn from is_fast_delivery (0 or 1)
than from raw delivery_time_mins (22 to 120).

---

### The Proof

The script trains the exact same Logistic Regression model twice:
once on dirty data, once on clean data.

Results:
- Dirty data accuracy: 73.3%
- Clean data accuracy: 82.4%
- Improvement: +9.0%

Same algorithm. Same model. Different data quality. Different results.

---

## Experiments to Try

### Experiment 1: Add more dirty data problems

Add five more rows with various problems and see if accuracy drops:
- More duplicates
- More missing values
- More outliers
- Conflicting labels

### Experiment 2: Try different outlier strategies

Instead of capping at 120, try removing the outlier row entirely:
```python
clean_data = clean_data[clean_data["delivery_time_mins"] <= 120]
```

Does accuracy change?

### Experiment 3: Engineer more features

Try adding these engineered features and see if accuracy improves:
```python
clean_data["amount_per_min"] = clean_data["order_amount"] / clean_data["delivery_time_mins"]
clean_data["is_budget_order"] = (clean_data["order_amount"] < 250).astype(int)
```

---

## Key Takeaways

1. Real-world data is almost always messy. This is not a mistake, it is the norm.

2. Data cleaning always comes before model building. There are no shortcuts.

3. The five most common problems are:
   - Missing values
   - Duplicates
   - Inconsistent formats
   - Outliers
   - Wrong labels

4. Data scientists spend 60 to 80 percent of their time on this.
   Not on algorithms. Not on models. On data.

5. Garbage-In, Garbage-Out: no algorithm can save you from bad data.

---

## Next Module

Module 1.4: The ML Taxonomy

We will explore Supervised vs Unsupervised Learning
and understand when to use which approach.
