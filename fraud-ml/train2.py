# train_loan_ml.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
import joblib

# ----------------------------
# 1. Generate synthetic data
# ----------------------------
np.random.seed(42)
n_samples = 5000

# Income in INR/month
income = np.random.normal(loc=50000, scale=20000, size=n_samples).clip(10000, 200000)

# Account balance in INR
balance = np.random.normal(loc=15000, scale=10000, size=n_samples).clip(0, 100000)

# Avg transaction amount
avg_transaction = np.random.normal(loc=2000, scale=1500, size=n_samples).clip(100, 20000)

# Credit score (300-850)
credit_score = np.random.normal(loc=650, scale=100, size=n_samples).clip(300, 850)

# Requested loan amount
requested_amount = np.random.normal(loc=20000, scale=15000, size=n_samples).clip(5000, 100000)

# Eligibility logic (for synthetic ground truth)
eligible = (
    (income > 30000) &
    (balance > 5000) &
    (credit_score > 600) &
    (requested_amount < income * 1.5)
).astype(int)

# Introduce some randomness
flip_indices = np.random.choice(n_samples, size=int(0.1 * n_samples), replace=False)
eligible[flip_indices] = 1 - eligible[flip_indices]

# Combine into DataFrame
data = pd.DataFrame({
    "income": income,
    "balance": balance,
    "avg_transaction": avg_transaction,
    "credit_score": credit_score,
    "requested_amount": requested_amount,
    "eligible": eligible
})

print("Data distribution:\n", data['eligible'].value_counts())

# ----------------------------
# 2. Split dataset
# ----------------------------
X = data.drop("eligible", axis=1)
y = data["eligible"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ----------------------------
# 3. Handle class imbalance with SMOTE
# ----------------------------
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

print("After SMOTE:", pd.Series(y_train_res).value_counts())

# ----------------------------
# 4. Scale features
# ----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_res)
X_test_scaled = scaler.transform(X_test)

# ----------------------------
# 5. Train XGBoost classifier
# ----------------------------
model = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    use_label_encoder=False,
    eval_metric="logloss"
)
model.fit(X_train_scaled, y_train_res)

# ----------------------------
# 6. Evaluate model
# ----------------------------
y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:,1]

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nROC-AUC:", roc_auc_score(y_test, y_prob))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ----------------------------
# 7. Save model and scaler
# ----------------------------
joblib.dump(model, "loan_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("\nModel and scaler saved successfully!")
