# credit-risk-model
Credit Scoring Business Understanding
1. Basel II and Model Interpretability

The Basel II Accord emphasizes accurate risk measurement, transparency, and proper documentation in credit risk management. Financial institutions must be able to explain how a credit decision is made and demonstrate that the model is reliable and fair. Therefore, credit scoring models should be interpretable and well documented. Interpretable models help risk managers, auditors, and regulators understand the relationship between customer characteristics and predicted risk. Proper documentation also supports model validation, monitoring, governance, and regulatory compliance.

2. Why a Proxy Variable is Necessary

The provided transaction dataset does not contain a direct default label indicating whether a customer failed to repay a loan. Since supervised machine learning models require a target variable, a proxy variable must be created.

In this project, customer behavior can be analyzed using Recency, Frequency, and Monetary (RFM) metrics. Customers who transact infrequently, spend little, and have not interacted recently may be considered higher risk.

However, proxy targets introduce business risks because they are assumptions rather than actual default outcomes. A customer classified as high risk by the proxy may never default, while a customer classified as low risk could still default. This may lead to incorrect lending decisions, customer exclusion, or inaccurate risk estimates.

3. Trade-offs Between Interpretable and High-Performance Models
Logistic Regression with WoE

Advantages:

Easy to interpret
Regulatory friendly
Transparent decision process
Simple to validate and monitor

Disadvantages:

May fail to capture complex nonlinear relationships
Often produces lower predictive performance
Gradient Boosting Models

Advantages:

High predictive accuracy
Captures complex interactions automatically
Often achieves better risk discrimination

Disadvantages:

Less interpretable
More difficult to explain to regulators
Requires additional tools for explainability
More complex monitoring and validation

In regulated financial environments, organizations often balance predictive performance with explainability. While advanced machine learning models may achieve higher accuracy, interpretable models remain attractive because they support compliance, governance, and trust in credit decisions.
## Task 2 — Exploratory Data Analysis

The dataset was explored to understand transaction behavior, fraud distribution, feature relationships, and data quality.

### Key Findings

- Transaction amounts were highly right-skewed with significant outliers.
- Fraudulent transactions represented only a very small portion of the dataset, indicating severe class imbalance.
- Strong correlations existed among some monetary variables.
- Customer transaction behavior varied substantially across users.
- Temporal transaction patterns suggested potentially useful behavioral signals for downstream modeling.

### Techniques Used

- Summary statistics
- Missing value analysis
- Distribution analysis
- Boxplots
- Correlation heatmaps
- Fraud distribution analysis
- Customer-level aggregation
## Task 3 — Feature Engineering

Customer-level behavioral features were engineered from raw transaction data to prepare the dataset for machine learning.

### Engineered Features

- Transaction frequency
- Average transaction amount
- Total transaction value
- Transaction variability
- Time-based transaction features
- Encoded product and channel features

### Preprocessing Steps

- Datetime feature extraction
- Aggregation by customer
- One-hot encoding
- Numerical feature scaling
## Task 4 — Proxy Target Variable Engineering

Since the dataset did not contain an actual default label, a proxy target variable was created using RFM analysis and clustering techniques.

### RFM Features

The following customer behavioral metrics were generated:

| Feature | Description |
|---|---|
| Recency | Days since last transaction |
| Frequency | Total number of transactions |
| Monetary | Total transaction amount |

### Sample RFM Output

| CustomerId | Recency | Frequency | Monetary |
|---|---|---|---|
| CustomerId_1 | 83 | 1 | -10000 |
| CustomerId_1001 | 89 | 5 | 20000 |
| CustomerId_1002 | 25 | 11 | 4225 |

### Clustering Results

KMeans clustering was applied to segment customers into behavioral groups.

Cluster distribution:

- Cluster 0: 2315 customers
- Cluster 1: 1427 customers
- Cluster 2: 2314 customers

The smaller and behaviorally weaker cluster was selected as the high-risk proxy group.

### Proxy Target Distribution

| Label | Meaning |
|---|---|
| 1 | High Risk |
| 0 | Low Risk |

The generated proxy target variable will be used for downstream supervised credit risk modeling.# Credit Risk Modeling Project

## 📌 Overview

This project builds a credit risk analytics pipeline using transaction data. Since the dataset does not contain actual default labels, a proxy target variable is created using behavioral customer segmentation.

The pipeline includes:
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Proxy Target Creation
- Model Training
- Model Evaluation

---

## 📊 Task 2 — Exploratory Data Analysis

### Key Insights

- Transaction amounts are highly skewed with extreme outliers
- Fraud data is highly imbalanced
- Strong correlations exist between monetary features
- Customer behavior varies significantly across users
- Temporal patterns provide behavioral signals

---

## ⚙️ Task 3 — Feature Engineering

### Steps Performed

- Extracted time-based features (hour, day, month, weekday)
- Created customer-level aggregated features:
  - Total amount
  - Average amount
  - Transaction count
  - Standard deviation
- Encoded categorical variables
- Scaled numerical features

---

## 🎯 Task 4 — Proxy Target Creation

Since no real default label exists, a proxy target was created using RFM analysis and KMeans clustering.

### RFM Features

- Recency: Time since last transaction
- Frequency: Number of transactions
- Monetary: Total spending

### Clustering

Customers were grouped into 3 clusters using KMeans.

The smaller behavioral segment was selected as the **high-risk group**:

- Cluster 0: 2315 customers  
- Cluster 1: 1427 customers  
- Cluster 2: 2314 customers  

---

## 🤖 Task 5 — Model Training

A baseline Logistic Regression model was trained using engineered features.

### Steps:
- Train-test split
- Model fitting
- Prediction generation

---

## 📈 Task 6 — Model Evaluation

### Metrics Used:
- Confusion Matrix
- Precision, Recall, F1-score
- ROC-AUC Score