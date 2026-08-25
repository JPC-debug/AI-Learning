import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score

import joblib

df = pd.read_csv('data/students.csv')

print(df)

X = df[
    [
        'study_hours',
        'attendance',
        'homework'
    ]
]

y = df['pass']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

model.fit(X_train, y_train)

# 交叉验证

scores = cross_val_score(
    model,
    X,
    y,
    cv=4
)


print(
    "Cross Validation Scores:",
    scores
)


print(
    "Average Score:",
    scores.mean()
)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(
    "Accuracy:",
    accuracy
)

joblib.dump(model,'models/student_model.pkl')
print('模型保存成功！')