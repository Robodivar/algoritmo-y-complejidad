"""Benchmark de algoritmos de ordenamiento.

Compara Selección, Inserción, Burbuja, Quicksort y Heapsort sobre
exactamente los mismos datos (cada algoritmo recibe una copia de la misma
lista) para distintos órdenes iniciales y tamaños n.

Uso:  python3 benchmark.py
Salida: tabla en consola + resultados.csv
"""
import csv
import random
import statistics
import time

# ----------------------------------------------------------------------
# Algoritmos (todos in-place, ordenan de menor a mayor)
# ----------------------------------------------------------------------

def seleccion(a):
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]


def insercion(a):
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        while j >= 0 and a[j] > clave:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = clave


def burbuja(a):
    # Versión con bandera: corta si una pasada no hizo intercambios.
    n = len(a)
    for i in range(n - 1):
        hubo = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                hubo = True
        if not hubo:
            break


def quicksort(a):
    # Pivote mediana de tres + partición de Hoare. Se recursa sobre la
    # partición menor y se itera sobre la mayor (profundidad O(log n)).
    def qs(lo, hi):
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < a[lo]:
                a[mid], a[lo] = a[lo], a[mid]
            if a[hi] < a[lo]:
                a[hi], a[lo] = a[lo], a[hi]
            if a[hi] < a[mid]:
                a[hi], a[mid] = a[mid], a[hi]
            p = a[mid]
            i, j = lo, hi
            while i <= j:
                while a[i] < p:
                    i += 1
                while a[j] > p:
                    j -= 1
                if i <= j:
                    a[i], a[j] = a[j], a[i]
                    i += 1
                    j -= 1
            if j - lo < hi - i:
                qs(lo, j)
                lo = i
            else:
                qs(i, hi)
                hi = j
    qs(0, len(a) - 1)


def heapsort(a):
    n = len(a)

    def sift_down(i, fin):
        while True:
            h = 2 * i + 1
            if h >= fin:
                return
            if h + 1 < fin and a[h + 1] > a[h]:
                h += 1
            if a[i] >= a[h]:
                return
            a[i], a[h] = a[h], a[i]
            i = h

    for i in range(n // 2 - 1, -1, -1):   # construir el heap: O(n)
        sift_down(i, n)
    for fin in range(n - 1, 0, -1):        # n extracciones: O(n log n)
        a[0], a[fin] = a[fin], a[0]
        sift_down(0, fin)


ALGORITMOS = {
    "Seleccion": seleccion,
    "Insercion": insercion,
    "Burbuja": burbuja,
    "Quicksort": quicksort,
    "Heapsort": heapsort,
}

# ----------------------------------------------------------------------
# Generadores de datos (órdenes iniciales)
# ----------------------------------------------------------------------

def aleatorio(n, rng):
    return [rng.randint(0, n * 10) for _ in range(n)]


def ordenado(n, rng):
    return list(range(n))


def inverso(n, rng):
    return list(range(n, 0, -1))


def casi_ordenado(n, rng):
    a = list(range(n))
    for _ in range(max(1, n // 100)):      # ~1 % de pares fuera de lugar
        i, j = rng.randrange(n), rng.randrange(n)
        a[i], a[j] = a[j], a[i]
    return a


ORDENES = {
    "Aleatorio": aleatorio,
    "Ordenado": ordenado,
    "Inverso": inverso,
    "Casi ordenado": casi_ordenado,
}

TAMANOS = [500, 1000, 2000, 4000]
REPETICIONES = 3        # se reporta la mediana
SEMILLA = 42


def medir(func, datos):
    tiempos = []
    for _ in range(REPETICIONES):
        copia = datos[:]                   # mismos datos, copia nueva
        t0 = time.perf_counter()
        func(copia)
        tiempos.append(time.perf_counter() - t0)
        assert copia == sorted(datos), f"{func.__name__} ordenó mal"
    return statistics.median(tiempos)


def main():
    rng = random.Random(SEMILLA)
    filas = []
    for orden, gen in ORDENES.items():
        for n in TAMANOS:
            datos = gen(n, rng)            # un único conjunto por (orden, n)
            for nombre, func in ALGORITMOS.items():
                filas.append((orden, n, nombre, medir(func, datos)))
                print(f"{orden:14s} n={n:5d} {nombre:10s} {filas[-1][3]*1000:10.2f} ms",
                      flush=True)

    with open("resultados.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["orden", "n", "algoritmo", "segundos"])
        w.writerows(filas)


if __name__ == "__main__":
    main()