from sympy import *
import matplotlib.pyplot as plt
import numpy as np


def u(a, n, x):
    return 1 / sqrt(a) * sin(pi*n*(x/a + 1))


x = np.linspace(-1, 1, 100)


y1 = [u(1, 1, xi) for xi in x]
y2 = [u(1, 2, xi) for xi in x]
y3 = [u(1, 3, xi) for xi in x]

plt.plot(x, y1, label='n=1')
plt.plot(x, y2, label='n=2')
plt.plot(x, y3, label='n=3')

plt.xlim(-1, 1)
plt.ylim(-1.5, 1.5)

plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid()

plt.show()