from collections import defaultdict, deque

class Graph_BFS:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, src, dest):
        self.adjacency_list[src].append(dest)
        # self.adjacency_list[dest].append(src)  # Uncomment for Undirected Graph

    def bfs(self, start):
        queue = deque([start])
        visited = set([start])

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Example Usage
graph = Graph_BFS()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "E")
graph.add_edge("E", "F")

print("BFS Traversal starting from A:", end=" ")
graph.bfs("A")