"""
Test and benchmark sorting algorithms.
"""

from time import time

from algorithms.heap_sort import heap_sort
from algorithms.quicksort import quicksort
from algorithms.merge_sort import merge_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.utils.data_generation import get_whole_number_array


def evaluate(alg, retries=10):
    success = 0
    execution_time = []
    for _ in range(retries):
        test_arr = get_whole_number_array()
        start = time()
        alg(test_arr)
        end = time()
        success += int(test_arr == sorted(test_arr))
        execution_time.append(end - start)
    print(
        f"{alg.__name__}: {success}/{retries} tests successful,"
        f" average perfromance: {sum(execution_time) / len(execution_time)}"
    )


if __name__ == "__main__":
    sorting_algorithms = [heap_sort, quicksort, merge_sort, insertion_sort]
    for alg in sorting_algorithms:
        evaluate(alg)
