#! /usr/bin/python3

# Verificar un usuario y clave si estan correctamente ingresados
# Determinar si es correcto o no
# Permitir solo 3 intentos

#Contadores de intentos
i=0
j=0

while i<3 and j<3:
    usuario=input("Ingrese su nombre de usuario ")
    if str(usuario)=="Carla":
        print("Usuario Correcto")
        clave=input("Ingrese su clave ")
        if str(clave)=="ROSARIO":
            print("Bienvenida Carla")
            break
        else:
            print("Clave Incorrecta")
            print ("Usted usó", j+1,"intentos de clave")
            j=j+1
            if j==3:
                print("Intentos agotados")
                break
    else:
        print("Usuario Incorrecto")
        print ("Usted usó", i+1,"intentos de usuario")
        i=i+1
        if i==3:
           print("Intentos agotados")


