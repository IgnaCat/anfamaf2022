import math
import random
def ej3():
    x = float(2)
    y = float(2)
    while True:
        x = x * float(2)  
        if math.isinf:
            print(x)
            break
    while True:
        x = x / float(2)
        print(x)
        if x == 0.0:
            break
def ej4 ():
    x = 0
    while x != 10:
        x = x + 0.1
        print(x)

def ej5 ():
    #A
    n = 6
    x = 1
    while True :
        if (n-1) == 0 :
            break
        x = x * n
        n = n-1
    print(x)
    #B
    print(math.factorial(6))

def ej5C (n):
    x = 1
    while True :
        if (n-1) == 0 :
            break
        x = x * n
        n = n-1
    print(x)

#d = int(input("Ingrese un numero: \n"))
#ej5C(d)

def ej6():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: ")) 

    if (a == b):
        print("Son Iguales")

    if (a < b):
        print(b, " es mayor")
        
    if (a > b):
        print(a, " es mayor")


def ej7():
    def potencia_enesima(x, n):
        res = 1
        for i in range(n+1):           
            res = x*res   
            print(res)       
        return res

    potencia_enesima(2, 5)
    

def ej8():
    def mala(a,b,c):
        delta = b*b - 4*a*c
        if (a == 0):
            print("El polinomio no es cuadratico")
            return
        if (delta < 0):
            print("Raices imaginarias")
            return
        x1 = -b + math.sqrt(delta) / (2*a)
        x2 = -b - math.sqrt(delta) / (2*a)

        return [x1, x2]

    def buena(a, b, c):
        delta = b*b - 4*a*c
        if (a == 0):
            print("El polinomio no es cuadratico")
            return
        if (delta < 0):
            print("Raices imaginarias")
            return
        x1 = -b + math.sqrt(delta) / (2*a)
        x2 = c / (x1*a) 

        return [x1, x2]

def ej9():
    def horn(coefs, x):
        z = coefs[0]
        for i in range(1, len(coefs)):
            z = coefs[i] + x*z
        return z

    print(horn([1,-5,6,5], 2))

def ej10():
    def SonReciprocos(x,y):
        if x*y == 1:
            return True
        else:
            return False
    for _ in range(100):
        x = 1 + random.random()
        y = 1/x
        if not SonReciprocos(x,y):
            print(x)


def ej11():
    def f(x):
        return math.sqrt(x*x + 1) - 1
    def g(x):
        return (x*x)/(math.sqrt(x*x + 1) + 1)
    for i in range(20):
        x = 8**-i
        print("f(x): ",f(x),"g(x): ", g(x))


def ej_12():
    x = [1, 1.024074512658109]
    y = [-1,1/x[1]]
    def SonOrtogonales(x, y):
        x1,x2= x[0],x[1]
        y1,y2= y[0],y[1]
        print(x,y)
        if x1*y1 + x2*y2 == 0:
            return True
        else:
            return False
    if not SonOrtogonales(x,y):
        print("Algo salio mal")
    else:
        print("Son ortogonales")
        


