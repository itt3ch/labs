from collections import deque
import os

def is_valid(x, y, matrix):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] != 0


def bfs(x, y, matrix, checked):
    queue = deque([(x, y, 0)])
    while queue:
        x, y, steps = queue.popleft()
        if (x, y) in checked or not is_valid(x, y, matrix):
            continue
        if y == len(matrix[0]) - 1:
            return steps + 1
        checked.add((x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            queue.append((x + dx, y + dy, steps + 1))
    return float('inf')

def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line:
                matrix.append(list(map(int, stripped_line.split(','))))
    return matrix



def write_result_to_file(result, filename):
    with open(filename, 'w') as file:
        file.write(str(result))

def safest_way(matrix):
    if not matrix or not matrix[0]:
        return -1

    min_steps = float('inf')
    for i in range(len(matrix)):

        if matrix[i][0] == 1:
            min_steps = min(min_steps, bfs(i, 0, matrix, set()))

    return min_steps if min_steps != float('inf') else -1


def main():
    input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    matrix = read_matrix_from_file(input_file_path)
    shortest_path_length = safest_way(matrix)
    write_result_to_file(shortest_path_length, 'output.txt')

if __name__ == "__main__":
    main()

