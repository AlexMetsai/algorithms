"""
Overall aim is to keep syntax as simple as possible, the focus being the algorithms themselves,
thus resisting the temptation to wrap up everything under a class and/or use @classmethod.
"""


def parent_node(i: int):
    return int(i / 2)


def left_node(i: int):
    return int(2 * i)


def right_node(i: int):
    return int(2 * i + 1)


def restore_max_heap(heap: list, i: int):
    left = left_node(i)
    right = right_node(i)
    if left <= len(heap) and heap[left] > heap[right]:
        max_idx = left
    else:
        max_idx = i
    if right <= len(heap) and heap[right] > heap[max_idx]:
        max_idx = right
    if max_idx != i:
        heap[i], heap[max_idx] = heap[max_idx], heap[i]
        restore_max_heap(heap, max_idx)


def create_max_heap(arr: list):
    heap_size = len(arr)
    for i in reversed(range(1, int(len(arr) / 2 + 1))):
        restore_max_heap(arr, i)
    return arr, heap_size
