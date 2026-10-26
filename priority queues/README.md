# Soluciones LeetCode: Priority Queue y Hash Table

Lenguaje: Python 3

| Estructura | Problema | Dificultad | Solucion | Complejidad |
|---|---|---|---|---|
| Priority Queue (heap) | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | [`priority-queue/kth_largest_element.py`](priority-queue/kth_largest_element.py) | O(n log k) tiempo, O(k) espacio |
| Hash Table | [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [`hash-table/two_sum.py`](hash-table/two_sum.py) | O(n) tiempo, O(n) espacio |

## Enfoque

- **Kth Largest:** min-heap de tamano k con `heapq`. Cada elemento se inserta y, si el heap supera k elementos, se saca el minimo. La raiz final es el k-esimo mayor.
- **Two Sum:** un diccionario guarda los valores ya vistos con su indice. Para cada numero se consulta en O(1) si existe su complemento.

## Ejecutar los tests

```bash
python priority-queue/kth_largest_element.py
python hash-table/two_sum.py
```
