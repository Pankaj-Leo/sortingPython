class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    # Get height of a node
    def height(self, node):
        return node.height if node else 0

    # Get balance factor of a node
    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    # Right Rotate (LL Rotation)
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    # Left Rotate (RR Rotation)
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    # Insert a node in the AVL tree
    def insert(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node  # Duplicate keys not allowed

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.get_balance(node)

        # Rotations to balance the tree
        if balance > 1 and key < node.left.key:  # LL Rotation
            return self.right_rotate(node)
        if balance < -1 and key > node.right.key:  # RR Rotation
            return self.left_rotate(node)
        if balance > 1 and key > node.left.key:  # LR Rotation
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.key:  # RL Rotation
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # Get node with the minimum value (for deletion)
    def get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    # Delete a node from the AVL tree
    def delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None or node.right is None:
                # Node with only one child or no child
                node = node.left if node.left is not None else node.right

            else:
                # Node with two children: get the inorder successor (smallest in the right subtree)
                temp = self.get_min_value_node(node.right)
                # Copy the inorder successor's key to this node
                node.key = temp.key
                # Delete the inorder successor
                node.right = self.delete(node.right, temp.key)

        if not node:
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.get_balance(node)

        # Rotations to balance the tree
        if balance > 1 and self.get_balance(node.left) >= 0:  # LL Rotation
            return self.right_rotate(node)
        if balance > 1 and self.get_balance(node.left) < 0:  # LR Rotation
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.get_balance(node.right) <= 0:  # RR Rotation
            return self.left_rotate(node)
        if balance < -1 and self.get_balance(node.right) > 0:  # RL Rotation
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # Inorder Traversal
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

# Example Usage
tree = AVLTree()
root = None

# Insert nodes
for key in [10, 20, 30, 40, 50, 25]:
    root = tree.insert(root, key)

print("Inorder traversal after insertion:")
tree.inorder(root)

# Delete a node
root = tree.delete(root, 30)
print("\nInorder traversal after deleting 30:")
tree.inorder(root)