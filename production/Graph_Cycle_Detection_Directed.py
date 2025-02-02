from collections import defaultdict

from sqlalchemy.sql.operators import truediv


class Graph_Cycle_Detection_Directed:

    def __inti__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge (self, src, dest):
        self.adjacencyList[src].append(dest)

    def dfs (self, node, visited, recStack):
        if node in recStack:
            return True # cycle detected
        if node in visited:
            return False # Already processed

        for neighbor in self.adjacency_list[node]:
            if self.dfs(neighbor, visited, recStack):
                return True

        recStack.remove(node)
        return False

    def has_cycle(self):
        visited = set ()
        recStack = set()

        for node in self.adjacency_list:
            if node not in visited:
                if self.dfs (node, visited, recStack):
                    return True
        return False

graph = Graph_Cycle_Detection_Directed()
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "A")  # Creates a cycle
graph.add_edge("D", "E")

print("Graph contains cycle:", graph.has_cycle())