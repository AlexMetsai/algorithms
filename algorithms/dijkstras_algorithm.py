"""
Dijkstra's Algorithm

Looking at a visual example of the algorithm will assist in understanding it.
"""

from typing import List


class Graph:
    def __init__(self, adjacent_matrix: List[List]):
        self.num_vertices = len(adjacent_matrix)
        self.graph = adjacent_matrix


def dijkstras_algorithm(g: Graph, start: int, end: int):

    dist = {v: float("inf") for v in range(g.num_vertices)}
    prev = {v: None for v in range(g.num_vertices)}
    dist[start] = 0

    queue = list(range(g.num_vertices))

    # Find distances from start.
    while queue:
        queue_dist = {k: v for k, v in dist.items() if k in queue}
        min_dist_vertex = min(queue_dist, key=queue_dist.get)
        queue.remove(min_dist_vertex)

        for v in queue:
            dist_temp = dist[min_dist_vertex] + g.graph[min_dist_vertex][v]
            if dist_temp < dist[v]:
                dist[v] = dist_temp
                prev[v] = min_dist_vertex

    # Find shortest path.
    seq = []
    min_dist_vertex = end
    if prev[min_dist_vertex] is not None or min_dist_vertex == start:
        while min_dist_vertex is not None:
            seq.insert(0, min_dist_vertex)
            min_dist_vertex = prev[min_dist_vertex]

    return seq


def dummy_adj_matrix():
    """
    A quick example I created, maybe I should look into something
    more focused for testing, which has been manual so far.
    """
    adjacent_matrix = [
        [0, 4, 5, 0, 0,],
        [4, 0, 0, 3, 9,],
        [5, 0, 0, 9, 0,],
        [0, 3, 9, 0, 1,],
        [0, 9, 0, 1, 0,]
    ]
    adjacent_matrix = [
        [float("inf") if i == 0 else i for i in row]
        for row in adjacent_matrix
    ]
    return adjacent_matrix


if __name__ == "__main__":
    g = Graph(dummy_adj_matrix())
    res = dijkstras_algorithm(g, start=0, end=3)
    print(res)
