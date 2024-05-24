import unittest
import sys
sys.path.append('../src')
from sum_of_three import finding_nums


class FindingNums(unittest.TestCase):
    def test_1(self):
        array = [2, 6, 9, 1, 6, 2]
        p = 9
        expected_result = True
        self.assertEqual(finding_nums(array, p), expected_result)

    def test_2(self):
        array = [2, 8, 1, 9, 2, 7, 4, 6]
        p = 2
        expected_result = False
        self.assertEqual(finding_nums(array, p), expected_result)

    def test_3(self):
        array = [1, 2, 3]
        p = 6
        expected_result = True
        self.assertEqual(finding_nums(array, p), expected_result)