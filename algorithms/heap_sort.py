"""
Overall aim is to keep syntax as simple as possible, the focus being the algorithms themselves,
thus resisting the temptation to wrap up everything under a class with @classmethod.
"""

def left_node(i: int):
    return 2 * i + 1


def right_node(i: int):
    return 2 * i + 2


def restore_max_heap(heap: list, i: int, heap_size: int):
    left = left_node(i)
    right = right_node(i)
    if left < heap_size and heap[left] > heap[i]:
        max_idx = left
    else:
        max_idx = i
    if right < heap_size and heap[right] > heap[max_idx]:
        max_idx = right
    if max_idx != i:
        heap[i], heap[max_idx] = heap[max_idx], heap[i]
        restore_max_heap(heap, max_idx, heap_size)


def create_max_heap(arr: list):
    for i in reversed(range(int(len(arr) / 2))):
        restore_max_heap(arr, i, len(arr))


def heap_sort(arr: list):
    create_max_heap(arr)
    for i in reversed(range(len(arr))):
        arr[0], arr[i] = arr[i], arr[0]
        restore_max_heap(arr, 0, i)
