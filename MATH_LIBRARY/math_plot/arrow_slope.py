import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

PI = np.pi
fig, ax = plt.subplots(figsize=(16, 9), dpi=80, layout="constrained")
X, Y = np.meshgrid(np.arange(0, 2 * PI, 0.2), np.arange(0, 2 * PI, 0.2))
U = np.cos(X)
V = np.sin(Y)
Q = ax.quiver(X, Y, U, V, units="width")
qk = ax.quiverkey(Q, 0.98, 0.98, 2, r'$2 \frac{m}{s}$', labelpos='E',
                  coordinates='figure')
plt.show()
