"""
Algoritmos de ordenamiento: Heap Sort y Counting Sort
-----------------------------------------------------
Heap Sort     -> basado en comparaciones, in-place, O(n log n) siempre.
Counting Sort -> NO basado en comparaciones, estable, O(n + k).
"""

import random
import time


# ---------------------------------------------------------------------------
# 1) HEAP SORT
# ---------------------------------------------------------------------------
def _sift_down(arr, inicio, fin):
    """Restaura la propiedad de max-heap hundiendo el elemento en 'inicio'."""
    raiz = inicio
    while True:
        hijo = 2 * raiz + 1              # hijo izquierdo
        if hijo > fin:
            break
        # Elegir el mayor de los dos hijos
        if hijo + 1 <= fin and arr[hijo] < arr[hijo + 1]:
            hijo += 1
        if arr[raiz] < arr[hijo]:
            arr[raiz], arr[hijo] = arr[hijo], arr[raiz]
            raiz = hijo
        else:
            break


def heap_sort(lista):
    """Ordena de menor a mayor. Devuelve una copia ordenada (no modifica la original)."""
    arr = list(lista)
    n = len(arr)

    # Fase 1: construir max-heap en O(n)
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(arr, i, n - 1)

    # Fase 2: extraer el máximo repetidamente, O(n log n)
    for fin in range(n - 1, 0, -1):
        arr[0], arr[fin] = arr[fin], arr[0]   # mover el máximo al final
        _sift_down(arr, 0, fin - 1)           # reparar el heap reducido
    return arr


# ---------------------------------------------------------------------------
# 2) COUNTING SORT (estable, soporta enteros negativos)
# ---------------------------------------------------------------------------
def counting_sort(lista, key=None):
    """
    Ordena enteros de menor a mayor. 'key' permite ordenar objetos por una
    clave entera (útil para demostrar estabilidad).
    """
    if not lista:
        return []
    key = key or (lambda x: x)

    claves = [key(x) for x in lista]
    minimo, maximo = min(claves), max(claves)
    k = maximo - minimo + 1                    # tamaño del rango

    # 1. Contar ocurrencias
    conteo = [0] * k
    for c in claves:
        conteo[c - minimo] += 1

    # 2. Acumular: conteo[i] = posición final (exclusiva) del grupo i
    for i in range(1, k):
        conteo[i] += conteo[i - 1]

    # 3. Colocar elementos recorriendo de derecha a izquierda -> ESTABLE
    salida = [None] * len(lista)
    for i in range(len(lista) - 1, -1, -1):
        idx = claves[i] - minimo
        conteo[idx] -= 1
        salida[conteo[idx]] = lista[i]
    return salida


# ---------------------------------------------------------------------------
# PRUEBAS Y COMPARACIÓN
# ---------------------------------------------------------------------------
def pruebas():
    casos = [
        [],
        [1],
        [5, 2, 9, 1, 5, 6],
        [3, -1, 0, -7, 3, 2],
        list(range(20)),
        list(range(20, 0, -1)),
        [4] * 10,
    ]
    for _ in range(200):
        casos.append([random.randint(-50, 50) for _ in range(random.randint(0, 60))])

    for c in casos:
        esperado = sorted(c)
        assert heap_sort(c) == esperado, f"heap_sort falló con {c}"
        assert counting_sort(c) == esperado, f"counting_sort falló con {c}"
    print("✔ Todas las pruebas de correctitud pasaron.")

    # Prueba de estabilidad: ordenar pares (clave, etiqueta) por la clave
    datos = [(2, "a"), (1, "b"), (2, "c"), (1, "d"), (2, "e")]
    print("\nEstabilidad (ordenando por la primera componente):")
    print("  Counting Sort:", counting_sort(datos, key=lambda t: t[0]))
    # Heap Sort comparando solo por clave perdería el orden relativo; lo
    # mostramos con una versión que ordena tuplas completas por clave:
    print("  (Counting Sort conserva a-c-e y b-d en su orden original)")


def benchmark():
    print("\nBenchmark (segundos, promedio de 3 corridas):")
    print(f"{'n':>9} {'rango k':>10} {'Heap Sort':>12} {'Counting Sort':>15}")
    for n, k in [(10_000, 1_000), (100_000, 1_000), (100_000, 10_000_000)]:
        datos = [random.randint(0, k) for _ in range(n)]
        tiempos = []
        for f in (heap_sort, counting_sort):
            t = 0
            for _ in range(3):
                inicio = time.perf_counter()
                f(datos)
                t += time.perf_counter() - inicio
            tiempos.append(t / 3)
        print(f"{n:>9} {k:>10} {tiempos[0]:>12.4f} {tiempos[1]:>15.4f}")


if __name__ == "__main__":
    pruebas()
    benchmark()