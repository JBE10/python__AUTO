#crando una lista con lisr
lista= list(["Bauti",13,"Boca"])


#Muesstra la cantidad de elementos de la lista
cantidad_item= len(lista)

#agrendado una elemento a la lista
lista.append("AJAJAJ")

#agrendo un elemneto a la lista en un indice especifico
lista.insert(2,"toma")

#agregando varias elementos a la lista 
lista.extend(["hola",2003])

#eliminando un elemento de la lista por su indice
lista.pop(-1) #-1 para eliminar el ultomo -2 eliminar el anteultimo

#removendo un elemento de la lista por su valor
lista.remove("AJAJAJ")

#eliminando todos los elementos de la lista
#lista.clear

#ordena la lista (solo funciona con true, flase, numeros) (reverse=True)=da vuelta los elementos es decir 123 a 321
#lista.sort(reverse=True)

#invierte los elementos de una lista
lista.reverse()

#veriifica si un elemeneto se encuentra en la lista, busca elementos identicos
elemento_enncontrado= lista.index(13)








print(elemento_enncontrado)