from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

X = np.array([
    [2],
    [4],
    [6],
    [8],
    [10]
])

y = np.array([
    58,
    73,
    79,
    92,
    96
])

plt.scatter(X, y)
# plt.xlabel('Study Time')
# plt.ylabel('Score')
# plt.title('Relationship')
# plt.show()


model = LinearRegression()

model.fit(X,y)

y_pred = model.predict(X)
plt.plot(X, y_pred)
plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.title('Study Hours vs Score')
plt.show()


print('系数：',model.coef_)
print('截距：', model.intercept_)

result = model.predict([[12]])

print('预测成绩：', result)

from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y, y_pred)

r2 = r2_score(y, y_pred)

print('MSE:', mse)
print('R2:', r2)
