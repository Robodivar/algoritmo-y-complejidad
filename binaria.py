def busqueda_binaria(arreglo, objetivo):
    inicio = 0
    fin = len(arreglo) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if arreglo[medio] == objetivo:
            return medio

        elif arreglo[medio] < objetivo:
            inicio = medio + 1

        else:
            fin = medio - 1

    return -1


# Arreglo ordenado
numeros = [1, 3, 4, 6, 12, 15, 35, 44]

# Buscar el número 12
resultado = busqueda_binaria(numeros, 12)

if resultado != -1:
    print("Número encontrado en la posición:", resultado)
else:
    print("Número no encontrado")