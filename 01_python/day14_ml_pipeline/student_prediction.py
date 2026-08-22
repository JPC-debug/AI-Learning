import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('students.csv')

print(df)

X = df[
    [
        # 'study_hours'
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

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)

model = LinearRegression()

model.fit(
    X_train_scaled,
    y_train
)

y_pred = model.predict(
    X_test_scaled
)

print('\n真实成绩：')
print(list(y_test))

print('预测成绩：')
print(y_pred)

print('\nMSE:')
print(
    mean_squared_error(
        y_test,
        y_pred
    )
)

print('\nR2:')
print(
    r2_score(
        y_test,
        y_pred
    )
)