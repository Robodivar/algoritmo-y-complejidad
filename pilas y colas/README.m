# Problemas de Pilas y Colas - LeetCode
## Lenguaje
Python 3

## 1. Pila (Stack) - Valid Parentheses

**Problema:** LeetCode 20 - Valid Parentheses

**Enlace:** https://leetcode.com/problems/valid-parentheses/

### Descripción
Dada una cadena formada por `()`, `[]` y `{}`, se debe determinar si los paréntesis están correctamente abiertos y cerrados.

### Solución
Se utiliza una pila. Cada paréntesis de apertura se guarda en la pila. Cuando aparece uno de cierre, se compara con el elemento que está en la cima de la pila.

### Complejidad
- Tiempo: **O(n)**, porque se recorre la cadena una sola vez.
- Espacio: **O(n)** en el peor caso, si todos los caracteres son paréntesis de apertura.

---

## 2. Cola (Queue) - Number of Islands

**Problema:** LeetCode 200 - Number of Islands

**Enlace:** https://leetcode.com/problems/number-of-islands/

### Descripción
Dada una matriz formada por `1` (tierra) y `0` (agua), se debe contar cuántas islas existen. Las partes de tierra conectadas horizontal o verticalmente forman una isla.

### Solución
Se utiliza una cola para realizar un recorrido BFS. Cuando se encuentra una celda con `1`, se considera una nueva isla y se agregan a la cola sus vecinos conectados.

### Complejidad
- Tiempo: **O(m × n)**, porque cada celda se procesa como máximo una vez.
- Espacio: **O(m × n)** en el peor caso por la cola utilizada durante el recorrido.


