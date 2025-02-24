from collections import deque

def topological_sort(adj, V):
    # Step 1: Compute in-degree for each vertex
    indegree = [0] * V
    for i in range(V):
        for vertex in adj[i]:
            indegree[vertex]+= 1 # Increment in-degree

    # Step 2: Initialize queue with vertices having in-degree = 0
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    result = []

    # Step 3: Process the queue
    while q:
        node = q.popleft()
        result.append(node)

        # Reduce in-degree of all adjacent nodes
        for adjacent in adj[node]:
            indegree[adjacent] -= 1
            if indegree[adjacent] == 0:  # If in-degree becomes zero, add to queue
                q.append(adjacent)

        # Step 4: Check for cycle
    if len(result) != V:
        print("Graph contains cycle!")  # If all nodes are not in result, cycle exists
        return []

    return result




# Example Usage
if __name__ == "__main__":
    n = 6  # Number of nodes
    edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]

    # Graph represented as an adjacency list
    adj = [[] for _ in range (n)]
    for edge in edges:
        adj[edge[0]].append(edge[1])

    print("Topological Sorting:", end=" ")
    result = topological_sort(adj, n)

    if result:
        print(" ".join(map(str, result)))

