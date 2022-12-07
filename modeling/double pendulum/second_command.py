import numpy as np
import sympy as smp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter
import decimal


class DoublePendulum:

    def __init__(self):
        self.l1 = 10
        self.l2 = 10
        self.m1 = 12
        self.m2 = 8
        self.theta1 = 40
        self.theta2 = 15
        self.theta1_ = 0
        self.theta2_ = 0
        self.g = 9.8


    def get_coordinates(self, t):
        numerator = (-self.g*(2*self.m1+self.m2)*math.sin(self.theta1) - self.m2*self.g*math.sin(self.theta1-2*self.theta2) - 2*math.sin(self.theta1-self.theta2)*self.m2*((self.theta2_**2)*self.l2+(self.theta1_**2)*self.l1*math.cos(self.theta1-self.theta2)))
        denominator = (self.l1*(2*self.m1+self.m2-self.m2*math.cos(2*self.theta1-2*self.theta2)))

        theta1__ = numerator / denominator

        numerator = (2*math.sin(self.theta1-self.theta2)*((self.theta1_**2)*self.l1*(self.m1+self.m2)+self.g*(self.m1+self.m2)*math.cos(self.theta1)+(self.theta2_**2)*self.l2*self.m2*math.cos(self.theta1-self.theta2)))
        denominator = (self.l2*(2*self.m1+self.m2-self.m2*math.cos(2*self.theta1-2*self.theta2)))

        theta2__ = numerator / denominator

        x1 = self.l1 * math.sin(self.theta1)
        y1 = -self.l1 * math.cos(self.theta1)

        x2 = x1 + self.l2 * math.sin(self.theta2)
        y2 = y1 - self.l2 * math.cos(self.theta2)

        self.theta1 += self.theta1_
        self.theta2 += self.theta2_

        self.theta1_ += theta1__
        self.theta2_ += theta2__

        return [
            x1,
            y1,
            x2,
            y2,
        ]



plt.style.use('ggplot')

t = np.arange(0., 10, 1)

double_pendulum = DoublePendulum()

x = np.sin(t)
arr_x1 = []
arr_y1 = []
arr_x2 = []
arr_y2 = []



for i in t:
    mass = double_pendulum.get_coordinates(t)
    arr_x1.append(mass[0])
    arr_y1.append(mass[1])
    arr_x2.append(mass[2])
    arr_y2.append(mass[3])


plt.subplot(2, 2, 1)
plt.plot(t, np.array(arr_x1))
plt.title('уравнение движения координаты х1')

plt.subplot(2, 2, 2)
plt.plot(t, np.array(arr_y1))
plt.title('уравнение движения координаты y1')

plt.subplot(2, 2, 3)
plt.plot(t, np.array(arr_x2))
plt.title('уравнение движения координаты х2')

plt.subplot(2, 2, 4)
plt.plot(t, np.array(arr_y2))
plt.title('уравнение движения координаты y2')

plt.show()