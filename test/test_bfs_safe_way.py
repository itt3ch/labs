import unittest
import sys
sys.path.append('../src')
from bfs_safe_way import safest_way
class TestSafestPath(unittest.TestCase):
    def test_safest_way(self):
        matrix1 = [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1]
        ]
        self.assertEqual(safest_way(matrix1), 7)

        matrix2 = [
            [1, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 1, 1]
        ]
        self.assertEqual(safest_way(matrix2), 4)

        matrix3 = [
            [0, 0, 1],
            [1, 0, 1],
            [1, 0, 1]
        ]
        self.assertEqual(safest_way(matrix3), -1)

        matrix4 = [[]]
        self.assertEqual(safest_way(matrix4), -1)
        matrix5 = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.assertEqual(safest_way(matrix5), -1)
if __name__ == "__main__":
    unittest.main()
