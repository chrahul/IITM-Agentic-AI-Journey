# Week 12 Graded Mini Project

## Understanding the Assignment and Solution Design

---

# 1. Assignment Overview

The objective of this project is to design and implement a Goal-Oriented Multi-Agent System using CrewAI.

The system should demonstrate how multiple AI agents collaborate to solve a real-world business problem by:

* Performing specialized tasks
* Passing information between agents
* Making decisions based on business rules
* Escalating high-risk situations when necessary

The focus of this assignment is not only on code implementation but also on demonstrating proper agent architecture, collaboration logic, and realistic business workflows.

---

# 2. What The Evaluator Is Looking For

The grading rubric focuses on five major areas:

## 2.1 Agent Design & Role Clarity (25 Marks)

Each agent must:

* Have a clear purpose
* Have a clearly defined input
* Produce a clearly defined output
* Avoid overlapping responsibilities

The evaluator should easily understand:

"What exactly does this agent do?"

---

## 2.2 Multi-Agent Collaboration Logic (25 Marks)

Agents must depend on each other.

Bad Example:

Agent A answers independently.

Agent B answers independently.

Agent C answers independently.

Good Example:

Agent A classifies a request.

Agent B uses Agent A's output.

Agent C uses Agent B's output.

Agent D decides whether escalation is required.

This creates a real collaboration workflow.

---

## 2.3 Industry Realism & Complexity (20 Marks)

The workflow should resemble a real business environment.

The project should include:

* Business policies
* Risk considerations
* Edge cases
* Escalation scenarios

The workflow should not look like a toy example.

---

## 2.4 Tool Use & Decision Making (15 Marks)

The system must demonstrate:

* Decision making
* Rule evaluation
* Risk assessment
* Escalation logic

The evaluator should clearly see:

"Why was this case escalated?"

and

"Why was this case resolved automatically?"

---

## 2.5 Code Structure & Readability (15 Marks)

Code should be:

* Modular
* Well organized
* Easy to understand
* Properly commented

Outputs should be clearly displayed.

---

# 3. Selected Industry Domain

## Banking & Financial Services

### Problem Statement

Banks receive thousands of customer requests every day related to:

* Failed transactions
* Loan inquiries
* Debit card issues
* Credit card issues
* Fraud reports
* Suspicious account activity

Some requests can be resolved automatically.

Others require escalation because they involve:

* Financial risk
* Security concerns
* Fraud investigation

The objective is to build a Multi-Agent Banking Resolution System that handles customer requests and determines whether escalation is necessary.

---

# 4. Proposed Multi-Agent Architecture

The solution will use four collaborating agents.

---

## Agent 1: Intent Classification Agent

### Goal

Understand the customer's request.

### Input

Customer Query

### Output

Intent Category

Examples:

* Fraud
* Transaction Issue
* Loan Inquiry
* Card Problem
* General Inquiry

### Responsibility

Only classify the request.

No policy decisions.

No resolution generation.

---

## Agent 2: Banking Policy Agent

### Goal

Determine applicable banking policies.

### Input

Customer Query

Intent Category

### Output

Relevant Policy Information

Examples:

* Fraud Handling Policy
* Loan Eligibility Policy
* Card Replacement Policy

### Responsibility

Interpret business rules and policies.

---

## Agent 3: Resolution Agent

### Goal

Generate a customer resolution.

### Input

Intent Category

Policy Information

### Output

Draft Resolution

Examples:

* Transaction status explanation
* Loan guidance
* Card replacement instructions

### Responsibility

Provide the recommended response.

---

## Agent 4: Risk & Escalation Agent

### Goal

Evaluate risk and determine escalation.

### Input

Intent Category

Policy Information

Draft Resolution

### Output

* Risk Level
* Escalation Decision
* Final Recommendation

### Responsibility

Determine whether human intervention is required.

---

# 5. Agent Collaboration Flow

The workflow follows a dependency chain.

Customer Query

↓

Intent Classification Agent

↓

Banking Policy Agent

↓

Resolution Agent

↓

Risk & Escalation Agent

↓

Final Decision

Each agent depends on the output produced by the previous agent.

This satisfies the multi-agent collaboration requirement.

---

# 6. Escalation Logic

The system will classify requests into three risk levels.

---

## Low Risk

Examples:

* Account statement request
* EMI information
* General loan inquiry

Action:

Auto Resolve

---

## Medium Risk

Examples:

* Failed transaction
* Duplicate payment
* Loan rejection inquiry

Action:

Conditional Escalation

---

## High Risk

Examples:

* Unauthorized transaction
* Stolen card
* Suspicious account activity
* Possible fraud

Action:

Immediate Escalation

---

# 7. Sample Test Cases

## Test Case 1

Customer Query:

"I want to know my loan eligibility."

Expected Result:

Intent: Loan Inquiry

Risk Level: Low

Escalation: No

---

## Test Case 2

Customer Query:

"My debit card payment failed."

Expected Result:

Intent: Transaction Issue

Risk Level: Medium

Escalation: Conditional

---

## Test Case 3

Customer Query:

"I noticed a ₹50,000 transaction that I never authorized."

Expected Result:

Intent: Fraud

Risk Level: High

Escalation: Yes

---

## Test Case 4

Customer Query:

"My account appears hacked."

Expected Result:

Intent: Fraud

Risk Level: Critical

Escalation: Immediate

---

# 8. CrewAI Implementation Plan

The implementation will include:

1. Agent Definitions
2. Task Definitions
3. Crew Definition
4. Sequential Workflow
5. Escalation Logic
6. Test Execution
7. Output Display

The notebook will demonstrate complete end-to-end execution for all test scenarios.

---

# 9. Expected Outcome

The final system should:

* Classify banking requests accurately
* Apply banking policies consistently
* Generate customer responses
* Evaluate risk levels
* Escalate high-risk cases
* Demonstrate clear agent collaboration

This architecture directly aligns with all grading criteria and demonstrates a realistic enterprise multi-agent workflow.

---

# 10. Conclusion

This project demonstrates how a goal-oriented multi-agent system can be applied to a real banking environment.

The design focuses on:

* Clear agent responsibilities
* Structured agent collaboration
* Decision-making logic
* Risk assessment
* Escalation handling

The solution showcases practical use of CrewAI for enterprise business automation while maintaining safety, compliance, and operational efficiency.
