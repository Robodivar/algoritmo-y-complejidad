"""
Punto de entrada: demuestra Merge Sort sobre un arreglo de ejemplo.
"""

from merge_sort import ordenar_por_mezcla


def main():
    arreglo = [38, 27, 43, 3, 9, 82, 10]

    print("Arreglo original:", arreglo)
    ordenado = ordenar_por_mezcla(arreglo)
    print("Arreglo ordenado:", ordenado)


if __name__ == "__main__":
    main()
