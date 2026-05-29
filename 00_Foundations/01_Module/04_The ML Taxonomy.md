# Module 1.4: The ML Taxonomy

## CONTEXT: The Zoo Problem

Imagine you are the head of data science at Amazon India. Your CEO walks in and gives you three completely different problems to solve this week:

**Problem 1:** "We have 10 million product photos with labels (shirt, shoes, electronics). Build something that correctly tags new photos automatically."

**Problem 2:** "We have purchase history of 50 million customers but zero idea how to group them. Find the natural customer groups hiding in this data."

**Problem 3:** "Build a system that teaches itself to price products optimally. It should try different prices, see what sells, and keep getting smarter."

You sit down to build three models. Then you realize something important. These three problems are fundamentally different in nature. Not just in data. In the very type of learning required.

This is why the ML Taxonomy exists. It is a map that tells you which type of learning fits which type of problem, before you write a single line of code.

---

## CONCEPT: The Three Types of Machine Learning

Here is the big picture first, then we go deep on each.

<img width="1440" height="680" alt="image" src="https://github.com/user-attachments/assets/8dccfd86-11f3-431b-b4bd-449ee5de1b0b" />



Now let us go deep on each type, starting with the one you will use most often.

---

## CONCEPT: Supervised Learning

### The Core Idea

The name says it all. You are supervising the learning by providing the correct answers.

Think of it like a student preparing for an exam using a solved question bank. Every question comes with the correct answer already written. The student studies the patterns in how questions relate to their answers, then applies those patterns to new, unseen questions.

In ML terms: you provide data where every input already has a label (the correct answer). The model learns the relationship between inputs and labels, then predicts labels for new inputs it has never seen.

**The defining question: Do you have labeled data?**
If yes, supervised learning is your starting point.

### Real-World Example: Zomato Delivery Time Prediction

Zomato wants to show customers an accurate "arrives in X minutes" estimate.

**Training data they have (labeled):**

```
distance_km | restaurant_prep_mins | time_of_day | weather | actual_delivery_mins
2.1         | 12                   | lunch_rush  | clear   | 28
5.4         | 8                    | off_peak    | clear   | 41
1.2         | 20                   | dinner_rush | rain    | 35
3.8         | 15                   | off_peak    | clear   | 32
```

The model learns: "When distance is short AND prep time is low AND weather is clear, delivery tends to be 25-30 minutes. When it is raining AND dinner rush, add 15 minutes."

Now when a new order comes in, it predicts accurately without any human writing those rules.

### Two Tasks Inside Supervised Learning

Supervised learning splits into two fundamentally different tasks. The difference is in the type of answer you are predicting.

**Regression: Predicting a number on a continuous scale**

You are not predicting a category. You are predicting an actual numeric value.

Real examples:
- "How many minutes until delivery?" (28, 41, 35...)
- "What will this flat in Mumbai cost?" (85 lakhs, 1.2 crore, 68 lakhs...)
- "How many tickets will BookMyShow sell for this concert?" (12,000, 45,000...)
- "What will Nifty50 close at tomorrow?" (numerical prediction)

**Classification: Predicting which category something belongs to**

You are not predicting a number. You are predicting a label from a fixed set of options.

Real examples:
- "Is this email spam or not spam?" (two categories)
- "Which cuisine type is this restaurant?" (Indian, Chinese, Italian, Mexican...)
- "Will this loan applicant default?" (yes or no)
- "Which product category does this image show?" (electronics, clothing, food...)

The diagram below makes this distinction crystal clear:


<img width="1440" height="640" alt="image" src="https://github.com/user-attachments/assets/506a1e2b-1966-4aa4-ac9d-a9f7999fe7ff" />



The one question that tells you which to use: **"Is my answer a number I could put on a ruler, or a category from a fixed list?"**

Number on a ruler (28 minutes, 94.5 lakhs, 24,782) = Regression.
Category from a list (spam, Indian cuisine, will default) = Classification.

---

## CONCEPT: Unsupervised Learning

### The Core Idea

Here there are no correct answers to learn from. No labels. No teacher.

You hand the machine raw data and say: "I do not know what groups or patterns exist. You figure it out."

The machine finds natural structure hiding in the data on its own.

### Real-World Example: Paytm Customer Segmentation

Paytm has 300 million users. They want to run personalized marketing campaigns. But nobody has sat down and labeled each customer as "premium user" or "occasional user" or "high-fraud-risk user." There are too many customers and the categories are not predefined.

