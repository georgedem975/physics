import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def u2(a, b, x):
    return -1 / np.sqrt(a * (1 - np.sin(2 * b) / (2 * b))) * np.sin(b * np.abs(x) / a - 1)


om = [0, 1 / 4, 1 / 2, 1, 2, 4]

n = 5

kna = np.zeros((len(om), n))

for i in range(len(om)):
    for j in range(n):
        f = lambda k: k / np.tan(k) + om[i]
        k0 = (j + 0.5) * np.pi
        kna[i, j] = fsolve(f, k0)[0]


for j in range(n):
    b = kna[:, j]
    print(b)
    plt.plot(b, drawstyle='steps-pre')

plt.title('Eigenvalues for even solutions')
plt.show()