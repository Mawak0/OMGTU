from scipy.misc import derivative
import scipy
import sympy
import math

def f(x):
    return 2/(math.sin(x)+4)

p1 = derivative(f, 2.0, dx=1e-6)

print("Первая производная функции в точке: "+str(p1))

p2= derivative(f, 2.0,n=2, dx=1e-6)

print("Вторая производная функции в точке: "+str(p2))

x = sympy.Symbol('x')
ps = sympy.diff(2/sympy.sin(x)+4, x)
print("Символьное представление производной:")
print(ps)


def rectangle_method(f, a, b, n):
    width = (b - a) / n
    result = 0

    for i in range(n):
        result += f(a + i * width) * width

    return result



a = 3
b = 6
n = 10000
print("определенный интеграл от a до b = "+str(rectangle_method(f, a, b, n)))

it = sympy.integrate(2/sympy.sin(x)+4, x)
print("Неопределенный интеграл "+str(it))

def L(X):
    x1, x2 = X
    return (x1-4)**2 + (x2-2)**2

print("Минимизация функции:")

def b1(X):
    x1, x2 = X
    return 4*x1 + 2*x2 - 11

def b2(X):
    x1, x2 = X
    return -2*x1 - 7

con1 = {'type': 'ineq', 'fun': b1}
con2 = {'type': 'ineq', 'fun': b2}
cons = [con1, con2]

bounds = [(0, None), (0, None)]


x0 = [0.5, 0.5]

solution = scipy.optimize.minimize(L, x0, method='trust-constr', bounds=bounds, constraints=cons)

print('Решение:', solution)
print('Значение целевой функции:', solution.fun)

