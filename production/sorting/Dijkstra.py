import heapq
from typing import List, Dict


class Solution:
    def shortestPath(self, n: int, edges: List[tuple], src: int) -> Dict[int, int]:
        """
        Implements Dijkstra's algorithm to find the shortest path from the source vertex to all other vertices.

        Args:
            n (int): Number of vertices.
            edges (List[tuple]): List of edges where each edge is represented as (u, v, weight).
            src (int): Source vertex.

        Returns:
            Dict[int, int]: A dictionary where the key is the vertex and the value is the shortest distance from the source.
        """
        # Create an adjacency list to represent the graph
        adj = {i: [] for i in range(n)}
        for s, d, weight in edges:
            adj[s].append((d, weight))

        # Dictionary to store the shortest distance to each vertex
        shortest = {}  # {vertex: shortest_distance}

        # Min-heap to store (distance, vertex), starting with the source
        minHeap = [(0, src)]  # (distance_from_source, vertex)

        # Process the min-heap until it's empty
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)  # Get the vertex with the smallest distance

            # If the vertex is already processed, skip it
            if n1 in shortest:
                continue

            # Record the shortest distance for this vertex
            shortest[n1] = w1

            # Explore the neighbors of the current vertex
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    # Push the neighbor with the updated distance into the min-heap
                    heapq.heappush(minHeap, (w1 + w2, n2))

        # Fill in vertices that were not reachable from the source with -1
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest


# Driver code
if __name__ == "__main__":
    edges = [
        (0, 1, 4), (0, 7, 8),
        (1, 2, 8), (1, 7, 11),
        (2, 3, 7), (2, 5, 4), (2, 8, 2),
        (3, 4, 9), (3, 5, 14),
        (4, 5, 10),
        (5, 6, 2),
        (6, 7, 1), (6, 8, 6),
        (7, 8, 7)
    ]

    solution = Solution()
    shortest_distances = solution.shortestPath(9, edges, 0)
    print("Shortest distances from source 0:")
    for vertex, distance in shortest_distances.items():
        print(f"Vertex {vertex} -> Distance: {distance}")




