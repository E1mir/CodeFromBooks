from .dijkstra_oop import DijkstraSearch
INFINITY = float('inf')

graph_A = {}
graph_A["start"] = {}
graph_A["start"]["a"] = 5
graph_A["start"]["b"] = 2

graph_A["a"] = {}
graph_A["a"]["d"] = 4
graph_A["a"]["c"] = 2

graph_A["b"] = {}
graph_A["b"]["a"] = 8
graph_A["b"]["c"] = 7

graph_A["d"] = {}
graph_A["d"]["c"] = 6
graph_A["d"]["end"] = 3

graph_A["c"] = {}
graph_A["c"]["end"] = 1

graph_A["end"] = {}

costs_A = {}
costs_A["a"] = 5
costs_A["b"] = 2
costs_A["d"] = INFINITY
costs_A["c"] = INFINITY
costs_A["end"] = INFINITY

parents_A = {}
parents_A["a"] = "start"
parents_A["b"] = "start"
parents_A["d"] = "a"
parents_A["end"] = None

solve_A = DijkstraSearch(graph_A, costs_A, parents_A)
solve_A.solve()
