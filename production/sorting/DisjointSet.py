class DisjointSet:
	def __init__(self,size):
		self.parent = [i for i in range (size)]
		self.rank = [1]*size #Rank to optimize union

	def find(self, node):
		"""Finds the root of the set containing `node`, with path compression."""
		if self.parent[node] != node:
			self.parent[node] = self.find(self.parent[node])  # Path compression
		return self.parent[node]

	def union(self, node1, node2):
		""" Unites the sets of node1 and node2 using union by rank. """
		root1 = self.find(node1)
		root2 = self.find(node2)

		if self.rank[root1] > self.rank[root2]:  # Merge the smaller tree under the larger one
			self.parent[root2] = root1
		elif self.rank[root1] < self.rank[root2]:
			self.parent[root1] = root2
		else:
			self.parent[root2] = root1  # If ranks are equal, merge under root1
			self.rank[root1] += 1  # Increase the rank of root1

	def are_connected(self, node1, node2):
		""" Checks if two nodes belong to the same set. """
		return self.find(node1) == self.find(node2)


# Example Usage
ds = DisjointSet(10)  # 10 individuals: a-j (indexed as 0-9)
relations = [(0, 1), (1, 3), (2, 5), (2, 8), (9, 4), (6, 9)]  # Friendships

for u, v in relations:
    ds.union(u, v)

# Checking friendships
print(ds.are_connected(0, 3))  # True (a and d are connected)
print(ds.are_connected(2, 8))  # True (c and i are connected)
print(ds.are_connected(4, 6))  # True (e and g are connected)
print(ds.are_connected(0, 5))  # False (a and f are not connected)