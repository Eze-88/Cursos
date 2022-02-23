#Impresion de una evaluacion booleana
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Evaluacion de variable
x="Hola"
y=27

print(bool(x)) #solo da False si la cadena esta vacia
print(bool(y)) #solo da False si el valor es cero

#Casos especiales
print(bool(False))
print(bool(None))
print(bool(()))
print(bool([]))
print(bool({}))

#Se puede verificar el tipo de dato
print(isinstance(x,int))
print(isinstance(x,str))