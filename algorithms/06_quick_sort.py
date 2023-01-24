import random

from algorithms.random_array import random_array


def quick_sort(array, fst, lst):
    if fst >= lst:
        return

    i, j = fst, lst
    pivot = array[random.randint(fst, lst)]

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quick_sort(array, fst, j)
    quick_sort(array, i, lst)
    return array


if __name__ == '__main__':
    arr = random_array(10)
    print(quick_sort(arr, 0, len(arr) - 1))
