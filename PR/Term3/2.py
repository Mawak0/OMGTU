from scipy.misc import derivative
import scipy
import sympy
def f(x):
    return (2*x**3)**(1/2)

p1 = derivative(f, 4.0, dx=1e-6)

print("Первая производная функции в точке: "+str(p1))

p2= derivative(f, 4.0,n=2, dx=1e-6)

print("Вторая производная функции в точке: "+str(p2))
x = sympy.Symbol('x')
ps = sympy.diff((2*x**3)**(1/2), x)
print(ps)


iq = scipy.integrate.quad(f, a = 2, b= 4)

print("определенный интеграл от a до b = "+str(iq[0]))
