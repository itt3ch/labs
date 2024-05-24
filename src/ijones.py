from typing import List, Tuple


def find_same_letters_pos(corridor: List[str], W: int, H: int) -> List[Tuple[int, int]]:
    letter_positions = {}
    for row in range(H):
        for col in range(W):
            letter = corridor[row][col]
            if letter not in letter_positions:
                letter_positions[letter] = []
            letter_positions[letter].append((row, col))
    return letter_positions


def count_paths(corridor: List[str], W: int, H: int) -> int:
    paths_count = [[0 for _ in range(W)] for _ in range(H)]

    for curr_row_index in range(H):
        paths_count[curr_row_index][0] = 1

    letter_positions = find_same_letters_pos(corridor, W, H)

    for curr_col_index in range(1, W):
        for curr_row_index in range(H):
            paths_count[curr_row_index][curr_col_index] += paths_count[curr_row_index][curr_col_index - 1]

            curr_letter = corridor[curr_row_index][curr_col_index]
            for (target_row, target_col) in letter_positions[curr_letter]:
                if target_col == curr_col_index - 1:
                    paths_count[curr_row_index][curr_col_index] += paths_count[target_row][target_col]

    if curr_col_index == 1:
            checked_letters = set()
            for curr_row_index in range(H):
                letter = corridor[curr_row_index][curr_col_index]
                if letter not in checked_letters:
                    paths_count[curr_row_index][curr_col_index] += 1
                    checked_letters.add(letter)

    return paths_count[0][W - 1] + paths_count[H - 1][W - 1]- 2


def read_input(input_filename) -> Tuple[int, int, list]:
    file = open(input_filename, "r")
    W, H = map(int, file.readline().split(" "))
    corridor = [file.readline().strip() for _ in range(H)]

    return W, H, corridor


def create_output(output_filename, result: int):
    file = open(output_filename, "w")
    file.write(str(result))
    file.close()


input_filename = "ijones.in"
output_filename = ("ijones.out")
W, H, corridor = read_input(input_filename)
paths = count_paths(corridor, W, H)
create_output(output_filename, paths)