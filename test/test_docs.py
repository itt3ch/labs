import unittest
from collections import defaultdict
import sys
sys.path.append('../src')
from docs import topological_sort

class TestTopologicalSort(unittest.TestCase):
    def test_topological_sort(self):
        graph = defaultdict(list)
        graph["visa"] = ["foreignpassport", "hotel", "bankstatement"]
        graph["bankstatement"] = ["nationalpassport"]
        graph["hotel"] = ["creditcard"]
        graph["creditcard"] = ["nationalpassport"]
        graph["nationalpassport"] = ["birthcertificate"]
        graph["foreignpassport"] = ["nationalpassport", "militarycertificate"]
        graph["militarycertificate"] = ["nationalpassport"]

        expected_output = ["foreignpassport", "militarycertificate", "visa", "bankstatement", "hotel", "creditcard", "nationalpassport", "birthcertificate"]

        self.assertEqual(topological_sort(graph), expected_output)

if __name__ == "__main__":
    unittest.main()

