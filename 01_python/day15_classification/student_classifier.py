import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score

df = pd.read_csv('students.csv')

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
    test_size=0.2,
    random_state=42
)

model = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

model.fit(
    X_train,
    y_train
)

y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("预测结果:")
print(y_pred)

print("\n真实结果:")
print(y_test.values)

print("\nAccuracy:")
print(accuracy)

new_student = pd.DataFrame(
    {
        'study_hours':[5],
        'attendance':[90],
        'homework':[95]
    }
)

prediction = model.predict(new_student)

print("\n新学生预测:")
print(prediction)

probability = model.predict_proba(new_student)

print("\n预测概率:")
print(probability)