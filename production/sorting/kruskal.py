class DisjointSet:
	""" Disjoint Set (Union-Find) with Path Compression & Rank Optimization. """

	def __init__(self, n):
		self.parent = [i for i in range(n)]
		self.rank = [0] * n

	def find(self, node):
		""" Finds the representative (root) of the set. """
		if self.parent[node] != node:
			self.parent[node] = self.find(self.parent[node])  # Path Compression
		return self.parent[node]

	def union(self, u, v):
		""" Unites two sets using rank optimization. """
		root1 = self.find(u)
		root2 = self.find(v)

		if root1 != root2:
			if self.rank[root1] > self.rank[root2]:
				self.parent[root2] = root1
			elif self.rank[root1] < self.rank[root2]:
				self.parent[root1] = root2
			else:
				self.parent[root2] = root1
				self.rank[root1] += 1


def kruskal(n, edges):
	""" Finds the Minimum Spanning Tree (MST) using Kruskal's Algorithm. """
	# Step 1: Sort edges by weight
	edges.sort(key=lambda edge: edge[2])  # Sort by weight (edge[2])

	ds = DisjointSet(n)
	mst = []
	total_weight = 0

	# Step 2: Pick edges one by one
	for u, v, weight in edges:
		if ds.find(u) != ds.find(v):  # If adding edge doesn't create a cycle
			ds.union(u, v)
			mst.append((u, v, weight))
			total_weight += weight

			if len(mst) == n - 1:  # Stop when we have (V - 1) edges
				break

	return mst, total_weight


# Example Graph (Number of Nodes = 5)
edges = [
	(0, 1, 10), (0, 2, 6), (0, 3, 5),
	(1, 3, 15), (2, 3, 4)
]
n = 4  # Number of nodes

mst, weight = kruskal(n, edges)
print("Edges in MST:", mst)
print("Total Weight of MST:", weight)