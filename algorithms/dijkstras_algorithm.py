"""
Dijkstra's Algorithm

Looking at a visual example of the algorithm will assist in understanding it.
"""

from typing import List


class Graph:
    def __init__(self, adjacent_matrix: List[List]):
        self.num_vertices = len(adjacent_matrix)
        self.graph = adjacent_matrix

def dummy_adj_matrix():
    """
    A quick example I created, maybe I should look into something
    more focused for testing.
    """
    adjacent_matrix = [
        [0, 4, 5, 0, 0,],
        [4, 0, 0, 3, 9,],
        [5, 0, 0, 9, 0,],
        [0, 3, 9, 0, 1,],
        [0, 9, 0, 1, 0,]
    ]


if __name__ == "__main__":
    ...
