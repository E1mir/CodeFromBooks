class DijkstraSearch(object):
    INFINITY = float("inf")

    def __init__(self, graph, costs, parents):
        self.graph = graph
        self.costs = costs
        self.parents = parents
        self.processed = []

    def find_lowest_cost_node(self):
        lowest_cost = self.INFINITY
        lowest_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def solve(self):
        node = self.find_lowest_cost_node()
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed.append(node)
            node = self.find_lowest_cost_node()

        self.show_results()

    def show_results(self):
        print("Your solution is: {}".format(self.parents))
        print("The lowest costs are: {}".format(self.costs))
