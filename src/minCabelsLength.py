import csv
import os

def read_matrix_from_file(filename):
    """
    Зчитує матрицю з файла та повертає її у вигляді списку списків цілих чисел.

    :param filename: Ім'я файлу, з якого буде зчитана матриця.
    :type filename: str
    :return: Матриця, представлена у вигляді списку списків цілих чисел.
    :rtype: list of lists of int
    """
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(element) for element in line.strip().split(',')]
            matrix.append(row)
    return matrix

def floyd_warshall(matrix):
    """
    Виконує алгоритм Флойда-Уоршелла для знаходження найкоротших шляхів між усіма парами вершин у графі.

    :param matrix: Матриця відстаней між вершинами графу.
    :type matrix: list of lists of int
    """
    n = len(matrix)
    for via_vertex in range(n):
        for start_vertex in range(n):
            for end_vertex in range(n):
                matrix[start_vertex][end_vertex] = min(matrix[start_vertex][end_vertex], matrix[start_vertex][via_vertex] + matrix[via_vertex][end_vertex])

def find_min_distance_sum(matrix):
    """
    Обчислює суму мінімальних значень у кожному рядку матриці.

    :param matrix: Матриця, представлена у вигляді списку списків цілих чисел.
    :type matrix: list of lists of int
    :return: Сума мінімальних значень у кожному рядку матриці.
    :rtype: int
    """
    n = len(matrix)
    min_distances_sum = 0
    for i in range(n):
        min_distance = min(matrix[i])
        min_distances_sum += min_distance
    return min_distances_sum

def main():
    """
    Головна функція програми.
    """
    filename = 'islands.csv'
    matrix = read_matrix_from_file(filename)
    floyd_warshall(matrix)
    min_distance_sum = find_min_distance_sum(matrix)
    print("Сума мінімальних значень у кожному рядку матриці:", min_distance_sum)

if __name__ == "__main__":
    main()
