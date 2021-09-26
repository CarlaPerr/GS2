#! /usr/bin/python3

# Verificar un usuario y clave si estan correctamente ingresados
# Determinar si es correcto o no
# Permitir solo 3 intentos
i=0
while i<3:
    usuario=input("Ingrese su nombre de usuario ")
    i=i+1
    if str(usuario)=="Carla":
        print("Usuario Correcto")
        clave=input("Ingrese su clave ")
        if str(clave)=="ROSARIO":
            print("Bienvenido Carla")
            break
        else:
            print("Clave Incorrecta")
            if i==3:
                print("Intentos agotados")
                break
    else:
        print("Usuario Incorrecto")
        if i==3:
           print("Intentos agotados")


