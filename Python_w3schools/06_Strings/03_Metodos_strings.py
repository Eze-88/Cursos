#Uso de diferentes metodos para strings
x=" Perro Mirando al Norte "
print(x)

#imprime la cadena sin los espacios al principio y final
print(x.strip())

#imprime la cadena en minusculas
print(x.lower())

#imprime la cadena en mayusculas
print(x.upper())

#imprime reemplazo de los elementos que sean iguales a "o" por "0"
print(x.replace("o","0"))

#parte un string usando un elemento especificado
x1=x.split(" ")
print(x1[1])
print(x1[2])
print(x1[3])
print(x1[4])
print(x1)
#le puedo asignar una cadena especifica al partir la original
x1=x.split(" ")[2]
print(x1)

#verificar que se encuentre una cadena dentro de otra
y= "erro" in x
print(y) #devuelve true o false

#Concatenacion
y="contemplativamente"
version=1.2
release=2
compilacion=1
z=x.strip()+", "+y+" v"+str(version)
print(z)
y="La version es la v{}.R{}.C{}"
print(y.format(version,release,compilacion))
y="La version es la v{2}.R{0}.C{1}"
print(y.format(release,compilacion,version)) #deberia imprimir lo mismo que antes