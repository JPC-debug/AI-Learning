import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('students.csv')

X = df[
    [
        'study_hours',
        'attendance',
        'homework'
    ]
]

y = df['score']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

pipeline = Pipeline(
    [
        ('scaler', StandardScaler()),

        ('model', LinearRegression())
    ]
)

pipeline.fit(
    X_train,
    y_train
)

y_pred = pipeline.predict(
    X_test
)

print('真实成绩：')
print(list(y_test))

print('预测成绩：')
print(y_pred)

print('MSE:')
print(
    mean_squared_error(
        y_test,
        y_pred
    )
)

print('R2:')
print(
    r2_score(
        y_test,
        y_pred
    )
)