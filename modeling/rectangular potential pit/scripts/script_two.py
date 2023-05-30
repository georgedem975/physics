import numpy as np
import matplotlib.pyplot as plt


def get_gamilton(matrix_size, h, m, omega):
    H = np.zeros((matrix_size, matrix_size))
    for i in range(matrix_size):
        H[i, i] = 1 / h ** 2 + 0.5 * m * omega ** 2 * (i * h) ** 2
        if i > 0:
            H[i, i - 1] = -0.5 / h ** 2
            H[i - 1, i] = -0.5 / h ** 2
    return H


def get_graphics(L, N, eigenvectors, eigenvalues, ylabel, title):
    x = np.linspace(-L, L, N)
    for i in range(L):
        plt.plot(x, eigenvectors[:, i], label='n={}; E={}'.format(i, round(eigenvalues[i]), 2))
    plt.legend(title='№ эн. уровня и соотв. собств. значения', loc='upper left')
    plt.xlabel('X')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


if __name__=='__main__':
    m = 1
    omega = 0
    h = 0.01
    L = 3
    N = int(L / h)

    H = get_gamilton(N, h, m, omega)

    eigenvalues, eigenvectors = np.linalg.eigh(H)

    get_graphics(L, N, eigenvectors, eigenvalues, 'Psi', 'график собственной функции')

    for i in range(L):
        print('E_{} = {}'.format(i, eigenvalues[i]))

    eigenvectors = np.abs(eigenvectors) ** 2

    get_graphics(L, N, eigenvectors, eigenvalues, '|Psi|^2', 'график плотности вероятности находения частицы в окрестности точки')

