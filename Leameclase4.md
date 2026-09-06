# Ecuaciones de Recurrencia y Algoritmo Divide y Vencerás

Este repositorio resuelve seis ecuaciones de recurrencia mediante el **Teorema Maestro** (o árbol de recursión cuando no aplica), las verifica empíricamente con código (`ecuaciones_recurrencia.py`) y expone en código un algoritmo real de **Divide y Vencerás**: `Merge Sort` (`merge_sort.py`).

## Ecuaciones de recurrencia

Aquí el trabajo por llamada es **O(1)** (una constante), no `O(n)`, salvo en las ecuaciones 3 y 6 donde se indica `O(n²)` explícitamente. Esto cambia el resultado de algunas ecuaciones respecto a asumir `O(n)` por defecto — ver nota sobre la Ecuación 5 más abajo.

| # | Ecuación | Caso / Método | Resultado |
|---|---|---|---|
| 1 | `T(n) = 2T(n/2) + O(1)` | Maestro, caso 1 | `Θ(n)` |
| 2 | `T(n) = 4T(n/2) + O(1)` | Maestro, caso 1 | `Θ(n²)` |
| 3 | `T(n) = 2T(n/2) + O(n²)` | Maestro, caso 3 | `Θ(n²)` |
| 4 | `T(n) = T(n-1) + O(1)` | Suma directa (decrease-and-conquer) | `Θ(n)` |
| 5 | `T(n) = T(n/3) + T(2n/3) + O(1)` | Akra-Bazzi / árbol de recursión | `Θ(n)` |
| 6 | `T(n) = 3T(n/4) + O(n²)` | Maestro, caso 3 | `Θ(n²)` |

**Teorema Maestro**: para `T(n) = aT(n/b) + f(n)`, se compara `f(n)` con `n^(log_b a)`:

- **Caso 1** — `f(n)` es polinómicamente menor → `T(n) = Θ(n^(log_b a))`.
- **Caso 2** — `f(n)` es del mismo orden → `T(n) = Θ(n^(log_b a) · log n)`.
- **Caso 3** — `f(n)` es polinómicamente mayor y cumple la condición de regularidad → `T(n) = Θ(f(n))`.

Las ecuaciones 4 y 5 no encajan en el Teorema Maestro estándar (decremento en vez de división, o división desigual) y se resuelven expandiendo la recurrencia término a término (o con el método de Akra-Bazzi).

### Nota sobre la Ecuación 5: `O(1)` vs `O(n)` por llamada

Es un error común confundir dos versiones de esta recurrencia:

- **`T(n) = T(n/3) + T(2n/3) + O(1)`** (la de este repositorio): cada llamada hace trabajo constante. Resultado: **Θ(n)**. Se verificó ejecutando `ecuacion_5(n)` para `n` de 8 a 32768: la razón `ecuacion_5(n) / n` da exactamente `1.0` en todos los casos.
- **`T(n) = T(n/3) + T(2n/3) + O(n)`** (variante con trabajo lineal por llamada, análoga a la fase de combinación de un algoritmo tipo *quickselect* o *mergesort* con partición desigual): ahí sí el resultado es **Θ(n log n)**, porque el trabajo por nivel es `O(n)` y la profundidad del árbol es `O(log n)` (dominada por la rama 2/3).

La diferencia se puede justificar formalmente con el **método de Akra-Bazzi**: se busca `p` tal que `(1/3)^p + (2/3)^p = 1`, lo cual se cumple con `p = 1`. Luego `T(n) = Θ(n^p (1 + ∫₁ⁿ f(u)/u^(p+1) du))`. Con `f(u) = O(1)`, la integral converge a una constante → `Θ(n)`. Con `f(u) = O(u)`, la integral da `Θ(log n)` → `Θ(n log n)`.

### Corrección de un bug (recursión infinita)

La implementación original de `ecuacion_5` usaba `parte_1 = n // 3`. Para `n = 2`, esto da `parte_1 = 0` y `parte_2 = n - 0 = n`, es decir, la función se vuelve a llamar con el **mismo** valor de `n` — recursión infinita (`RecursionError`). Se corrigió con `parte_1 = max(1, n // 3)`, garantizando que ambas partes sean siempre estrictamente menores que `n`.

## Algoritmo investigado: Merge Sort

`ordenar_por_mezcla()` implementa el paradigma Divide y Vencerás sobre un arreglo de números.

- **Divide**: el arreglo de tamaño `n` se parte en dos mitades de tamaño `n/2` usando el índice medio.
- **Vencerás (conquista)**: cada mitad se ordena recursivamente. El caso base es un arreglo de 0 o 1 elementos, que ya está ordenado.
- **Combina**: `mezclar()` fusiona las dos mitades ordenadas en un único arreglo ordenado, comparando elemento por elemento. Este paso cuesta `O(n)`.

No usa `sorted()`, `list.sort()` ni ninguna función de ordenamiento incorporada del lenguaje.

### Complejidad

| Operación | Complejidad |
|---|---|
| Divide (calcular mitad) | O(1) |
| Combina (`mezclar`) | O(n) por nivel |
| Recurrencia total | `T(n) = 2T(n/2) + O(n)` |
| Resultado | `Θ(n log n)` en todos los casos (mejor, promedio, peor) |
| Espacio auxiliar | `O(n)` (arreglos temporales en la mezcla) |

Esta recurrencia es exactamente la **Ecuación 1** de la tabla anterior: cada nivel del árbol de recursión hace un trabajo total de `O(n)`, y hay `log₂ n` niveles hasta llegar al caso base, de ahí el `n log n`.

## Archivos

- `merge_sort.py` — Implementación de `ordenar_por_mezcla()` y `mezclar()`, con comentarios que marcan la fase de división, conquista y combinación.
- `main.py` — Punto de entrada: ordena un arreglo de ejemplo y muestra el resultado paso a paso.
