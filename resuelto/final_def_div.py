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

def diferencia_divididas2(x, y):
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
    return coefs

def new(c0, x0, x1, y1):
    n0 = len(x0)
    n1 = len(x1)
    coefs = c0
    # Genero filas de coefs
    for i in range(n0):
        for j in range(n1):
            coefs[i].append(y1[j])
    coefs.append(y1[:n1].copy())
    x = x0
    for i in range(n1):
        x.append(x1[i])
    
    # # Calculo coeficientes de diferencias divididas
    for i in range(1, n0+n1):
        for j in range(n0-i, n0+n1 - i):
            (coefs[i])[j] = ((coefs[i-1])[j+1] - (coefs[i-1])[j])
            (coefs[i])[j] = (coefs[i])[j] / (x[j + i] - x[j])

    # # Genero vector de coeficientes del polinomio

    return coefs

print(diferencia_divididas([3,1,5], [1, -3, 2]))
print(diferencia_divididas2([3,1,5,6], [1, -3, 2, 4]))
print(new(diferencia_divididas2([3,1,5], [1, -3, 2]),[3,1,5] ,[6], [4]))