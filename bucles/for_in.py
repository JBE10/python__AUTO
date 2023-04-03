animales = ["gato", "perro","loro","cocodrilo","pez"]


#recoriendo la lista animales
for animal in animales:
    print(f"ahora la variable animal es igual a:{animal}")
    
    
numeros=[1,2,3,4,6]

#recoriendo la lista y mutiplicando cada valor por 10
for numero in numeros:
    resultados= numero*10
    print(resultados)

#iterando dos lista al mismmo tiempo    
for numero, animal in zip(animales,numeros):
    print(f"recoriendo lista 1 {numero}")
    print(f"Recoriendo lista 2  {animal}")