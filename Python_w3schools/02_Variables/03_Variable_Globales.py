#Creacion de una variable dentro y fuera de una funcion

#x y z son variables globales
x="FramuS"
z=0

#definicion de una funcion
def mi_funcion():
 x="Eze"
 global y #se establece que esta variable es de caracter global
 y="Arigon"
 global z
 z=32 #esta modificacion tiene impacto en la variable global
 print("Mi nombre es: "+x) #impresion de la variable local
 print("Mi apellido es: "+y) #impresion de la variable global creada localmente
 print(z)

#Ejecucion de la funcion creada
mi_funcion()

#Impresion de la variable global
print("Mi nombre es: "+x)
print("Mi apellido es: "+y) #impresion de la variable global creada localmente
print(z)