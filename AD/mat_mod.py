import numpy as np
P = np.array([
    [0.4,0.3,0.3],
    [0.2,0.5,0.3],
    [0.1,0.2,0.7]
]
)

#1
n = 2
total_1 = np.linalg.matrix_power(P,n)
print(total_1, end='   ')




