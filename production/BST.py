from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    @staticmethod
    def insert(root, val):
        if root is None:
            return Node(val)

        if root.data > val:
            root.left = BST.insert(root.left, val)
        else:
            root.right = BST.insert(root.right, val)

        return root

    @staticmethod
    def inorder(root):
        if root is None:
            return
        BST.inorder(root.left)
        print(root.data, end=" ")
        BST.inorder(root.right)

    @staticmethod
    def search(root, key):
        if root is None:
            return False

        if root.data == key:
            return True

        if root.data > key:
            return BST.search(root.left, key)
        else:
            return BST.search(root.right, key)

    @staticmethod
    def delete(root, val):
        if root is None:
            return None

        if root.data > val:
            root.left = BST.delete(root.left, val)
        elif root.data < val:
            root.right = BST.delete(root.right, val)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                IS = BST.inorder_successor(root.right)
                root.data = IS.data
                root.right = BST.delete(root.right, IS.data)

        return root

    @staticmethod
    def inorder_successor(root):
        while root.left is not None:
            root = root.left
        return root

    @staticmethod
    def print_root_to_leaf(root, path):
        if root is None:
            return

        path.append(root.data)

        if root.left is None and root.right is None:
            BST.print_path(path)
        else:
            BST.print_root_to_leaf(root.left, path)
            BST.print_root_to_leaf(root.right, path)

        path.pop()

    @staticmethod
    def print_path(path):
        for i in range(len(path)):
            print(path[i], end=" ")
        print()

    @staticmethod
    def level_order(root):
        if root is None:
            return

        q = deque()
        q.append(root)
        q.append(None)

        while q:
            curr = q.popleft()
            if curr is None:
                print()
                if not q:
                    break
                else:
                    q.append(None)
            else:
                print(curr.data, end=" ")
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

# Example usage
if __name__ == "__main__":
    values = [5, 1, 3, 4, 2, 7]
    root = None

    # Insert values into the BST
    for val in values:
        root = BST.insert(root, val)

    # Inorder Traversal
    print("Inorder Traversal:")
    BST.inorder(root)
    print()

    # Search for a value
    key = 3
    if BST.search(root, key):
        print(f"{key} is found in the BST.")
    else:
        print(f"{key} is not found in the BST.")

    # Delete a node
    print("Deleting node with value 3...")
    root = BST.delete(root, 3)

    # Inorder Traversal after deletion
    print("Inorder Traversal after deletion:")
    BST.inorder(root)
    print()

    # Print all root-to-leaf paths
    print("Root-to-Leaf Paths:")
    BST.print_root_to_leaf(root, [])

    # Level Order Traversal
    print("Level Order Traversal:")
    BST.level_order(root)