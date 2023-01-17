from algorithms.random_array import random_array


def selection_sort(array):
    for i in range(len(array) - 1):
        max_element_index = 0
        for j in range(len(array) - i):
            if array[j] > array[max_element_index]:
                max_element_index = j
        array[len(array) - i - 1], array[max_element_index] = array[max_element_index], array[len(array) - i - 1]
    return array


print(selection_sort(random_array(10)))
