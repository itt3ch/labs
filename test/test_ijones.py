import unittest
import tempfile
import os
import sys
from contextlib import contextmanager


sys.path.append('../src')
from ijones import read_input, count_paths
@contextmanager
def create_temp_file(content: str):
    temp = tempfile.NamedTemporaryFile(delete=False)
    try:
        temp.write(content.encode())
        temp.close()
        yield temp.name
    finally:
        os.remove(temp.name)

def read_input(input_filename) -> tuple[int, int, list]:
    with open(input_filename, "r") as file:
        W, H = map(int, file.readline().split())
        corridor = [file.readline().strip() for _ in range(H)]
    return W, H, corridor

class TestIJones(unittest.TestCase):

    def test_example1(self):
        input_data = "3 3\naaa\ncab\ndef\n"
        expected_output = "5"
        with create_temp_file(input_data) as input_filename:
            W, H, corridor = read_input(input_filename)
            result = count_paths(corridor, W, H)
            self.assertEqual(str(result), expected_output)

    def test_example2(self):
        input_data = "10 1\nabcdefaghi\n"
        expected_output = "0"
        with create_temp_file(input_data) as input_filename:
            W, H, corridor = read_input(input_filename)
            result = count_paths(corridor, W, H)
            self.assertEqual(str(result), expected_output)

    def test_example3(self):
        input_data = "7 6\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\n"
        expected_output = "235296"
        with create_temp_file(input_data) as input_filename:
            W, H, corridor = read_input(input_filename)
            result = count_paths(corridor, W, H)
            self.assertEqual(str(result), expected_output)

if __name__ == "__main__":
    unittest.main()