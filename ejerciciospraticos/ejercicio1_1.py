#promedio de duracion
este_curso = 1.5
curso_rapido = 2.5
curso_promedio = 4
curso_lento = 7

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5


#calculando el tiempo vacio 
tiempo_removido_dalto = 100 - este_curso *1000 // crudo_dalto / 10
tiempo_removido_promedio = 100 - curso_promedio *1000 // crudo_promedio/10

#mostrado resultado ejercicio2
print(f"este curso elimina un{tiempo_removido_dalto}% del espacio vacio")
print(f"los cursos promedios eliminan un {tiempo_removido_promedio}% de espacio vacio ")
    
    
    
#diferancia de duracion
dif_duracion_con_rapido = int(100 - este_curso / curso_rapido * 100)
dif_duracion_con_lento = 100 - este_curso * 1000 // curso_lento / 10
dif_duracion_con_promedio = int(100 - este_curso / curso_promedio * 100)


print(f'el curso de dalto dura un {dif_duracion_con_rapido}% menos')
print(f'el curso de dalto dura un {dif_duracion_con_lento}% menos')
print(f'el curso de dalto dura un {dif_duracion_con_promedio}% menos')


#ejecicio3 cuanto equivale ver uno del otro
print(f"Ver 10 horas de este curso equivale a ver {curso_promedio *100 // este_curso /10} horas de otros cursos")
print(f"Ver 10 horas de otro curso equivale a ver {este_curso *100  // curso_promedio /10} horas de este curso")

