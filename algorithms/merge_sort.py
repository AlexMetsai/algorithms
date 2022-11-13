"""
Merge sort algorithm.

1. split into two parts
2. merge_sort(part 1)
3. merge_sort(part 2)
4. merge(part1, part2)

Obviously the core logic is about the merging logic.
"""


def merge(arr: list, p: int, q: int, r: int):
    n1 = q - p + 1
    n2 = r - q

    left_arr = []
    for i in range(n1):
        left_arr.append(arr[p + i])
    left_arr.append(float("inf"))

    right_arr = []
    for i in range(n2):
        right_arr.append(arr[q + i + 1])
    right_arr.append(float("inf"))

    i, j = 0, 0
    for k in range(p, r):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i =+ 1
        else:
            arr[k] = right_arr[j]
            j += 1


def merge_sort(arr: list, p: int = None, r: int = None):
    if p is None:
        # first call
        p, r = 0, len(arr) - 1
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)
