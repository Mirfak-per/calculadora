#Escribe un programa que solicite ingresar un nombre de usuario y una contraseña.
#Si el nombre es “Gwenevere” y la contraseña es “excalibur”,
#mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”.
#Si el nombre o la contraseña no coinciden, mostrar “Accesodenegado”


nombre = input("ingrese su usuario")
contra = input("ingrese la contraseña")

if nombre == "Gwenvere" and contra == "excalibur":
    print("usuario y contraseña correctos, puede ingresar a Camelot")
else:
    print("usurio y/o contraseña incorrectos, acceso denegado")