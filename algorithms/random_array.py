import random


def random_array(length):
    array = []
    for i in range(length):
        array.append(random.randint(1, 100))
    return array
