import json
import unittest
from pathlib import Path

from algoritmos.bfs_dummy import construir_g_prima, resolver

EJEMPLOS = Path(__file__).parent.parent / "ejemplos"
PIZARRA = json.loads((EJEMPLOS / "grafo_pizarra.json").read_text())["grafo"]


class TestBfsDummy(unittest.TestCase):
    def test_grafo_pizarra(self):
        self.assertEqual(
            resolver(PIZARRA, "S"),
            {"A": ["S", "A", 1], "B": ["S", "B", 2], "T": ["S", "A", "T", 5]},
        )

    def test_g_prima_como_el_dibujo(self):
        # sin dirección: 0 + 1 + 2 + 3 = 6 dummies, cada cadena de ida y vuelta
        adj = construir_g_prima(PIZARRA["V"], PIZARRA["EC"])
        self.assertEqual(len(adj) - 4, 6)
        self.assertEqual(adj["d1"], ["S", "B"])

    def test_arista_con_direccion(self):
        # S -> A existe, A -> S no: desde A no se llega a S
        grafo = {"V": ["S", "A"], "EC": [[None, 2], [None, None]]}
        self.assertEqual(resolver(grafo, "S"), {"A": ["S", "A", 2]})
        self.assertEqual(resolver(grafo, "A"), {})

    def test_inalcanzable_no_aparece(self):
        grafo = {"V": ["S", "A", "Z"], "EC": [[None, 3, None], [None, None, None], [None, None, None]]}
        self.assertEqual(resolver(grafo, "S"), {"A": ["S", "A", 3]})

    def test_peso_cero_se_rechaza(self):
        grafo = {"V": ["S", "A"], "EC": [[None, 0], [None, None]]}
        with self.assertRaises(ValueError):
            resolver(grafo, "S")


if __name__ == "__main__":
    unittest.main()
