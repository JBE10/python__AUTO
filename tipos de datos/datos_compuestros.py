#lista = ["Juan Espino","44147343","Nebwery 10181"]

#tuplas/conjuntos no modificafle
#tupla = ("1177030 " "Vienna")
#conjunto = {1.70, 82.5} 
#no se puede accedder al indece en los conjuntos(set), no almacena duplicados.
nombres = input("Nombre")
red_social = input("Colocar tu red Social")
n_d_dni = int(input("Colocar tu Documento"))
#diccionario la estructuraa es key : value y separamos con comas
diccionario = {
    "nombre" : nombres ,
    "Redes_sociales" : red_social ,
    "n_de_DNI" : n_d_dni
}
print(diccionario["nombre"])



