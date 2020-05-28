import numpy as np

A = np.array([[1, 0, 1], [0, 1, 0]])
B = np.array([[1, 0], [1, 0], [1, 0]])
C = np.dot(A, B)
print(C)
