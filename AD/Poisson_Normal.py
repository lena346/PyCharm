import numpy as np

l = 4
k = 10**3
X = np.random.poisson(l, k)

m = 4000
o = 144.5
Y = np.random.normal(m, o, k)

X_Y = X * Y
E_X_Y = X_Y.mean()
print(E_X_Y, (sum(map(lambda x: (x - E_X_Y) ** 2, X_Y)) / k) ** 0.5)