import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_scorepy churn_model.py

df = pd.DataFrame({
    'age': [45, 60, 30, 50, 70, 38, 62, 41, 55, 29],
    'premium': [200, 400, 150, 300, 500, 220, 450, 280, 390, 180],
    'claims_count': [1, 3, 0, 2, 4, 1, 3, 2, 2, 0],
    'tenure_months': [12, 6, 24, 18, 3, 15, 8, 20, 10, 30],
    'churn': [0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
})

X = df[['age','premium','claims_count','tenure_months']]
y = df['churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=200, max_depth=6)
clf.fit(X_train, y_train)

pred = clf.predict(X_test)
print('F1-score:', f1_score(y_test, pred))

# -----------------------------
# Sample Prediction Demo
# -----------------------------

# Create a sample patient (use same columns as your model)
sample_patient = pd.DataFrame([{
    'age': 67,
    'premium': 450,
    'claims_count': 3,
    'tenure_months': 6
}])

# Get prediction (0 or 1)
prediction = clf.predict(sample_patient)[0]

# Get probability
probability = clf.predict_proba(sample_patient)[0][1]

# Convert to readable label
risk_level = "High" if prediction == 1 else "Low"

print("\n--- Sample Prediction Demo ---")
print("Patient Profile:")
print(sample_patient.to_string(index=False))

print(f"\nPredicted Churn Risk: {risk_level}")
print(f"Churn Probability: {probability:.2%}")
