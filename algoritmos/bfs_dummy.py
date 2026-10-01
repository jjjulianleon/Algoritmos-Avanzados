"""Camino más corto con BFS + nodos dummy.

Referencia: DPV (Dasgupta, Papadimitriou, Vazirani), cap. 4,
§4.2 (BFS, Fig. 4.3, p. 117) y §4.4.1 "An adaptation of breadth-first search" (p. 119).

Uso:
    python -m algoritmos.bfs_dummy ejemplos/grafo_pizarra.json
"""

import json
import sys
from collections import deque  # cola para el BFS: append = inject, popleft = eject


# --- Paso 1 ---------------------------------------------------------------
def construir_g_prima(V, EC):
    """Construye G' reemplazando cada arista de costo l por l aristas de costo 1.

    V  : lista de nombres de vértices, p. ej. ["S", "A", "B", "T"]
    EC : matriz de costos; EC[i][j] = costo de la arista V[i] -> V[j], 0 = no hay arista.

    Devuelve la lista de adyacencia de G': dict {nodo: [vecinos]}.
    Los nodos originales conservan su nombre; los dummy deben tener nombres
    que no choquen con V.
    """
    raise NotImplementedError("Paso 1")


# --- Paso 2 ---------------------------------------------------------------
def bfs(adj, s):
    """BFS de DPV Fig. 4.3 sobre G', con prev(v) agregado.

    Devuelve (dist, prev): dos dicts sobre todos los nodos de G'.
    """
    raise NotImplementedError("Paso 2")


# --- Paso 3 ---------------------------------------------------------------
def reconstruir_camino(prev, s, v, V):
    """Sigue prev desde v hasta s y devuelve el camino SOLO con nodos de V.

    Ejemplo: s="S", v="T"  ->  ["S", "A", "T"]
    """
    raise NotImplementedError("Paso 3")


# --- Paso 4 ---------------------------------------------------------------
def resolver(grafo, s):
    """Une los pasos 1-3 y arma la salida.

    Formato: {v: [s, ..., v, costo]} para cada v != s alcanzable desde s.
    Ejemplo: {"A": ["S", "A", 1], "B": ["S", "B", 2], "T": ["S", "A", "T", 5]}
    """
    raise NotImplementedError("Paso 4")


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        datos = json.load(f)
    grafo = datos["grafo"]
    s = datos.get("origen", grafo["V"][0])  # si el JSON no dice origen, se usa el primer vértice
    print(json.dumps(resolver(grafo, s), indent=4, ensure_ascii=False))
