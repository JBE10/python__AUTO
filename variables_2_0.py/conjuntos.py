#creanddo un conjunto con set 
conjunto = set(["dato1", "dato2"])


#metiendo un conjunto dentro dee otro
conjunto1 = frozenset(["ddato1","dato2"])
conjunto2= {conjunto1 , "daato3"}

print(conjunto2)

#teoria de cnjuntos
conjunto1= {1,3,5,7}
conjunto2= {1,3,7}
# verficamos ssi es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1


#verificamos si ess un super conjunto
resultado= conjunto2.issuperset(conjunto1)
resultado= conjunto2>conjunto1
print(resultado)


#verificamos si hay algun numero en comun, solo sera true cuando seean todos numeros diferentes
resultado = conjunto2.isdisjoint(conjunto1)


print(resultado)
