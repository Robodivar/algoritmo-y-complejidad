"""
Merge Sort (Ordenamiento por Mezcla)
Ejemplo de algoritmo Divide y Vencerás.

Recurrencia:    T(n) = 2T(n/2) + O(n)
Complejidad:    Θ(n log n) en todos los casos
Espacio extra:  O(n)

No usa sorted() ni list.sort(): la comparación y el ordenamiento
se implementan manualmente para que el paradigma quede explícito.
"""


def ordenar_por_mezcla(arreglo):
    """
    Ordena `arreglo` de menor a mayor usando Divide y Vencerás.

    Fase DIVIDE: parte el arreglo en dos mitades.
    Fase VENCERÁS (conquista): ordena cada mitad recursivamente.
    Fase COMBINA: fusiona las dos mitades ya ordenadas.
    """
    n = len(arreglo)

    # Caso base: un arreglo de 0 o 1 elementos ya está ordenado.
    if n <= 1:
        return arreglo

    # --- DIVIDE ---
    medio = n // 2
    mitad_izquierda = arreglo[:medio]
    mitad_derecha = arreglo[medio:]

    # --- VENCERÁS (conquista): resolver recursivamente cada mitad ---
    mitad_izquierda = ordenar_por_mezcla(mitad_izquierda)
    mitad_derecha = ordenar_por_mezcla(mitad_derecha)

    # --- COMBINA: mezclar las dos mitades ordenadas ---
    return mezclar(mitad_izquierda, mitad_derecha)


def mezclar(izquierda, derecha):
    """
    Fusiona dos listas ya ordenadas en una sola lista ordenada.
    Costo: O(n), donde n es el tamaño combinado de ambas listas.
    """
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes (a lo sumo una de las dos listas
    # tendrá elementos pendientes en este punto).
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado
