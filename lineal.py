def busqueda_lineal(arreglo, objetivo):
    for i in range(len(arreglo)):
        if arreglo[i] == objetivo:
            return i

    return -1


# Arreglo
numeros = [1, 3, 4, 6, 12, 15, 35, 44]

# Buscar el número 12
resultado = busqueda_lineal(numeros, 12)

if resultado != -1:
    print("Número encontrado en la posición:", resultado)
else:
    print("Número no encontrado")