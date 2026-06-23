import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Generate dataset
np.random.seed(42)

n = 500

age = np.random.randint(21, 60, n)
income = np.random.randint(20000, 150000, n)
credit_score = np.random.randint(500, 850, n)
loan_amount = np.random.randint(50000, 500000, n)

loan_status = []

for i in range(n):
    if income[i] >= 50000 and credit_score[i] >= 650 and loan_amount[i] <= income[i] * 5:
        loan_status.append(1)
    else:
        loan_status.append(0)

df = pd.DataFrame({
    "Age": age,
    "Income": income,
    "CreditScore": credit_score,
    "LoanAmount": loan_amount,
    "Loan_Status": loan_status
})

X = df[["Age", "Income", "CreditScore", "LoanAmount"]]
y = df["Loan_Status"]

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X, y)

def predict_loan(age, income, credit_score, loan_amount):
    result = model.predict([[age, income, credit_score, loan_amount]])
    return result[0]