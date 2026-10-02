# Algoritmos Avanzados

Biblioteca de algoritmos del curso CMP-4007 (USFQ).

## Algoritmos

| Módulo | Qué hace | Referencia |
|---|---|---|
| `algoritmos/bfs_dummy.py` | Camino más corto con costos enteros positivos: BFS sobre G' con nodos dummy | DPV §4.4.1, p. 119 |

## Uso

```bash
python3 -m algoritmos.bfs_dummy ejemplos/grafo_pizarra.json
python3 -m unittest
```

### Formato de entrada

```json
{
    "grafo": {
        "V": ["S", "A", "B", "T"],
        "EC": [[null, 1, 2, null], [1, null, 3, 4], [2, 3, null, null], [null, 4, null, null]]
    }
}
```

`EC[i][j]` es el costo de la arista `V[i] → V[j]`; `null` significa que no hay arista (así `0` queda libre como peso).
Este algoritmo solo acepta costos enteros positivos (DPV §4.4.1).
Opcionalmente se puede indicar `"origen": "S"`; si no se indica, el origen es `V[0]`.

### Formato de salida

```json
{ "A": ["S", "A", 1], "B": ["S", "B", 2], "T": ["S", "A", "T", 5] }
```

Para cada vértice alcanzable: el camino desde el origen y, al final, su costo.

## Uso de IA

La estructura del repositorio y la implementación de `bfs_dummy.py` fueron hechas
con Claude Code (Anthropic), siguiendo DPV §4.2 y §4.4.1. El estudiante revisó y
entiende el código.
