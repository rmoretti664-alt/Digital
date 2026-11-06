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
    global hospital  # Permite modificar la variable global
    
    print("""
    Indique que hospital quieres consultar:

    1. Hospital Central
    2. Hospital Materno Infantil
    3. Sanatorio San Martin
    4. Clinica del Sol
    """)

    selecciona = input("Elige tu hospital: ")

    if selecciona == "1":
        hospital = "Hospital Central"
    elif selecciona == "2":
        hospital = "Hospital Materno Infantil"
    elif selecciona == "3":
        hospital = "Sanatorio San Martin"
    elif selecciona == "4":
        hospital = "Clinica del Sol"
    else:
        print("Opcion incorrecta")
        return

    if hospital != "":
        print("Ingresaste al " + hospital)


def registrar():
    global nombre, apellido, fecha, peso, altura, nombre_madre, nombre_padre, nombre_medico, hora

    print("\nREGISTRO DEL BEBE")

    nombre = input("Ingrese el nombre del bebe: ")
    apellido = input("Ingrese el apellido del bebe: ")
    fecha = input("Ingrese la fecha de nacimiento: ")
    peso = input("Ingrese el peso del bebe: ")
    altura = input("Ingrese la altura del bebe: ")
    nombre_madre = input("Ingrese el nombre de la madre: ")
    nombre_padre = input("Ingrese el nombre del padre: ")
    nombre_medico = input("Ingrese el nombre del medico: ")
    hora = input("Ingrese la hora de nacimiento: ")

    print("Bebe registrado correctamente")


def guardar():
    if nombre == "":
        print("Primero debes registrar un bebe")
    else:
        datos_registro = f"""----------------------------------------
INFORMACION GUARDADA
Hospital: {hospital}
Nombre: {nombre}
Apellido: {apellido}
Fecha de nacimiento: {fecha}
Peso: {peso}
Altura: {altura}
Nombre de la madre: {nombre_madre}
Nombre del padre: {nombre_padre}
Nombre del medico: {nombre_medico}
Hora de nacimiento: {hora}
----------------------------------------\n"""

        # Muestra en pantalla
        print(datos_registro)

        # Guarda en archivo de texto automáticamente
        with open("registros_bebes.txt", "a", encoding="utf-8") as archivo:
            archivo.write(datos_registro)

        print("¡Informacion guardada correctamente en el archivo 'registros_bebes.txt'!")


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
