from collections import defaultdict, deque


class Graph_DFS:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, src, dest):
        self.adjacency_list[src].append(dest)
        self.adjacency_list[dest].append(src)  # Uncomment for an undirected graph

    def dfs(self):
        visited = set()
        stack = deque()

        # Iterate through all nodes for disconnected graphs
        for node in self.adjacency_list:
            if node not in visited:
                print(f"\nDFS from component starting at {node}:", end=" ")
                stack.append(node)

                while stack:
                    current = stack.pop()

                    if current not in visited:
                        visited.add(current)
                        print(current, end=" ")

                        # Push neighbors onto the stack (reverse order for correct traversal)
                        for neighbor in reversed(self.adjacency_list[current]):
                            if neighbor not in visited:
                                stack.append(neighbor)


# Example Usage
graph = Graph_DFS()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")
graph.add_edge("F", "G")  # Disconnected component

print("Depth-First Traversal (Iterative using Stack):")
graph.dfs()