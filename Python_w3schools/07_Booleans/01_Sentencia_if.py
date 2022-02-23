#Estructura basica del comando if
x=80
y=200

if x>y:
    print("x es mayor que y")
else:
    print("y es mayor que x")

#Retorno de funciones
import random

def booleana_aleatoria ():
    x=random.randrange(0,2) #toma los valores 0 ó 1
    if x==0:
        return False
    else:
        return True

print(booleana_aleatoria())

if booleana_aleatoria():
    print("Verdadero")
else:
    print("Falso")