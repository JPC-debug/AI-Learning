import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

data = {
    "study_hours":[
        1,2,3,4,5,6,7,8,
        2,3,5,6
    ],

    "attendance":[
        50,60,70,75,85,90,95,98,
        65,72,88,92
    ],

    "homework":[
        55,65,75,80,90,95,98,100,
        70,78,92,96
    ],

    "pass":[
        0,0,0,0,1,1,1,1,
        0,0,1,1
    ]
}
df = pd.DataFrame(data)
print(df)

X = df[
    [
        "study_hours",
        "attendance",
        "homework"
    ]
]
y = df["pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


model = LogisticRegression()

model.fit(
    X_train,
    y_train
)

y_pred = model.predict(X_test)
print("预测结果:")
print(y_pred)
print("真实结果:")
print(y_test.values)

accuracy = accuracy_score(
    y_test,
    y_pred
)
print("Accuracy:")
print(accuracy)

cm = confusion_matrix(
    y_test,
    y_pred
)
print('Confusion Matrix:')
print(cm)

report = classification_report(
    y_test,
    y_pred
)
print('Classification Report:')
print(report)

cv_model = LogisticRegression()
scores = cross_val_score(
    cv_model,
    X,
    y,
    cv=5
)
print("Cross Validation Scores:")
print(scores)
print("Average Score:")
print(scores.mean())

import joblib

joblib.dump(
    model,
    'student_model.pkl'
)

print('模型保存成功！')