
print("""
BIENVENIDO AL REGISTRO DE BEBES RECIEN NACIDOS

Presiona 1 para elegir tu hospital
Presiona 2 para registrar al bebe
Presiona 3 para guardar la informacion ingresada
Presiona 4 para salir
""")

opcion = input("Ingresar opcion: ")
continuar = "si"

hospital = ""
nombre = ""
apellido = ""
fecha = ""
peso = ""
altura = ""
nombre_madre = ""
nombre_padre = ""
nombre_medico = ""
hora = ""

def consultar():
    return hospital

    print("""
    Indique que hospital quieres consultar:

    1. "...."
    2. "...."
    3. "...."
    4. "...."
    """)

    selecciona = input("Elige tu hospital: ")

    if selecciona == "1":
        hospital = "...."
    elif selecciona == "2":
        hospital = "...."
    elif selecciona == "3":
        hospital = "...."
    elif selecciona == "4":
        hospital = "...."
    else:
        print("Opcion incorrecta")

    if hospital = "":
        print("Ingresaste al " + hospital)


def registrar():
    return nombre, apellido, fecha, peso, altura, nombre_madre, nombre_padre, nombre_medico, hora

    print("REGISTRO DEL BEBE")

    nombre = input("Ingrese el nombre del bebe: ")
    apellido = input("Ingrese el apellido del bebe: ")
    fecha = input("Ingrese la fecha de nacimiento: ")
    peso = input("Ingrese el peso del bebe: ")
    altura = input("Ingrese la altura del bebe: ")
    nombre_madre = input("Ingrese el nombre de la madre: ")
    nombre_padre = input("Ingrese el nombre del padre: ")
    nombre_medico = input("Ingrese el nombre del medico: ")
    fecha = input("Ingrese la hora de nacimiento: ")

    print("Bebe registrado correctamente")


def guardar():
    if nombre == "":
        print("Primero debes registrar un bebe")
    else:
        print("""
        INFORMACION GUARDADA

        Hospital: """ + hospital + """
        Nombre: """ + nombre + """
        Apellido: """ + apellido + """
        Fecha de nacimiento: """ + fecha + """
        Peso: """ + peso + """
        Altura: """ + altura + """
        Nombre de la madre: """ + nombre_madre + """
        Nombre del padre: """ + nombre_padre + """
        Nombre del medico: """ + nombre_medico + """
        hora de nacimiento: """ + hora + """)

        print("Informacion guardada correctamente")


while continuar == "si":

    opcion = input("""
    ¿Que desea realizar?

    1. Elegir hospital
    2. Registrar al bebe
    3. Guardar informacion
    4. Salir

    Ingresar opcion: """)

    if opcion == "1":
        consultar()

    elif opcion == "2":
        if hospital == "":
            print("Primero debes elegir un hospital")
        else:
            registrar()

    elif opcion == "3":
        guardar()

    elif opcion == "4":
        print("Gracias por utilizar nuestro sistema")
        continuar = "no"

    else:
        print("Opcion incorrecta")
