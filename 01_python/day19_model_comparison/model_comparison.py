import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

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

logistic_model = Pipeline(
    [
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression())
    ]
)

decision_tree_model = DecisionTreeClassifier(random_state=42)

random_forest_model = RandomForestClassifier(random_state=42)

logistic_model.fit(X_train,y_train)
decision_tree_model.fit(X_train, y_train)
random_forest_model.fit(X_train, y_train)

logistic_pred = logistic_model.predict(X_test)
tree_pred = decision_tree_model.predict(X_test)
forest_pred = random_forest_model.predict(X_test)

logistic_accuracy = accuracy_score(y_test, logistic_pred)
tree_accuracy = accuracy_score(y_test, tree_pred)
forest_accuracy = accuracy_score(y_test, forest_pred)

print(
    "Logistic Regression Accuracy:",
    logistic_accuracy
)

print(
    "Decision Tree Accuracy:",
    tree_accuracy
)

print(
    "Random Forest Accuracy:",
    forest_accuracy
)

logistic_scores = cross_val_score(
    logistic_model,
    X,
    y,
    cv=4
)

tree_scores = cross_val_score(
    decision_tree_model,
    X,
    y,
    cv=4
)

forest_scores = cross_val_score(
    random_forest_model,
    X,
    y,
    cv=4
)


print(
    "Logistic Regression CV:",
    logistic_scores
)

print(
    "Decision Tree CV:",
    tree_scores
)

print(
    "Random Forest CV:",
    forest_scores
)


model_scores = {
    "Logistic Regression": logistic_scores.mean(),
    "Decision Tree": tree_scores.mean(),
    "Random Forest": forest_scores.mean()
}

print(
    "模型平均得分:",
    model_scores
)

best_model_name = max(
    model_scores,
    key=model_scores.get
)

best_score = model_scores[best_model_name]
print('最佳模型：', best_model_name)
print('最佳平均分：', best_score)