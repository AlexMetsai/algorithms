"""
Merge sort algorithm.

1. split into two parts
2. merge_sort(part 1)
3. merge_sort(part 2)
4. merge(part1, part2)

Obviously the core logic is about the merging logic.
"""


def merge():
    raise NotImplementedError


def merge_sort(arr: list, p: int = None, r: int = None):
    if p is None:
        # first call
        p, r, = 0, len(arr)
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)
