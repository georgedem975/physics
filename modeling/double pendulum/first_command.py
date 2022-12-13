import matplotlib.pyplot as plt
import numpy as np
import math

plt.style.use('ggplot')


G = 9.8
e = 2.71

a = 10 #= int(input('введите начальную фазу колебаний: '))
l = 300 #= int(input('введите длину стержня: '))

A = 15 #= int(input('введите аммплитуду колебаний: '))

w0 = math.sqrt(G/l)

# массив времени t от 0 секунд до 5
t = np.arange(0., 150., 0.2)

f = A*np.cos(w0*t + a)

r = 1#= int(input('введите коэффициент трения: '))
m = 12 #= int(input('введите массу: '))

#коэффициент затухания
B = r / (2*m)

#циклическая частота
w = math.sqrt((w0**2 - B**2))

#уравнение затухающих колебаний
x = A * (e**(-B*t))*np.cos(w*t + a)

print('Гармонические колебания:')
print('собственная частота = ', w0)
print('период = ', 2 * 3.14 / w0)
print('частота колебаний = ', w0 / (6.28))
print('момент инерции = ', m * l**2)

print()
print('Затухающие колебания:')
print('собственная частота = ', w0)
print('период = ', 6.28 / w)
print('частота колебаний = ', w)
print('коэфициент затухания = ', B)

plt.subplot(2, 1, 1)
# отображение графиков
plt.plot(t, x, 'r--')
plt.title('уравнение затухающих колебаний маятника')

plt.subplot(2, 1, 2)
# отображение графиков  math.cos(w0*t + a)
plt.plot(t, f, 'r--')
plt.title('уравнение гармонических колебаний маятника')

plt.show()