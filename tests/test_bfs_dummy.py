import json
import unittest
from pathlib import Path

from algoritmos.bfs_dummy import resolver

EJEMPLOS = Path(__file__).parent.parent / "ejemplos"


class TestBfsDummy(unittest.TestCase):
    def test_grafo_pizarra(self):
        grafo = json.loads((EJEMPLOS / "grafo_pizarra.json").read_text())["grafo"]
        self.assertEqual(
            resolver(grafo, "S"),
            {"A": ["S", "A", 1], "B": ["S", "B", 2], "T": ["S", "A", "T", 5]},
        )

    def test_inalcanzable_no_aparece(self):
        grafo = {"V": ["S", "A", "Z"], "EC": [[None, 3, None], [None, None, None], [None, None, None]]}
        self.assertEqual(resolver(grafo, "S"), {"A": ["S", "A", 3]})

    def test_peso_cero_se_rechaza(self):
        grafo = {"V": ["S", "A"], "EC": [[None, 0], [None, None]]}
        with self.assertRaises(ValueError):
            resolver(grafo, "S")


if __name__ == "__main__":
    unittest.main()
