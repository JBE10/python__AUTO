usuario_resgitrado = input("Introduccir Nuevo Usuario")
contraseña_resgistrado = input("Contraseña") 


base_de_datos= {
    "nombre" : usuario_resgitrado,
    "contraseña" : contraseña_resgistrado
}

user01_ = input("Indtroduccir Ususario")
password = input("Contraseña")

if base_de_datos["nombre"] == user01_  :
    if base_de_datos["contraseña"] == password:
         print(f"Bienvenido {user01_} a FaceBook")
    
    else: 
        print("Usuario/Contraseña incorrecta")