So they run an unsupervised clustering algorithm on behavioral data:
- How often does the user transact per month?
- What is the average transaction value?
- What categories do they spend in (bills, food, travel)?
- What time of day do they transact?
- How many times have they failed payment verification?

The algorithm runs. Nobody told it what groups to look for. It discovers on its own:

**Cluster 1:** High-frequency, small transactions, mostly mobile recharge and food ordering. The algorithm surfaces these. Humans then label them: "Daily convenience users."

**Cluster 2:** Low-frequency, very high-value transactions, mostly travel and electronics. Humans label them: "Premium occasional users."

**Cluster 3:** New accounts, erratic behavior, unusual transaction times, multiple failed verifications. Humans label them: "High-risk accounts."

The machine found the groups. Humans named them afterward.

### Why This Matters

Without unsupervised learning, Paytm would need a human analyst to manually review 300 million accounts and assign each one a segment. That is impossible.

With unsupervised learning, the algorithm does it automatically and can do it again every week as user behavior evolves.

---

## CONCEPT: Reinforcement Learning

### The Core Idea

Reinforcement Learning is the most different of the three. There is no dataset at all. The model learns by actually doing things in an environment and receiving feedback on whether each action was good or bad.

The best analogy is how humans learn to ride a bicycle. Nobody handed you a labeled dataset of "lean left is good, lean right is bad." You just got on the bike, fell, adjusted, fell less, adjusted again, and gradually learned the policy that keeps you balanced.

That iterative loop of action, outcome, and adjustment is exactly what reinforcement learning does.

### Real-World Example: YouTube Recommendation Engine

Here is how YouTube uses reinforcement learning to keep you watching.

The "agent" (the RL model) takes "actions" (recommending a video). The "environment" is your behavior. The "reward" is whether you watch the video, skip it, or close the app.

**The learning loop:**

Recommend Video A → You watch 80% of it → Positive reward (good recommendation)
Recommend Video B → You watch 5% and close app → Negative reward (bad recommendation)
Recommend Video C → You watch all of it AND click the next recommendation → Strong positive reward

Over billions of such interactions, YouTube's RL model learns the exact policy that maximizes watch time. Not from a predefined dataset. From the consequences of its own actions.

This is also why YouTube is so compelling. The model has been trained by billions of real human interactions to know exactly what to show you next to keep you engaged.


---

## CONCEPT: Putting It All Together with Amazon

Let us return to the three Amazon problems from the beginning and now classify them properly:

**Problem 1: Tag product photos automatically**
- Do we have labeled data? Yes. 10 million photos already tagged.
- What type of answer? A category from a fixed list (shirt, shoes, electronics).
- Answer: Supervised Learning, Classification.

**Problem 2: Find natural customer groups**
- Do we have labeled data? No. Zero predefined segments.
- Answer: Unsupervised Learning, Clustering.

**Problem 3: Price products optimally**
- Static dataset? No. The model needs to try prices, see results, and adapt.
- Answer: Reinforcement Learning.

Three problems. Three different ML types. Each perfectly matched to the nature of the problem.

This matching skill is what separates a good ML practitioner from someone who just knows algorithms.

---

## LAB: Seeing All Three Types in Action

Now we will run all three ML types on real data side by side so students can feel the difference concretely.All four parts run perfectly. Now let us copy everything to outputs:---

# Module 1.4 Complete

## What We Built

**CONTEXT:** The Amazon three-problems story showing why different problems require fundamentally different types of learning.

**CONCEPT:** Three diagrams plus detailed explanations:
- Full ML taxonomy tree (interactive, clickable)
- Regression vs Classification side-by-side with real examples
- Interactive decision tool where students answer 2 questions and get the right ML type instantly

**LAB:** One script, four live ML demonstrations all on the same Paytm customer dataset:
- Regression: predicts monthly spend with 2.9 unit average error
- Classification: detects fraud at 87.5% accuracy
- Clustering: discovers 3 customer groups (Power users, Casual users, High-risk)
- Reinforcement: a bandit agent learns the best cashback offer through trial

---

## Course Progress: Section 1

| Module | Status |
|---|---|
| 1.1 The Traditional Programming Problem | Done |
| 1.2 The Machine Learning Paradigm | Done |
| 1.3 Data as the New Code | Done |
| 1.4 The ML Taxonomy | Done |
| 1.5 Two Fundamental Tasks | Next |

