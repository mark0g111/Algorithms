from typing import Any


def linear_search(n: Any, arr: list) -> Any:
    for i in arr:
        if i == n:
            return arr.index(i)
    return None
