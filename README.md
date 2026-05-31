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