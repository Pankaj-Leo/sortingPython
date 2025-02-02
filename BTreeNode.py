# btree.py
class BTreeNode:
    def __init__(self, t, leaf):
        self.t = t  # Minimum degree
        self.leaf = leaf  # True if node is leaf
        self.keys = []  # List of keys
        self.children = []  # List of child pointers

    def traverse(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")
        if not self.leaf:
            self.children[len(self.keys)].traverse()

    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == key:
            return self
        if self.leaf:
            return None
        return self.children[i].search(key)

    def insert_non_full(self, key):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(0)  # dummy value to extend the list
            while i >= 0 and self.keys[i] > key:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and self.keys[i] > key:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i, self.children[i])
                if self.keys[i] < key:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i, y):
        z = BTreeNode(y.t, y.leaf)
        z.keys = y.keys[y.t:(2 * y.t - 1)]
        if not y.leaf:
            z.children = y.children[y.t:(2 * y.t)]
        y.keys = y.keys[0:y.t - 1]
        y.children = y.children[0:y.t] if not y.leaf else y.children
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop())


class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None

    def traverse(self):
        if self.root:
            self.root.traverse()
            print()

    def search(self, key):
        return None if self.root is None else self.root.search(key)

    def insert(self, key):
        if self.root is None:
            self.root = BTreeNode(self.t, True)
            self.root.keys.append(key)
        else:
            if len(self.root.keys) == 2 * self.t - 1:
                s = BTreeNode(self.t, False)
                s.children.append(self.root)
                s.split_child(0, self.root)
                i = 0
                if s.keys[0] < key:
                    i += 1
                s.children[i].insert_non_full(key)
                self.root = s
            else:
                self.root.insert_non_full(key)


if __name__ == '__main__':
    t = 3
    tree = BTree(t)
    for key in [10, 20, 5, 6, 12, 30, 7, 17]:
        tree.insert(key)
    print("Traversal of the constructed B-Tree is:")
    tree.traverse()
    search_key = 6
    result = tree.search(search_key)
    print(f"Key {search_key} {'found' if result is not None else 'not found'} in the tree.")
