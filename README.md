# TAD Pila - Rodrigo Vargas

## Objetivo
Implementar el TAD Pila en Python mediante dos representaciones: arreglo dinámico y lista enlazada, sin usar estructuras nativas de pila o lista.

La Pila trabaja con disciplina LIFO: el último elemento que entra es el primero que sale.

## Seis operaciones
- `crear()` crea una pila vacía.
- `apilar(x)` agrega `x` al tope.
- `desapilar()` retira y devuelve el elemento del tope.
- `cima()` consulta el tope sin retirarlo.
- `estaVacia()` indica si la pila está vacía.
- `tamaño()` devuelve la cantidad de elementos.

La Clase 2 permite que, en una implementación orientada a objetos, `desapilar()` modifique la pila y devuelva el elemento retirado, siempre que la decisión quede documentada.

## Arreglo dinámico
`PilaArreglo` mantiene un arreglo de referencias, una capacidad y un índice `__tope`. Cuando se llena, duplica su capacidad y copia los elementos.

No usa `list`, `deque`, `Stack` ni colecciones de pila/lista.

Complejidad:
- apilar: O(1) amortizado; O(n) al redimensionar.
- desapilar: O(1).
- cima: O(1).
- estaVacia: O(1).
- tamaño: O(1).

## Lista enlazada
`PilaLista` usa una clase `Nodo` propia. Cada nodo contiene `dato` y `siguiente`. La cabeza representa el tope.

No usa `list`, `deque`, `Stack` ni colecciones de pila/lista.

Complejidad:
- apilar: O(1).
- desapilar: O(1).
- cima: O(1).
- estaVacia: O(1).
- tamaño: O(1).

## Manejo de errores
`desapilar()` y `cima()` lanzan `IndexError` con un mensaje descriptivo cuando la pila está vacía.

## Pruebas
`main.py` prueba las seis operaciones, los errores y compara ambas implementaciones con la secuencia `5, 8, 13, 21, 34`.

Ejecutar:

```text
python main.py
```

Resultado esperado:

```text
TODAS LAS PRUEBAS FINALIZARON CORRECTAMENTE.
```
