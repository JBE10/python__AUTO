diccionario = {
    "nombre" : 'Bautista',
    "apellido":'Espino',
    "Sueldo": 1000000
}

#nos devuelve un objeto diict_item
claveskey= diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_sueldo= diccionario.get("Sueldo")

#eliminando todo del diccionario 
#limpiar_diccionario= diccionario.clear()

#eliminamos un un iteam del diccionario
limpiar_uno = diccionario.pop("nombre")

#obtenniendo un elemnto ddict_items iterable
diccionario_iterable = diccionario.items

    
print(claves)
