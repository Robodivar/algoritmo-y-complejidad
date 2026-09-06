# Ecuaciones de Recurrencia
# Análisis de complejidad
#
# Cada función simula el árbol de recursión de una ecuación distinta.
# Para las ecuaciones con trabajo constante por llamada (O(1)), la función
# solo suma los resultados de las llamadas recursivas: el valor devuelto
# equivale al número de nodos hoja del árbol, que es asintóticamente
# proporcional al costo total real.
# Para las ecuaciones con trabajo no constante (O(n^2)), se suma
# explícitamente ese trabajo en cada llamada.


# Ecuación 1
# T(n) = 2T(n/2) + O(1)
# Complejidad: O(n)
def ecuacion_1(n):
    if n <= 1:
        return 1
    return ecuacion_1(n // 2) + ecuacion_1(n // 2)


# Ecuación 2
# T(n) = 4T(n/2) + O(1)
# Complejidad: O(n^2)
def ecuacion_2(n):
    if n <= 1:
        return 1
    return (
        ecuacion_2(n // 2)
        + ecuacion_2(n // 2)
        + ecuacion_2(n // 2)
        + ecuacion_2(n // 2)
    )


# Ecuación 3
# T(n) = 2T(n/2) + O(n^2)
# Complejidad: O(n^2)
def ecuacion_3(n):
    if n <= 1:
        return 1
    trabajo = n ** 2
    return (
        ecuacion_3(n // 2)
        + ecuacion_3(n // 2)
        + trabajo
    )


# Ecuación 4
# T(n) = T(n-1) + O(1)
# Complejidad: O(n)
def ecuacion_4(n):
    if n <= 1:
        return 1
    return ecuacion_4(n - 1) + 1


# Ecuación 5
# T(n) = T(n/3) + T(2n/3) + O(1)
# Complejidad: O(n)
#
# NOTA IMPORTANTE (corrección):
# Con trabajo O(1) por llamada, esta recurrencia da Θ(n), NO Θ(n log n).
# El Θ(n log n) solo aparece cuando el trabajo por llamada es O(n)
# (por ejemplo, la fase de "mezcla" en Merge Sort). Aquí, al ser O(1),
# el análisis por método de Akra-Bazzi da exponente p=1 (porque
# (1/3)^1 + (2/3)^1 = 1) y la integral de un término O(1) converge a una
# constante, por lo que T(n) = Θ(n^1 · (1 + O(1))) = Θ(n).
# Se verificó empíricamente: ecuacion_5(n) / n = 1.0 para todo n probado.
#
# Además se corrigió un bug de recursión infinita: con la partición
# original (parte_1 = n // 3), para n = 2 se obtenía parte_1 = 0 y
# parte_2 = 2 - 0 = 2, es decir, la función se volvía a llamar con el
# mismo n indefinidamente. Se usa max(1, n // 3) para garantizar que
# ambas partes sean siempre estrictamente menores que n.
def ecuacion_5(n):
    if n <= 1:
        return 1
    parte_1 = max(1, n // 3)
    parte_2 = n - parte_1
    return ecuacion_5(parte_1) + ecuacion_5(parte_2)


# Ecuación 6
# T(n) = 3T(n/4) + O(n^2)
# Complejidad: O(n^2)
def ecuacion_6(n):
    if n <= 1:
        return 1
    trabajo = n ** 2
    return (
        ecuacion_6(n // 4)
        + ecuacion_6(n // 4)
        + ecuacion_6(n // 4)
        + trabajo
    )


# Prueba de las funciones
if __name__ == "__main__":
    n = 8
    print("Ecuación 1:", ecuacion_1(n))
    print("Ecuación 2:", ecuacion_2(n))
    print("Ecuación 3:", ecuacion_3(n))
    print("Ecuación 4:", ecuacion_4(n))
    print("Ecuación 5:", ecuacion_5(n))
    print("Ecuación 6:", ecuacion_6(n))
