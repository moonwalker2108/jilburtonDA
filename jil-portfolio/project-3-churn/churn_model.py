import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

df = pd.read_csv('churn_data_dictionary.csv')
X = df[['age','premium','claims_count','tenure_months']]
y = df['churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=200, max_depth=6)
clf.fit(X_train, y_train)

pred = clf.predict(X_test)
print('F1-score:', f1_score(y_test, pred))