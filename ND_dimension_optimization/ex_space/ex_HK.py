import numpy as np

a = np.array([[0.125, 0.005208333333333333], [0.005208333333333333, 1.0002170138888888]])
b = np.array([[-0.0416666666880019], [1.0]])
c = np.array([[1,3],[2,5]])
d = np.array([[2],[7]])
print(-np.dot(a, b))
print(np.dot(c,d))
