
#Ignacio Martinez Goloboff
#Ejercicio 4

def rsteffensen(fun,x0,err,mit):
    v = fun(x0)
    hx, hf= [],[]
    for k in range(mit):
        w = fun(x0 + v) - v
        x1 = x0 -((v**2)/w)
        v = fun(x1)
        hx.append(x1)
        hf.append(v)
        if abs(fun(x1)) < err:            
            break
        x0 = x1
    return hx, hf