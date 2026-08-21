from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [50],
    [70],
    [90],
    [110],
    [130]
])

y = np.array([
    150,
    200,
    260,
    310,
    380
])

model = LinearRegression()

model.fit(X, y)
print('系数：',model.coef_)
print('截距：',model.intercept_)
result = model.predict([[150]])

print(result)

from sklearn.metrics import mean_squared_error, r2_score
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print('MSE:', mse)
print('R2:', r2)

plt.scatter(X, y)

plt.plot(X, y_pred)
plt.xlabel('Size')
plt.ylabel('Price')
plt.title('Size vs Price')
plt.show()