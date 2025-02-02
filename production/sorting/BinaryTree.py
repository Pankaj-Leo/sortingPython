from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.idx = -1

    def build_tree(self, nodes):
        self.idx += 1
        if nodes[self.idx] == -1:
            return None
        new_node = Node(nodes[self.idx])
        new_node.left = self.build_tree(nodes)
        new_node.right = self.build_tree(nodes)
        return new_node

    # Preorder Traversal
    def preorder(self, root):
        if root is None:
            print(-1, end=" ")
            return
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    # Inorder Traversal
    def inorder(self, root):
        if root is None:
            print(-1, end=" ")
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root is None:
            print(-1, end=" ")
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

    # Level Order Traversal
    def level_order(self, root):
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

    # Height of Tree
    def height(self, root):
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height, right_height) + 1

    # Count of Nodes
    def count_of_nodes(self, root):
        if root is None:
            return 0
        left_nodes = self.count_of_nodes(root.left)
        right_nodes = self.count_of_nodes(root.right)
        return left_nodes + right_nodes + 1

    # Sum of Nodes
    def sum_of_nodes(self, root):
        if root is None:
            return 0
        left_sum = self.sum_of_nodes(root.left)
        right_sum = self.sum_of_nodes(root.right)
        return left_sum + right_sum + root.data

    # Diameter of Tree - O(N^2)
    def diameter(self, root):
        if root is None:
            return 0
        diam1 = self.height(root.left) + self.height(root.right) + 1
        diam2 = self.diameter(root.left)
        diam3 = self.diameter(root.right)
        return max(diam1, max(diam2, diam3))

    # Diameter of Tree - O(N)
    class TreeInfo:
        def __init__(self, height, diam):
            self.height = height
            self.diam = diam

    def diameter_optimized(self, root):
        if root is None:
            return self.TreeInfo(0, 0)
        left_ti = self.diameter_optimized(root.left)
        right_ti = self.diameter_optimized(root.right)
        my_height = max(left_ti.height, right_ti.height) + 1
        diam1 = left_ti.height + right_ti.height + 1
        diam2 = left_ti.diam
        diam3 = right_ti.diam
        my_diam = max(diam1, max(diam2, diam3))
        return self.TreeInfo(my_height, my_diam)

    # Subtree of Another Tree
    def is_identical(self, root, sub_root):
        if sub_root is None and root is None:
            return True
        if root is None or sub_root is None:
            return False
        if root.data == sub_root.data:
            return self.is_identical(root.left, sub_root.left) and self.is_identical(root.right, sub_root.right)
        return False

    def is_subtree(self, root, sub_root):
        if sub_root is None:
            return True
        if root is None:
            return False
        if self.is_identical(root, sub_root):
            return True
        return self.is_subtree(root.left, sub_root) or self.is_subtree(root.right, sub_root)

# Example usage
if __name__ == "__main__":
    nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    bt = BinaryTree()
    root = bt.build_tree(nodes)

    print("Preorder Traversal:")
    bt.preorder(root)

    print("\nInorder Traversal:")
    bt.inorder(root)

    print("\nPostorder Traversal:")
    bt.postorder(root)

    print("\nLevel Order Traversal:")
    bt.level_order(root)

    print("Height of Tree:", bt.height(root))
    print("Count of Nodes:", bt.count_of_nodes(root))
    print("Sum of Nodes:", bt.sum_of_nodes(root))
    print("Diameter of Tree (O(N^2)):", bt.diameter(root))
    print("Diameter of Tree (O(N)):", bt.diameter_optimized(root).diam)