# bplustree.py
class BPlusTreeNode:
    def __init__(self, m, is_leaf):
        self.m = m                  # Maximum keys per node
        self.is_leaf = is_leaf      # True if leaf node
        self.keys = []              # List of keys
        self.children = []          # List of child pointers (for internal nodes)
        self.next = None            # Pointer to next leaf (for leaf nodes)

class BPlusTree:
    def __init__(self, m):
        self.m = m
        self.root = BPlusTreeNode(m, True)

    def search(self, key):
        cur = self.root
        while not cur.is_leaf:
            i = 0
            while i < len(cur.keys) and key >= cur.keys[i]:
                i += 1
            cur = cur.children[i]
        return key in cur.keys

    def insert(self, key):
        root = self.root
        if len(root.keys) == self.m:  # Root is full; split it.
            new_root = BPlusTreeNode(self.m, False)
            new_root.children.append(root)
            self.split_child(new_root, 0, root)
            self.root = new_root
        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        if node.is_leaf:
            i = len(node.keys) - 1
            node.keys.append(0)  # dummy value to extend list
            while i >= 0 and node.keys[i] > key:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            i = len(node.keys) - 1
            while i >= 0 and node.keys[i] > key:
                i -= 1
            i += 1
            if len(node.children[i].keys) == self.m:
                self.split_child(node, i, node.children[i])
                if key >= node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, index, child):
        new_node = BPlusTreeNode(self.m, child.is_leaf)
        mid = (self.m + 1) // 2
        new_node.keys = child.keys[mid:]
        child.keys = child.keys[:mid]
        if not child.is_leaf:
            new_node.children = child.children[mid:]
            child.children = child.children[:mid]
        if child.is_leaf:
            new_node.next = child.next
            child.next = new_node
        parent.children.insert(index + 1, new_node)
        parent.keys.insert(index, new_node.keys[0])

    def traverse(self):
        # Go to leftmost leaf.
        cur = self.root
        while not cur.is_leaf:
            cur = cur.children[0]
        while cur:
            for key in cur.keys:
                print(key, end=" ")
            cur = cur.next
        print()

if __name__ == "__main__":
    bpt = BPlusTree(4)  # Maximum 4 keys per node.
    for key in [10, 20, 5, 6, 12, 30, 7, 17]:
        bpt.insert(key)
    print("B+ Tree traversal:")
    bpt.traverse()
    print("Search 12:", bpt.search(12))
    print("Search 15:", bpt.search(15))
