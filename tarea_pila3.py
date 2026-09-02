# Pila de departamentos de Nicaragua

pila = []


# Función para agregar un departamento
def agregar_departamento():
    departamento = input("Ingrese el nombre del departamento: ").strip()

    if departamento != "":
        pila.append(departamento)
        print(f"{departamento} fue agregado a la pila.")
    else:
        print("El nombre del departamento no puede estar vacío.")


# Función para remover un departamento
def remover_departamento():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        departamento = pila.pop()
        print(f"Se removió: {departamento}")


# Función para imprimir los departamentos
def imprimir_pila():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("\nDepartamentos en la pila:")

        # Se muestran desde la cima hasta el fondo
        for i in range(len(pila) - 1, -1, -1):
            print(pila[i])


# Menú principal
def menu():
    while True:
        print("\n***** MENÚ DE OPCIONES *****")
        print("1. Agregar departamento")
        print("2. Remover departamento")
        print("3. Imprimir pila")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_departamento()

        elif opcion == "2":
            remover_departamento()

        elif opcion == "3":
            imprimir_pila()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar el programa
menu()

