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
        "EC": [[0, 1, 2, 0], [1, 0, 3, 4], [2, 3, 0, 0], [0, 4, 0, 0]]
    }
}
```

`EC[i][j]` es el costo de la arista `V[i] → V[j]`; `0` significa que no hay arista.
Opcionalmente se puede indicar `"origen": "S"`; si no se indica, el origen es `V[0]`.

### Formato de salida

```json
{ "A": ["S", "A", 1], "B": ["S", "B", 2], "T": ["S", "A", "T", 5] }
```

Para cada vértice alcanzable: el camino desde el origen y, al final, su costo.

## Uso de IA

La estructura del repositorio (carpetas, lectura del JSON, test) fue preparada con
Claude Code. Los algoritmos fueron implementados por el estudiante.
