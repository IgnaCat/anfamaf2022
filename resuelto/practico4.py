import numpy as np
import matplotlib.pyplot as plt

#Ejericio1
def ej1():
    data = np.loadtxt("../datos/datos1a.dat")
    x = data[:,0]
    y = data[:,1]

    #A
    length = len(x)
    sumxi = 0
    sumxi_2 = 0
    sumxy = 0
    sumyi = 0

    for i in range(1, length):
        sumxi += x[i]
        sumxi_2 += x[i]**2
        sumxy += x[i]*y[i]
        sumyi += y[i]

    a0 = (sumxi_2*sumyi - sumxy*sumxi) / ((length*sumxi_2) - sumxi**2)
    a1 = (length*sumxy - sumxi*sumyi) / ((length*sumxi_2) - sumxi**2)
    fun = a0 + a1*x

    # plt.plot(x, y, "o", label="Datos existentes")
    # plt.plot(x, fun, label="Aprox lineal por cuadrados minimos")
    # plt.title("A")
    # plt.legend()
    # plt.savefig("ej1a.png")
    # plt.show()

    #B
    ones = np.ones(length)
    sumxi = np.dot(x, ones)
    sumxi_2 = np.dot(x, x)
    sumxy = np.dot(x, y)
    sumyi = np.dot(y, ones)

    # plt.plot(x, y, "o", label="Datos existentes")
    # plt.plot(x, fun, label="Aprox lineal por cuadrados minimos")
    # plt.title("B")
    # plt.legend()
    # plt.savefig("ej1b.png")
    # plt.show()

    #C

    x = np.linspace(0, 10, 20)
    y = ((3/4)*x) - 1/2
    dispersion = np.random.randn(20) #Array 20 elems con nums random
    y_dispersion = y + dispersion

    ajuste_lineal = np.polyfit(x, y_dispersion, 1)
    y_2 = np.polyval(ajuste_lineal, x) #Evalua en x el polinomio de ajuste lineal


    plt.plot(x, y, "o", label="Datos existentes")
    plt.plot(x, y_dispersion, label="Aprox lineal dispersa")
    plt.plot(x, y_2, label="Aprox lineal recta ajustada")
    plt.title("C")
    plt.legend()
    plt.savefig("ej1c.png")
    plt.show()

#Ejercicio 2
#A
def ej2():
    x = np.linspace(0, 1, 50)
    y = np.arcsin(x) + np.random.randn(50)

    for i in range(1,6):
        ajuste = np.polyfit(x, y, i)
        yi = np.polyval(ajuste, x)
        residuo = sum(abs(y-yi))
    #     print(f"Residuo de grado {i}: {residuo}")
    #     plt.plot(x, yi, label=f"Ajuste de grado {i}")

    # plt.plot(x, y, "o", label="Datos existentes")
    # plt.plot(x, y, label="Funcion con dispersion")
    # plt.title("A")
    # plt.legend()
    # plt.savefig("ej2a.png")
    # plt.show()
    #Mientras mas subis el grado del ajuste, el residuo va disminuyendo y la aprox es cada vez mas cercana

    #B
    x = np.linspace(0, 4*np.pi, 50)
    y = np.cos(x) + np.random.randn(50)

    for i in range(1,6):
        ajuste = np.polyfit(x, y, i)
        yi = np.polyval(ajuste, x)
        residuo = sum(abs(y-yi))
    #     print(f"Residuo de grado {i}: {residuo}")
    #     plt.plot(x, yi, label=f"Ajuste de grado {i}")

    # plt.plot(x, y, "o", label="Datos existentes")
    # plt.plot(x, y, label="Funcion con dispersion")
    # plt.title("B")
    # plt.legend()
    # plt.savefig("ej2b.png")
    # plt.show()

#Ejercicio 3
def ej3():
    dataA = np.loadtxt("../datos/datos3a.dat")
    dataB = np.loadtxt("../datos/datos3b.dat")

    #A
    x = dataA[0]
    y = dataA[1]

    # y = C * (x ** A) --> ln(y) = ln(C) + A * ln(x)

    x_p = np.log(x)
    y_p = np.log(y)

    coefs = np.polyfit(x_p, y_p, 1)

    A = coefs[0]
    C = np.exp(coefs[1])

    # print(f'Coef. A = {A}, Coef C = {C}.')

    # plt.plot(x, y, "o", label="Datos existentes")
    # plt.plot(x, C * (x ** A), label="Funcion a")
    # plt.savefig("ej3a.png")
    # plt.legend()
    # plt.show()

    #B
    x = dataB[0]
    y = dataB[1]

    # y = x / (Ax + B) --> x/y = Ax + B

    coefs = np.polyfit(x, x/y, 1)
    A = coefs[0]
    B = coefs[1]

    print(f'Coef. A = {A}, Coef B = {B}.')

    plt.plot(x, y, "o", label="Datos existentes")
    plt.plot(x, x / (A*x + B), label="Funcion b")
    plt.savefig("ej3b.png")
    plt.legend()
    plt.show()

#Ejercicio 4
data = np.loadtxt("../datos/covid_italia.csv", delimiter=",", dtype=str)
x = data[:,0]
y = data[:,1].astype(int)

# y = a* e**bx --> ln(y) = ln(a) + bx * ln(e)

x_p = np.array(range(1, len(x)+1))
y_p = np.log(y)

coefs = np.polyfit(x_p, y_p, 1)
b = coefs[0]
a = np.exp(coefs[1])

print(f'Coef. A = {a}, Coef C = {b}.')

plt.plot(x, y, "o", label="Datos existentes covid")
plt.plot(x, a*np.exp(b*x_p), label="Funcion exponencial")
plt.savefig("ej4.png")
plt.legend()
plt.show()