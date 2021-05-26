lista = [1,2,3,4,5,6,7,8,9,10]

def funcion(cuadrado, lista):
    resul = []
    for n in lista:
        resul.append(cuadrado(n))
    return resul

def cuadrado(n):
    return n*n

resul = funcion(cuadrado, lista)
print(resul)
