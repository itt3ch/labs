import unittest
import sys
sys.path.append('../src')
from rabin_karp import func_karp
class TestFuncKarp(unittest.TestCase):

    def test_func_karp(self):
        haystack = "programming program"
        needle = "program"
        expected_indices = [0, 12]
        self.assertEqual(func_karp(haystack, needle), expected_indices)


if __name__ == '__main__':
    unittest.main()
