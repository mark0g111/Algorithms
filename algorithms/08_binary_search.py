from typing import Any


def binary_search(key: Any, arr: list) -> Any:
    i = 0
    j = len(arr) - 1
    while i <= j:
        mid = (j + i) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            i = mid + 1
        else:
            j = mid - 1
    return None
