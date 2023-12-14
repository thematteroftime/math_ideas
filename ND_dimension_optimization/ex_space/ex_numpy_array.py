import numpy as np

a = np.array([[1, 2, 3]])
I = np.eye(3)
b = np.array([1, 2, 3])

print(np.dot(I, a.T))
print(np.dot(I, b))
print(np.dot(I, a.T) == np.dot(I, b))
