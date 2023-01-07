from typing import List


class Graph:
    def __init__(self, adjacent_matrix: List[List]):
        self.num_vertices = len(adjacent_matrix)
        self.graph = adjacent_matrix
