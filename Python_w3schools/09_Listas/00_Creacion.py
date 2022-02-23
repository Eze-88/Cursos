#Creacion
lista=["fideos","tomates","queso","ajo","queso"]

print(lista)
print(lista[1])
print(lista[-1]) #tambien con indice negativo
print(lista[2:4])
print(lista[:4])
print(lista[-3:])
print("El largo de la lista es: "+str(len(lista)))

if "tomates" in lista:
    print("Hay tomates en la lista")

#Las listas son un tipo de clases
print(type(lista))