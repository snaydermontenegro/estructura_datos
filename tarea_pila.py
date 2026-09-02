# Programa para trabajar con una pila de números enteros

# Pila
pila = []


# 1. Función para agregar números
def agregar_numeros():
    cantidad = int(input("¿Cuántos números desea agregar?: "))

    for i in range(cantidad):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        pila.append(numero)

    print("Números agregados correctamente.")


# 2. Función para contar elementos
def contar_elementos():
    cantidad = len(pila)
    print(f"La pila contiene {cantidad} elemento(s).")


# 3. Función para mostrar todos los elementos
def mostrar_elementos():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("Elementos de la pila:")

        for numero in pila:
            print(numero)


# 4. Función para calcular el promedio
def calcular_promedio():
    if len(pila) == 0:
        print("No se puede calcular el promedio porque la pila está vacía.")
    else:
        suma = sum(pila)
        promedio = suma / len(pila)

        print(f"El promedio de los números es: {promedio:.2f}")


# Función principal / menú
def menu():
    while True:
        print("\n***** MENÚ DE OPCIONES *****")
        print("1. Agregar números")
        print("2. Contar elementos")
        print("3. Mostrar todos los elementos")
        print("4. Promedio de todos los números")
        print("5. Salir del sistema")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_numeros()

        elif opcion == "2":
            contar_elementos()

        elif opcion == "3":
            mostrar_elementos()

        elif opcion == "4":
            calcular_promedio()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar el programa
menu()

