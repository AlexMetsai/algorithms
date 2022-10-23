"""
Quicksort algorithm.
"""


def divide(arr: list, p: int, r: int):
    """
    Rearrange a (part of a larger) array, arr[p..r], into two arrays arr[p..q-1] and arr[q+1..r],
    such that all values of the first are smaller than arr[q] and all values of the second
    are larger than arr[q].
    """
    i = p - 1
    for j in range(p, r):
        if arr[j] <= arr[r]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def _quicksort(arr: list, p: int, r: int):
    if p < r:
        q = divide(arr, p, r)
        _quicksort(arr, p, q - 1)
        _quicksort(arr, q + 1, r)


def quicksort(arr: list):
    _quicksort(arr, p=0, r=len(arr) - 1)
