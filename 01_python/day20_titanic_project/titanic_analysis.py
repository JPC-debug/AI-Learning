import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report
)

df = pd.read_csv('data/titanic.csv')
# print(df.head())
# print(df.shape)
# print(df.columns)
# df.info()

# print(df.isnull().sum())
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
# print(df.isnull().sum())

df = pd.get_dummies(
    df,
    columns=['Sex', 'Embarked'],
    drop_first=True
)

# print(df.head())
# print(df.columns)

X = df[
    [
        "Pclass",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Sex_male",
        "Embarked_Q",
        "Embarked_S"
    ]
]

y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = Pipeline(
    [
        (
            "scaler",
            StandardScaler()
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000
            )
        )
    ]
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(
    "Accuracy:",
    accuracy
)

print(
    "Confusion Matrix:"
)
print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

print(
    "Classification Report:"
)
print(
    classification_report(
        y_test,
        y_pred
    )
)

scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

print(
    "Cross Validation Scores:",
    scores
)

print(
    "Average CV Accuracy:",
    scores.mean()
)

classifier = model.named_steps["classifier"]

coefficients = classifier.coef_[0]

feature_importance = pd.DataFrame(
    {
        "Feature": X.columns,
        "Coefficient": coefficients
    }
)

feature_importance["Abs_Coefficient"] = (
    feature_importance["Coefficient"].abs()
)

feature_importance = feature_importance.sort_values(
    by="Abs_Coefficient",
    ascending=False
)

print(feature_importance)