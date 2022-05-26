import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

#Ejericio 1
def ilagrange(x, y, z):
    n = len(x)
    w = []
    for k in z:
        sum = 0
        for i in range(n):
            prod = 1
            for j in range(n):
                if (j != i):
                    prod = prod * (k - x[j])/ (x[i] - x[j])
            sum = sum + y[i]*prod
        
        w.append(sum)
    
    return w

def test_ilagrange():
    x = [-2, 0, 2]
    y = [4, 0, 4]
    z = [-5, 1, 3]

    w = ilagrange(x, y, z)
    return w

#Ejercicio 2
def diferencia_divididas(x, y):
    n = len(x)
    coefs = []
    # Genero filas de coefs
    for i in range(n):
        coefs.append(y[:n - i].copy())
    
    # Calculo coeficientes de diferencias divididas
    for i in range(1, n):
        for j in range(n - i):
            (coefs[i])[j] = ((coefs[i-1])[j+1] - (coefs[i-1])[j])
            (coefs[i])[j] = (coefs[i])[j] / (x[j + i] - x[j])

    # Genero vector de coeficientes del polinomio
    c = [x[0] for x in coefs]
    return c

def inewton( x, y, z):
    n = len(x)
    w = []
    c = diferencia_divididas(x, y)
    
    for k in z:
        sum = 0
        for i in range(n):
            prod = 1
            for j in range(i-1):
                prod = prod*(k - x[j])
            sum = sum + c[i]*prod
        
        w.append(sum)
    
    return w

def test_inewton():
    x = [-2, 0, 2]
    y = [4, 0, 4]
    z = [-5, 1, 3]

    w = inewton(x, y, z)
    return w


#Ejercicio 3
def f(x):
    return 1/x

def ej3():
    x = [1, 2, 3, 4, 5]
    y = [1, 1/2, 1/3, 1/4, 1/5]
    z = np.linspace(1, 5, 101) #Genera 101 puntos entre 1 y 5
    fz = f(z)

    w = ilagrange(x, y, z)


    # Scipy, para poder usar Splines es necesario agregar el argumento kind="cubic"
    # interp1d nos devuelve una función que podemos evaluar
    polinomio = interp1d(x, y, kind="cubic")
    spline_puntos = polinomio(z)

    plt.plot(z, fz, label="f(z)")
    plt.plot(z, w, label="p(z)")
    plt.plot(z, spline_puntos, label="spline(z)")
    plt.plot(x, y, "*", label="puntos")
    plt.legend()
    #plt.savefig("pepe.png")
    plt.show()


#Ejercicio 4
def f2(x):
    return 1/(1+25*(x**2))

def ej4(n):
    x = np.arange(1,n+1)
    xi = 2*(x-1)/n - 1
    y = f2(xi)
    z = np.linspace(-1, 1, 200)
    fz = f2(z)
    w = ilagrange(xi, y, z)

    plt.plot(z, fz, label="f(z)")
    plt.plot(z, w, label="p(z)")
    plt.legend()
    plt.show()


#Ejercicio 5
def ej5():
    datos = np.loadtxt('https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos_aeroCBA.dat')
    #Nos trae todas las filas de primera y seg columna
    year = datos[:,0]
    temp = datos[:,1]

    #isnan(a): array de booleanos
    #Arrays datos no faltantes
    temp_nonan = temp[~np.isnan(temp)]
    year_nonan= year[~np.isnan(temp)]

    pol = interp1d(year_nonan, temp_nonan, kind='cubic', fill_value='extrapolate')

    year_plot = np.arange(1957,2017)
    temp_plot = pol(year_plot)

    plt.plot(year_nonan,temp_nonan,'o',label='datos')
    plt.plot(year_plot,temp_plot,label='interpolaciones y extrapolaciones')
    plt.legend()
    plt.savefig("ej5.png")
    plt.show()

#Ejercicio 5
x = [-3., -2., -1., -0., 1 ,2, 3]
y = [1, 2, 5, 10, 5, 2, 1]
z = np.linspace(-3, 3)

polinomio = interp1d(x, y, kind='cubic')
interp1d = polinomio(z)
lagrange = ilagrange(x, y, z)
newton = inewton(x, y, z)

plt.plot(x, y, "o", label="Datos existentes")
plt.plot(z, interp1d, label="Spline cubico")
plt.plot(z, lagrange, label="Lagrange")
plt.plot(z, newton, label="Newton")
plt.legend()
plt.show()
