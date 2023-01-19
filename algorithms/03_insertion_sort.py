from algorithms.random_array import random_array


def insertion_sort(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            count = array[i]
            j = i - 1
            while array[j] > count and j >= 0:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = count
    return array


print(insertion_sort(random_array(5)))
