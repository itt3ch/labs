import unittest
import sys
import os


sys.path.append('../src')
from minCabelsLength import read_matrix_from_file, floyd_warshall, find_min_distance_sum

class TestMatrixFunctions(unittest.TestCase):
    def setUp(self):
        self.test_matrix = [
            [0, 2, 5],
            [2, 8, 4],
            [5, 4, 0]
        ]

        current_dir = os.path.dirname(__file__)

        self.filename = os.path.join(current_dir, 'islands.csv')

    def test_read_matrix_from_file(self):
        expected_matrix = self.test_matrix
        result_matrix = read_matrix_from_file(self.filename)
        self.assertEqual(result_matrix, expected_matrix)

    def test_floyd_warshall(self):
        expected_matrix = [
            [0, 2, 5],
            [2, 4, 4],
            [5, 4, 0]
        ]
        floyd_warshall(self.test_matrix)
        self.assertEqual(self.test_matrix, expected_matrix)

    def test_find_min_distance_sum(self):
        floyd_warshall(self.test_matrix)
        result = find_min_distance_sum(self.test_matrix)
        expected_sum = 0 + 2 + 0
        self.assertEqual(result, expected_sum)

if __name__ == "__main__":
    unittest.main()
