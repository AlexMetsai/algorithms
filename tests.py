"""
Test and benchmark sorting algorithms.
"""
from algorithms.heap_sort import heap_sort
from algorithms.quicksort import quicksort
from algorithms.utils.data_generation import get_whole_number_array


def evaluate(alg, retries=10):
    success = 0
    for _ in range(retries):
        test_arr = get_whole_number_array()
        alg(test_arr)
        success += int(test_arr == sorted(test_arr))
    print(f"{alg.__name__}: {success}/{retries} tests successful")


if __name__ == "__main__":
    sorting_algorithms = [heap_sort, quicksort]
    for alg in sorting_algorithms:
        evaluate(alg)
