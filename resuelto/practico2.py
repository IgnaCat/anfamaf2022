import math

from pyrsistent import b
#from matplotlib import pyplot

def rbisec(fun, I, err, mit):
    a, b = I[0], I[1]
    u, v = fun(a), fun(b)
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

def f(x):
    return math.tan(x) - 2*x

hx, hy = rbisec(f, [0.8, 1.4], 1e-5, 100)
#print (hx,"\n", hy)
#Son necesarias 15 iteraciones

def fun_lab2ej2b(x):
    return x*x - 3

hx1, hy1 = rbisec(fun_lab2ej2b, [0, 2], 1e-5, 100)
#print (hx,"\n", hy)
#Aproximacion raiz(3): 1.7320480346679688

#EJERCICIO 2 C:

x = range(-10, 10)
#x = [0.01 * i for i in range(0, 200)]
#y = [fun_labej2a(0.01 * xi) for xi in x]
#pyplot.plot(x, [fun_lab2ej2b(i) for i in x])
#pyplot.plot(hx1, hy1, '*')

#plt.plot(hx[-1], hf[-1], 'ok')

#pyplot.show()

#EJERCICIO3

def rnewton(fun,x0,err,mit):
    [v, w] = fun(x0)
    hx, hf= [],[]
    for k in range(mit-1):
        x1 = x0 -(v/w)
        [v, w] = fun(x1)
        hx.append(x1)
        hf.append(v)
        if abs(x1-x0)/ abs(x1) < err and abs(fun(x1)) < err:
            break
        x0 = x1 
    return hx, hf

def fun_newton(x):
    return [x*x-3,2*x]

hx1, hy1 = rnewton(fun_newton, 1.5 , 1e-10, 100)

#EJERCICIO4

def raiz_cubica(a):
    def f(x):
        return [x**3 - a, 3*(x**2)]
    x0 = 1
    x , _ = rnewton(f, x0, 1e-6, 100)
    return x


#EJERCICIO5
def ripf(fun,x0,err,mit):
    hx = []
    i=1  
    while i<mit:
        x1 = fun(x0)
        hx.append(x1)
        if (abs(x1-x0)<err):
            break     
        x0 = x1
        i = i+1
    return hx

#EJERCICIO6
def fun_lab2ej6(x):
    return 2**(x-1)
hx = ripf(fun_lab2ej6, 0.5, 1e-5, 100)
#Para x e(-inf, 2) converge en 1, x=2 converge en 2, en (2,inf) diverge 


def rsecante(fun,x0,x1,err,mit, err2):
    fa = fun(x0)
    fb = fun(x1)
    hx, hf= [],[]
    for k in range(2,mit-1):
        if (abs(fa) > abs(fb)):
            a_aux = a
            fa_aux = fa
            a = b
            b = a_aux
            fa = fb
            fb = fa_aux
        s = (b-a) / (fb - fa)
        b = a
        fb = fa
        a = a - (fa * s)
        fa = fun(a)
        hx.append(a)
        hf.append(fa)
        if abs(b-a) < err and abs(fa) < err2:
            break
    return hx, hf

#math.exp( x )