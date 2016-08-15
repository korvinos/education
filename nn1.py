import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([0.30, 0.35, 0.40, 0.50, 0.60, 0.80, 0.95, 1.10])
y = np.array([1.60, 1.40, 1.40, 1.60, 1.70, 2.00, 1.70, 2.10])

n = len(y)

# Ordinary Least Squares
m_OLS = (n*sum(x * y) - sum(x) * sum(y))/(n * sum(x ** 2) - sum(x) ** 2)
c_OLS = (np.sum(y) - m_OLS * np.sum(x)) / n
OLS = m_OLS * x + c_OLS

# Neural Network
m_NN, c_NN = 0.5, 0.5
nu = 0.001
NN = m_NN * x + c_NN
e2 = np.sum((OLS - NN) ** 2)
e1 = e2 + 1
step = 1
all_e2 = []

while e2 < e1:
    for i in range(0, n):
        test = m_NN * x[i] - c_NN
        d = y[i] - test
        dm = nu * x[i] * d
        dc = nu * 1 * d
        m_NN += dm
        c_NN += dc
    NN = m_NN * x + c_NN
    all_e2.append(e2)
    e1 = e2
    e2 = np.sum((OLS - NN) ** 2)
    step += 1



NN = m_NN * x + c_NN

print('REPORT: y = m*x + c',
      '\nCOUNT OF STEPS: ', step,
      '\nOLS: ', 'm: ', round(m_OLS, 4), '/ c: ', round(c_OLS, 4),
      '\nNN: ', 'm: ', round(m_NN, 4), '/ c: ', round(c_NN, 4),
      '\nSUM ERROR: ', round(e2, 4))

plt.figure('results')
plt.plot(x, y, label='data')
plt.plot(x, OLS, label='OLS')
plt.plot(x, NN, label='NN')
plt.legend(loc=0)

plt.figure('error')
plt.plot(all_e2)
plt.show()