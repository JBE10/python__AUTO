ingreso= 4000
gasto_mensual= 1000
#if anidados y else
if ingreso >= 10000: 
        if ingreso-gasto_mensual < 0:
            print("estas en deficit")
        elif ingreso-gasto_mensual > 3000:
            print("estas bien")
#podemos poner muchos elif
elif ingreso > 1000:
    print("estas bien")
else:
    print("sos pobre")
    
      