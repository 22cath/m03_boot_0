def normal(x):
    return x

def cuadrado(x):
    return x * x

def sumaTodos(limitTo, f):
    resultado = 0
    for x in range(limitTo+1):
        resultado += f(x)
    
    return resultado

print(sumaTodos(100, normal))
print(sumaTodos(3, cuadrado))

      
