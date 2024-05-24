def binary_search(x, left, right, array):
    while left <= right:
        center = (left + right) // 2
        if array[center] == x:
            return True
        elif array[center] < x:
            left = center + 1
        else:
            right = center - 1
    return False


def finding_nums(array, p):
    sorted_arr = sorted(array)
    for i in range(len(sorted_arr) - 2):
        j = i + 1
        k = len(sorted_arr) - 1
        while j < k:
            num_sum = sorted_arr[j] + sorted_arr[k]
            if num_sum + sorted_arr[i] == p:
                return True
            elif num_sum < p:
                if binary_search(p - num_sum, j + 1, k, sorted_arr):
                    return True
                else:
                    j += 1

            else:
                k -= 1
    return False