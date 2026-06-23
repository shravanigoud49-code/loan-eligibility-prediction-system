import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier



np.random.seed(42)

n = 500

age = np.random.randint(21, 60, n)
income = np.random.randint(20000, 150000, n)
credit_score = np.random.randint(500, 850, n)
loan_amount = np.random.randint(50000, 500000, n)

loan_status = []

for i in range(n):
    if (
        income[i] >= 50000
        and credit_score[i] >= 650
        and loan_amount[i] <= income[i] * 5
    ):
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



def predict_loan():
    try:
        age_val = int(age_entry.get())
        income_val = int(income_entry.get())
        credit_val = int(credit_entry.get())
        loan_val = int(loan_entry.get())

        customer = [[age_val, income_val, credit_val, loan_val]]

        prediction = model.predict(customer)

        if prediction[0] == 1:
            result_label.config(
                text="✅ LOAN APPROVED",
                fg="green"
            )
        else:
            result_label.config(
                text="❌ LOAN REJECTED",
                fg="red"
            )

    except:
        messagebox.showerror(
            "Error",
            "Please enter valid numeric values."
        )

# ==========================
# GUI WINDOW
# ==========================

root = tk.Tk()
root.title("Loan Eligibility Predictor")
root.geometry("600x500")
root.configure(bg="#E8F0FE")

title = tk.Label(
    root,
    text="🏦 Loan Eligibility Approval Predictor",
    font=("Arial", 18, "bold"),
    bg="#E8F0FE",
    fg="#1A237E"
)
title.pack(pady=20)

tk.Label(
    root,
    text="Age",
    font=("Arial", 12),
    bg="#E8F0FE"
).pack()

age_entry = tk.Entry(root, width=30)
age_entry.pack(pady=5)

tk.Label(
    root,
    text="Annual Income",
    font=("Arial", 12),
    bg="#E8F0FE"
).pack()

income_entry = tk.Entry(root, width=30)
income_entry.pack(pady=5)


tk.Label(
    root,
    text="Credit Score",
    font=("Arial", 12),
    bg="#E8F0FE"
).pack()

credit_entry = tk.Entry(root, width=30)
credit_entry.pack(pady=5)


tk.Label(
    root,
    text="Loan Amount",
    font=("Arial", 12),
    bg="#E8F0FE"
).pack()

loan_entry = tk.Entry(root, width=30)
loan_entry.pack(pady=5)


predict_btn = tk.Button(
    root,
    text="Check Eligibility",
    font=("Arial", 12, "bold"),
    bg="#1976D2",
    fg="white",
    command=predict_loan
)
predict_btn.pack(pady=20)


result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#E8F0FE"
)
result_label.pack(pady=20)


footer = tk.Label(
    root,
    text="AI-Based Loan Approval System",
    font=("Arial", 10),
    bg="#E8F0FE",
    fg="gray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()