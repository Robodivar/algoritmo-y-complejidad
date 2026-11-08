# Benchmark de algoritmos de ordenamiento

Comparación, sobre los mismos datos, de cinco algoritmos de ordenamiento: **Selección, Inserción, Burbuja, Quicksort y Heapsort**, relacionando los tiempos medidos con su complejidad teórica.

## Contenido

| Archivo | Descripción |
|---|---|
| `benchmark.py` | Implementación de los cinco algoritmos y del benchmark |
| `resultados.csv` | Resultados completos (orden, n, algoritmo, segundos) |

## Cómo ejecutarlo

Requiere Python 3.8 o superior. No tiene dependencias externas.

```bash
python3 benchmark.py
```

Imprime los tiempos en consola y regenera `resultados.csv`. La ejecución completa tarda aproximadamente un minuto.

## Metodología

- **Mismos datos:** para cada combinación (orden inicial, n) se genera un único conjunto de datos y cada algoritmo recibe una copia idéntica.
- **Órdenes iniciales:** aleatorio, ordenado, inverso y casi ordenado (~1 % de elementos fuera de lugar).
- **Tamaños:** n = 500, 1000, 2000 y 4000.
- **Repeticiones:** 3 por caso; se reporta la mediana. Semilla fija (42) para reproducibilidad.
- **Verificación:** después de cada corrida se comprueba que el resultado coincide con `sorted()`.
- **Detalles de implementación:**
  - Burbuja corta si una pasada no realiza intercambios.
  - Quicksort usa pivote mediana de tres y partición de Hoare, recursa sobre la partición menor e itera sobre la mayor.
  - Heapsort es in-place, con construcción del heap en O(n).

## Resultados (n = 4000, en ms)

| Orden inicial | Selección | Inserción | Burbuja | Quicksort | Heapsort |
|---|---|---|---|---|---|
| Aleatorio | 248,8 | 233,5 | 512,7 | **3,5** | 6,7 |
| Ordenado | 203,2 | 0,27 | **0,13** | 1,9 | 6,6 |
| Inverso | 198,6 | 404,8 | 611,7 | **1,8** | 5,4 |
| Casi ordenado | 180,5 | 6,7 | 250,0 | **1,8** | 6,2 |

## Análisis

### Más rápido y más lento por orden inicial

- **Aleatorio:** el más rápido es Quicksort (~n log n comparaciones con poco trabajo por paso) y el más lento Burbuja (~n²/2 comparaciones y ~n²/4 intercambios).
- **Ordenado:** el más rápido es Burbuja con bandera (una sola pasada, O(n)); Inserción también es O(n). El más lento es Selección, que siempre hace ~n²/2 comparaciones.
- **Inverso:** el más rápido es Quicksort y el más lento Burbuja (peor caso de Inserción y Burbuja; Burbuja paga un intercambio completo por cada inversión).
- **Casi ordenado:** el más rápido es Quicksort; Inserción queda cerca (costo O(n + inversiones)); el más lento es Burbuja, que casi no se beneficia del orden parcial.

### Duplicación de n

Razón promedio t(2n)/t(n) en los tres saltos medidos:

| Orden | Selección | Inserción | Burbuja | Quicksort | Heapsort |
|---|---|---|---|---|---|
| Aleatorio | 4,19 | 4,11 | 4,17 | 2,21 | 2,33 |
| Ordenado | 4,08 | 2,15* | 2,00* | 2,24 | 2,30 |
| Inverso | 3,96 | 4,01 | 4,33 | 2,06 | 2,21 |
| Casi ordenado | 3,93 | 4,04 | 4,46 | 2,10 | 2,14 |

\* Casos lineales (O(n)), donde se espera una razón de ≈2.

- Los algoritmos cuadráticos se multiplican por ≈4 cuando son Θ(n²).
- Quicksort y Heapsort se multiplican por algo más de 2, como predice la teoría: (2n·log 2n)/(n·log n) = 2·(1 + 1/log₂ n), es decir, entre 2,2 y 2,3 para estos tamaños.

### Quicksort frente a Heapsort

Ambos son O(n log n), pero Quicksort resultó entre 1,5 y 3,7 veces más rápido por sus constantes:

- **Localidad de memoria:** Quicksort recorre el arreglo en forma secuencial (buena para la caché); Heapsort salta entre posiciones i y 2i+1.
- **Menos comparaciones:** Heapsort hace ~2n log₂ n comparaciones contra ~1,39 n log₂ n de Quicksort.
- **Predicción de saltos:** los bucles de partición son simples y predecibles.
- **Adaptación al orden:** Heapsort no se beneficia de datos ya ordenados porque primero destruye el orden al construir el heap.

La ventaja de Heapsort es la garantía de O(n log n) en el peor caso y O(1) de memoria extra.

## Limitaciones

- Los tiempos corresponden a Python (lenguaje interpretado): las razones entre algoritmos y el crecimiento son comparables con la teoría, pero los valores absolutos no.
- Con 3 repeticiones por caso, los tiempos menores a ~1 ms tienen ruido apreciable.
