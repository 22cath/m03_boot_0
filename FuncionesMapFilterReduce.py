from functools import reduce

# MAP()

def doble(x):
    return x+x

lista = [1, 3, -1, 15, 9]

listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista)


# FILTER(): sobre los elementos de la lista, solo me vas a devolver los valores x
# que cumplan con que el resto de x partido por 2 es igual a zero, y lo aplicas sobre lista. Y si no, nada.

def esPar(x):
    return x % 2 == 0

listaPares = filter(lambda x: x % 2 == 0, lista)
listaPares1 = filter(esPar, lista)

# REDUCE()
sumatorio = reduce(lambda x, y: x + y, lista)
sumatorioDobles = reduce(lambda x, y: x + y*2, lista)
suma100 = reduce(lambda x, y: x + y, range(101))

print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(sumatorioDobles)
print(suma100)


