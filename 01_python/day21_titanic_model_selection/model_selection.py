import pandas as pd

from sklearn.model_selection import(
    train_test_split,
    cross_val_score,
    GridSearchCV
)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

import joblib

df = pd.read_csv('data/titanic.csv')

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

df = pd.get_dummies(
    df,
    columns=['Sex', 'Embarked'],
    drop_first=True
)

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

logistic_model = Pipeline(
    [
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(max_iter=1000))
    ]
)

tree_model = DecisionTreeClassifier(random_state=42)

forest_model = RandomForestClassifier(random_state=42)

logistic_model.fit(
    X_train,
    y_train
)

tree_model.fit(
    X_train,
    y_train
)

forest_model.fit(
    X_train,
    y_train
)



logistic_pred = logistic_model.predict(
    X_test
)

tree_pred = tree_model.predict(
    X_test
)

forest_pred = forest_model.predict(
    X_test
)



logistic_accuracy = accuracy_score(
    y_test,
    logistic_pred
)

tree_accuracy = accuracy_score(
    y_test,
    tree_pred
)

forest_accuracy = accuracy_score(
    y_test,
    forest_pred
)

# print(
#     "Logistic Regression Accuracy:",
#     logistic_accuracy
# )

# print(
#     "Decision Tree Accuracy:",
#     tree_accuracy
# )

# print(
#     "Random Forest Accuracy:",
#     forest_accuracy
# )


logistic_scores = cross_val_score(
    logistic_model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

tree_scores = cross_val_score(
    tree_model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

forest_scores = cross_val_score(
    forest_model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

# print(
#     "Logistic Regression CV:",
#     logistic_scores
# )

# print(
#     "Decision Tree CV:",
#     tree_scores
# )

# print(
#     "Random Forest CV:",
#     forest_scores
# )

# print(
#     "Logistic Regression Mean:",
#     logistic_scores.mean()
# )

# print(
#     "Decision Tree Mean:",
#     tree_scores.mean()
# )

# print(
#     "Random Forest Mean:",
#     forest_scores.mean()
# )

param_grid = {
    'n_estimators':[
        50,
        100,
        200
    ],
    'max_depth':[
        None,
        5,
        10
    ],
    'min_samples_split':[
        2,
        5,
        10
    ]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy'
)

grid_search.fit(X_train, y_train)

print(
    "最佳参数:",
    grid_search.best_params_
)

print(
    "最佳交叉验证分数:",
    grid_search.best_score_
)

best_model = grid_search.best_estimator_

best_pred = best_model.predict(
    X_test
)

best_accuracy = accuracy_score(
    y_test,
    best_pred
)

print(
    "调优后测试集准确率:",
    best_accuracy
)

joblib.dump(
    best_model,
    "models/best_titanic_model.pkl"
)

print(
    "最佳模型保存成功！"
)