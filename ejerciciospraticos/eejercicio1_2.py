#Calcular cuanto tarda en decir una frase 

palabras_queres_decir = input("decime una frase que quieras ddecir: ")
catidad_de_palabras = palabras_queres_decir.split(" ")
cantidad_total_palabras = len(catidad_de_palabras)

segundos_x_palabras = cantidad_total_palabras / 2

print (f"Tardarias {segundos_x_palabras} en decir {palabras_queres_decir}")

if cantidad_total_palabras > 120 :
    print('para flaco tampoco te pedi un testamento')
 
#ddalto tarda un 30% menos 

dalto_tiempo = segundos_x_palabras * 100 // 2 * 1.3 /100 

print(f'dalto tardaria {dalto_tiempo} segundos')