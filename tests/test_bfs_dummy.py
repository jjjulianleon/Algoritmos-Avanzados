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


if __name__ == "__main__":
    unittest.main()
