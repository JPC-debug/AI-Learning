import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

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

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

param_grid = {
    'classifier__C':[
        0.01,
        0.1,
        1,
        10,
        100
    ]
}

grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=4
)

grid_search.fit(
    X_train,
    y_train
)

print(
    '最佳参数：',
    grid_search.best_params_
)

print(
    '最佳交叉验证分数：',
    grid_search.best_score_
)

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)
accuracy = accuracy_score(
    y_test,
    y_pred
)
print(
    '测试集准确率：',
    accuracy
)

import joblib

joblib.dump(
    best_model,
    'best_student_model.pkl'
)

print('最佳模型保存成功！')