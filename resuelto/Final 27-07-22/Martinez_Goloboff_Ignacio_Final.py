#Ignacio Martinez Goloboff

import math
import matplotlib.pyplot as plt
import numpy as np

#Ejercicio 1
#a
def fun(y):
    return 1/y

def integral_simpson(x: float):
    n = 2 * 100
    h = (x-1)/n
    sx0 = fun(1) + fun(x)
    sx1 = 0
    sx2 = 0
    x = 1
    for j in range(1, n):
        x = x + h
        if j%2==0:
            sx2 += fun(x)
        else:
            sx1 += fun(x)
    return ( sx0 + 2*sx2 + 4*sx1) * h / 3

#b
# Integral (1/y) dy = 1 => Integral (1/y) dy - 1 = 0
# Usamos el metodo de biseccion para calcular la raiz, 
# ya que en el metodo de newton necesitamos calcular la derivada de f y tiene un mayor costo.
# y integral simpson para calcular la aproximacion de la integral

def f(y: float):
    return integral_simpson(y) - 1

def rbisec(fun, I, err, mit):
    a, b = I[0], I[1]
    u, v = f(a), f(b)
    e = abs(b-a)
    hx = []
    hf = []
    if math.copysign(1,u) == math.copysign(1,v): 
        return hx, hf
    for k in range(mit-1):
        e = e/2
        c = a+e
        w = fun(c)
        hx.append(c)
        hf.append(w)
        if abs(e)<err:
            break
        if math.copysign(1,u) != math.copysign(1,w):
            b = c
            v = w
        else:
            a = c
            u = w

    return hx, hf

hx, hf = rbisec(f, [1, math.e+1], 1e-6, 100)
print("Aproximacion de e: {}".format(hx[len(hx)-1]))
print("Math.e: {}".format(math.e))

#c
print("Error absoluto entre math.e y aprox de e: {}".format(abs(math.e - hx[len(hx)-1])))

x = np.linspace(1, 8, 200)
y = integral_simpson(x)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(hx, hf, "*", label="Puntos visitados con el metodo de biseccion")
ax1.legend()
ax2.plot(x, y, "o", label="Aproximacion de la integral simpson en [1,8]")
ax2.legend()
plt.show()