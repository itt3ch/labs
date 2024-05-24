def num_of_pumpkins(matrix):
    result = []
    for i in range(len(matrix)-1,-1,-1):
        if i % 2 != 0:
            result.extend((matrix[i]))
        else:
            result.extend(matrix[i][::-1])

    return " ".join(str(int(i)) for i in result)