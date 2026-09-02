
pila = []


# 1. Agregar un nombre
def agregar_nombre():
    nombre = input("Ingrese el primer nombre: ").strip()

    if nombre != "":
        pila.append(nombre)
        print(f"{nombre} fue agregado a la pila.")
    else:
        print("El nombre no puede estar vacío.")


# 2. Eliminar un nombre de la pila
def eliminar_nombre():
    if len(pila) == 0:
        print("La pila está vacía.")
        return

    print("\nNombres disponibles:")
    
    for i in range(len(pila)):
        print(f"{i + 1}. {pila[i]}")

    opcion = int(input("Seleccione el número del nombre que desea eliminar: "))

    if opcion >= 1 and opcion <= len(pila):
        eliminado = pila.pop(opcion - 1)
        print(f"Se eliminó: {eliminado}")
    else:
        print("Número inválido.")


# 3. Mostrar el último elemento (cima)
def mostrar_cima():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print(f"El nombre en la cima es: {pila[-1]}")


# 4. Buscar un elemento
def buscar_nombre():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        nombre = input("Ingrese el nombre a buscar: ").strip()

        if nombre in pila:
            print(f"{nombre} sí existe en la pila.")
        else:
            print(f"{nombre} no existe en la pila.")


# 5. Contar elementos
def contar_elementos():
    print(f"La pila tiene {len(pila)} elemento(s).")


# 6. Mostrar todos los elementos
def mostrar_elementos():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("\nNombres en la pila:")

        for i in range(len(pila) - 1, -1, -1):
            print(pila[i])


# 7. Limpiar la pila
def limpiar_pila():
    pila.clear()
    print("La pila fue limpiada correctamente.")


# Menú principal
def menu():
    while True:
        print("\n***** MENÚ DE OPCIONES *****")
        print("1. Agregar un nombre a la Pila")
        print("2. Eliminar un nombre de la Pila")
        print("3. Mostrar el último elemento en la Cima")
        print("4. Buscar un elemento en la Pila")
        print("5. Contar cuantos elementos tiene la Pila")
        print("6. Mostrar todos los elementos de la Pila")
        print("7. Limpiar la Pila")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_nombre()
        elif opcion == "2":
            eliminar_nombre()
        elif opcion == "3":
            mostrar_cima()
        elif opcion == "4":
            buscar_nombre()
        elif opcion == "5":
            contar_elementos()
        elif opcion == "6":
            mostrar_elementos()
        elif opcion == "7":
            limpiar_pila()
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar programa
menu()
  