import unittest
import sys
sys.path.append('../src')
from pumpkins import num_of_pumpkins


class TestSolution(unittest.TestCase):
    def test_1(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]

        expected_result = "25 24 23 22 21 16 17 18 19 20 15 14 13 12 11 6 7 8 9 10 5 4 3 2 1"
        self.assertEqual(num_of_pumpkins(matrix), expected_result)

    def test_2(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]

        expected_result = '5 6 7 8 4 3 2 1'
        self.assertEqual(num_of_pumpkins(matrix), expected_result)



    def test_3(self):
        matrix = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        expected_result = "6 5 4 3 2 1"
        self.assertEqual(num_of_pumpkins(matrix), expected_result)