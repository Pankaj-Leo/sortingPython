from functools import lru_cache


def tsp(graph):
    n = len(graph)

    @lru_cache(maxsize=None)
    def dp(mask, pos):
        if mask == (1 << n) - 1:
            return graph[pos][0], [0]  # Return to start, path ends with 0

        ans = float('inf')
        best_path = []

        for city in range(n):
            if not (mask & (1 << city)):  # If city is unvisited
                cost, path = dp(mask | (1 << city), city)  # Recursively solve
                total_cost = graph[pos][city] + cost

                if total_cost < ans:
                    ans = total_cost
                    best_path = [pos] + path  # Update best path

        return ans, best_path

    # Start the recursion
    min_cost, best_path = dp(1, 0)

    # Add the starting city to the path
    best_path = [0] + best_path

    return min_cost, best_path


# Example graph
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Solve TSP and print results
min_cost, best_path = tsp(graph)
print("Minimum TSP cost:", min_cost)
print("Shortest path:", " -> ".join(map(str, best_path)))