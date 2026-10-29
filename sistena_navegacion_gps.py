
import heapq


# Excepciones propias
class ErrorGPS(Exception):
    """Clase base para los errores del sistema."""


class CiudadNoExiste(ErrorGPS):
    """Se consultó una ciudad que no está en el grafo."""


class RutaInvalida(ErrorGPS):
    """Datos inválidos al crear una ruta (peso <= 0, bucle, etc.)."""


class SinCamino(ErrorGPS):
    """No existe ningún camino entre las dos ciudades."""


# Grafo ponderado (lista de adyacencia)
class Grafo:
    """Grafo ponderado no dirigido: las autopistas se recorren en ambos sentidos."""

    def __init__(self):
        # { ciudad: { vecino: minutos } }
        self._adyacencia = {}

    @staticmethod
    def _normalizar(nombre):
        """Quita espacios y unifica mayúsculas para evitar duplicados."""
        nombre = nombre.strip()
        if not nombre:
            raise RutaInvalida("El nombre de la ciudad no puede estar vacío.")
        return nombre.title()

    def agregar_ciudad(self, nombre):
        nombre = self._normalizar(nombre)
        self._adyacencia.setdefault(nombre, {})
        return nombre

    def agregar_ruta(self, origen, destino, minutos):
        """Agrega (o actualiza) una autopista entre dos ciudades."""
        origen = self._normalizar(origen)
        destino = self._normalizar(destino)
        if origen == destino:
            raise RutaInvalida("Una ruta no puede unir una ciudad consigo misma.")
        if minutos <= 0:
            # Dijkstra exige pesos no negativos; además, 0 minutos no es realista.
            raise RutaInvalida("El tiempo debe ser mayor que cero.")
        self.agregar_ciudad(origen)
        self.agregar_ciudad(destino)
        self._adyacencia[origen][destino] = minutos
        self._adyacencia[destino][origen] = minutos

    def ciudades(self):
        return sorted(self._adyacencia)

    def vecinos(self, ciudad):
        return self._adyacencia[ciudad]

    def existe(self, ciudad):
        return ciudad in self._adyacencia

    def obtener_ciudad(self, nombre):
        """Devuelve el nombre normalizado o lanza CiudadNoExiste."""
        nombre = self._normalizar(nombre)
        if not self.existe(nombre):
            raise CiudadNoExiste(f"La ciudad '{nombre}' no existe en el mapa.")
        return nombre

# Dijkstra con reconstrucción de ruta
def dijkstra(grafo, origen, destino):
    """
    Calcula la ruta más rápida de origen a destino.
    Devuelve (tiempo_total, [ciudades del recorrido]).
    """
    origen = grafo.obtener_ciudad(origen)
    destino = grafo.obtener_ciudad(destino)

    distancia = {c: float("inf") for c in grafo.ciudades()}
    previo = {}  # previo[v] = ciudad desde la que se llegó a v por el mejor camino
    distancia[origen] = 0
    cola = [(0, origen)]  # cola de prioridad (min-heap)

    while cola:
        d_actual, actual = heapq.heappop(cola)

        if d_actual > distancia[actual]:
            continue  # entrada obsoleta: ya hay un camino mejor
        if actual == destino:
            break  # el primer pop del destino ya es el óptimo

        for vecino, minutos in grafo.vecinos(actual).items():
            nueva = d_actual + minutos
            if nueva < distancia[vecino]:
                distancia[vecino] = nueva
                previo[vecino] = actual
                heapq.heappush(cola, (nueva, vecino))

    if distancia[destino] == float("inf"):
        raise SinCamino(f"No hay camino entre {origen} y {destino}.")

    # Reconstrucción: se recorre 'previo' desde el destino hacia el origen
    ruta = [destino]
    while ruta[-1] != origen:
        ruta.append(previo[ruta[-1]])
    ruta.reverse()

    return distancia[destino], ruta


# Interfaz de consola
def formatear_tiempo(minutos):
    h, m = divmod(minutos, 60)
    return f"{h} h {m} min" if h else f"{m} min"


def leer_entero_positivo(mensaje):
    """Pide un entero > 0 y repite hasta recibir uno válido."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("  ⚠ Debe ser un número mayor que cero.")
        except ValueError:
            print("  ⚠ Ingresa un número entero válido.")


def cargar_datos_ejemplo(grafo):
    rutas = [
        ("Ciudad A", "Ciudad B", 45),
        ("Ciudad A", "Ciudad C", 90),
        ("Ciudad B", "Ciudad C", 30),
        ("Ciudad B", "Ciudad D", 75),
        ("Ciudad C", "Ciudad D", 40),
        ("Ciudad C", "Ciudad E", 120),
        ("Ciudad D", "Ciudad E", 50),
    ]
    for o, d, t in rutas:
        grafo.agregar_ruta(o, d, t)
    grafo.agregar_ciudad("Ciudad Aislada")  # útil para probar SinCamino


def opcion_ver_ciudades(grafo):
    ciudades = grafo.ciudades()
    if not ciudades:
        print("  (No hay ciudades registradas)")
        return
    print("\nCiudades y autopistas:")
    for c in ciudades:
        conexiones = grafo.vecinos(c)
        if conexiones:
            detalle = ", ".join(f"{v} ({t} min)" for v, t in sorted(conexiones.items()))
        else:
            detalle = "sin conexiones"
        print(f"  • {c}: {detalle}")


def opcion_agregar_ruta(grafo):
    origen = input("Ciudad de origen: ")
    destino = input("Ciudad de destino: ")
    minutos = leer_entero_positivo("Tiempo en minutos: ")
    grafo.agregar_ruta(origen, destino, minutos)
    print("  ✔ Ruta agregada correctamente.")


def opcion_ruta_rapida(grafo):
    origen = input("Ciudad de origen: ")
    destino = input("Ciudad de destino: ")
    total, ruta = dijkstra(grafo, origen, destino)
    print("\nRuta más rápida:")
    print("  " + " → ".join(ruta))
    # Detalle tramo por tramo
    for a, b in zip(ruta, ruta[1:]):
        print(f"    {a} → {b}: {grafo.vecinos(a)[b]} min")
    print(f"  Tiempo total: {total} min ({formatear_tiempo(total)})")


def menu():
    grafo = Grafo()
    cargar_datos_ejemplo(grafo)

    acciones = {
        "1": opcion_ver_ciudades,
        "2": opcion_agregar_ruta,
        "3": opcion_ruta_rapida,
    }

    while True:
        print("\n=== SISTEMA DE NAVEGACIÓN GPS ===")
        print("1. Ver ciudades y autopistas")
        print("2. Agregar nueva ruta")
        print("3. Consultar ruta más rápida")
        print("4. Salir")

        try:
            opcion = input("Elige una opción: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n¡Hasta luego!")
            break

        if opcion == "4":
            print("¡Buen viaje!")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("  ⚠ Opción no válida.")
            continue
        try:
            accion(grafo)
        except ErrorGPS as e:
            print(f"  ✖ {e}")
        except (EOFError, KeyboardInterrupt):
            print("\n  Operación cancelada.")


if __name__ == "__main__":
    menu()