from collections import defaultdict, deque

class Graph_Cycle_Detection_Undirected:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, src, dest):
        self.adjacency_list[src].append(dest)
        self.adjacency_list[dest].append(src) # Undirected graph

    def has_cycle(self):
        visited = set()

        for node in self.adjacent_list:
            if node not in visited:
                if self.iterative_dfs(node):
                    return True
        return False

    def iterative_dfs(self, start_node):
        stack = ([start_node])
        parent_map = {start_node: None}
        visited = set ()

        while stack:
            current_node = stack.pop()
            visited.add(current_node)

            for neighbor in self.adjacency_list[current_node]:
                if neighbor not in  visited:
                    stack.append(neighbor)
                    parent_map[neighbor] = current_node
                elif parent_map[current_node]!= neighbor:
                    return True #Cycle detected

        return False

graph = Graph_Cycle_Detection_Undirected()
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "A")  # Cycle exists
graph.add_edge("D", "E")

print("Graph contains cycle:", graph.has_cycle())