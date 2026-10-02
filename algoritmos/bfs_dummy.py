"""Camino más corto con BFS + nodos dummy.

Referencia: DPV (Dasgupta, Papadimitriou, Vazirani), cap. 4,
§4.2 (BFS, Fig. 4.3, p. 117) y §4.4.1 "An adaptation of breadth-first search" (p. 119).

Costo: Θ(|V| + L) en el peor caso, con L = suma de todos los costos,
porque G' tiene a lo más |V| + L nodos y exactamente L aristas.

Uso:
    python -m algoritmos.bfs_dummy ejemplos/grafo_pizarra.json
"""

import json
import sys
from pathlib import Path
from collections import deque  # cola para el BFS: append = inject, popleft = eject

INF = float("inf")


# --- Paso 1 ---------------------------------------------------------------
def construir_g_prima(V, EC):
    """Construye G' reemplazando cada arista de costo l por l aristas de costo 1.

    V  : lista de nombres de vértices, p. ej. ["S", "A", "B", "T"]
    EC : matriz de costos; EC[i][j] = costo de la arista V[i] -> V[j], None = no hay arista
         (en el JSON se escribe null). Los costos deben ser enteros positivos.

    Devuelve la lista de adyacencia de G': dict {nodo: [vecinos]}.
    """
    adj = {v: [] for v in V}
    contador = 0

    for i in range(len(V)):
        for j in range(len(V)):
            l = EC[i][j]
            if l is None:
                continue
            if type(l) is not int or l < 1:
                raise ValueError(f"Costo {l} en {V[i]}->{V[j]}: solo se aceptan enteros positivos")

            # cadena V[i] -> d -> d -> ... -> V[j] con l - 1 dummies (DPV p. 119)
            x = V[i]
            for _ in range(l - 1):
                contador += 1
                d = "d" + str(contador)
                adj[x].append(d)
                adj[d] = []
                x = d
            adj[x].append(V[j])

    return adj


# --- Paso 2 ---------------------------------------------------------------
def bfs(adj, s):
    """BFS de DPV Fig. 4.3 sobre G', con prev(v) agregado.

    Devuelve (dist, prev): dos dicts sobre todos los nodos de G'.
    """
    dist = {u: INF for u in adj}
    prev = {u: None for u in adj}
    dist[s] = 0
    Q = deque([s])

    while Q:
        u = Q.popleft()                # eject(Q)
        for v in adj[u]:
            if dist[v] == INF:
                Q.append(v)            # inject(Q, v)
                dist[v] = dist[u] + 1
                prev[v] = u

    return dist, prev


# --- Paso 3 ---------------------------------------------------------------
def reconstruir_camino(prev, s, v, V):
    """Sigue prev desde v hasta s y devuelve el camino SOLO con nodos de V.

    Ejemplo: s="S", v="T"  ->  ["S", "A", "T"]
    """
    camino = []
    while v is not None:               # prev(s) = None, ahí termina
        camino.append(v)
        v = prev[v]

    originales = set(V)
    return [u for u in reversed(camino) if u in originales]


# --- Paso 4 ---------------------------------------------------------------
def resolver(grafo, s):
    """Une los pasos 1-3 y arma la salida.

    Formato: {v: [s, ..., v, costo]} para cada v != s alcanzable desde s.
    Ejemplo: {"A": ["S", "A", 1], "B": ["S", "B", 2], "T": ["S", "A", "T", 5]}
    """
    V = grafo["V"]
    if s not in V:
        raise ValueError(f"El origen {s} no está en V")

    adj = construir_g_prima(V, grafo["EC"])
    dist, prev = bfs(adj, s)

    return {
        v: reconstruir_camino(prev, s, v, V) + [dist[v]]
        for v in V
        if v != s and dist[v] != INF
    }


if __name__ == "__main__":
    # sin argumento (p. ej. botón Run de VS Code) se usa el ejemplo de la pizarra
    ruta = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent.parent / "ejemplos" / "grafo_pizarra.json"
    with open(ruta) as f:
        datos = json.load(f)
    grafo = datos["grafo"]
    s = datos.get("origen", grafo["V"][0])  # si el JSON no dice origen, se usa el primer vértice
    print(json.dumps(resolver(grafo, s), indent=4, ensure_ascii=False))
