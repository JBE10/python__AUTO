cadena1 = "Hola Soy bauti"
cadena2 = "bienvenido"
 
 #dato.metodo(parametro)
 #Explica que le podemos hacer
dir(cadena1)
 #convierte en mayuscula
mayus = cadena1 .upper()

#conviente en minuscula
minus = cadena1 .lower()

#Convierte en primera letra en mayuscula
pri_mayus = cadena1 .capitalize()


#buscacvamos una cadeana en otra cadeeana -1 no encuentra valor
busqueda_find = cadena1.find("Hola")

#buscamos una cadena en otra cadena, si no encuentra nada, encuentra una exepcion
buscamos_index = cadena1 .index("b")

#si es numerico devuelve true si no false
es_numerico  = cadena1.isnumeric()

#si es alfanumericco ddevuelvmmos true sino devuelmoes fale
es_alfanum = cadena1 .isalpha()

#bucamos una cadena en otra cadena, devuelve la catidad de vece que coincida
contar_coincidencias = cadena1.count("o")

#contamos cuantos caracteres tiene una cadena 
contar_carecteres= len(cadena1)

#verifiacamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("H")

#verifiacamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("i")

#remplaza un pedazo de la cadena dada por otra dada
cadena_nueva = cadena1.replace("la","lu")

#seprar cadenas con la cadena quee le passemos\
cadena_separada= cadena1.split(" ")






print (cadena_separada)



#print (dir())