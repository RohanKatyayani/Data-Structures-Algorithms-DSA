class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # Todo 1: Diameter of a Binary Tree
    def diameter(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        left_diameter = self.diameter(node.left)
        right_diameter = self.diameter(node.right)

        return max(left_height + right_height, max(left_diameter, right_diameter))

    # Todo 2: Lowest Common Ancestor (LCA) in a Binary Tree
    def lca(self, root, p ,q):
        if root is None:
            return None

        if root.data == p or root.data == q:
            return root

        left_lca = self.lca(root.left, p, q)
        right_lca = self.lca(root.right, p, q)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca else right_lca

    # Todo 3: Check if a Binary Tree is Balanced.
    def is_balanced(self, root):
        def check(node):
            if node is None:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(right - left) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1

if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)

    print("\nDiameter of tree:", bt.diameter(bt.root))  # Output = 3 (path: 4 -> 2 -> 5 or 4 -> 2 -> 1 -> 3)

    bt = BinaryTree()
    bt.root = Node(3)
    bt.root.left = Node(5)
    bt.root.right = Node(1)
    bt.root.left.left = Node(6)
    bt.root.left.right = Node(2)
    bt.root.right.left = Node(0)
    bt.root.right.right = Node(8)
    bt.root.left.right.left = Node(7)
    bt.root.left.right.right = Node(4)

    # Tree looks like:
    #          3
    #       /     \
    #      5       1
    #     / \     / \
    #    6   2   0   8
    #       / \
    #      7   4

    print("\nLCA of 5 and 1:", bt.lca(bt.root, 5, 1).data)  # 3
    print("LCA of 6 and 4:", bt.lca(bt.root, 6, 4).data)  # 5
    print("LCA of 7 and 8:", bt.lca(bt.root, 7, 8).data)  # 3

    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.left.left.left = Node(6)  # This extra depth unbalances the tree

    print("\nIs tree balanced?", bt.is_balanced(bt.root))  # False

    bt2 = BinaryTree()
    bt2.root = Node(1)
    bt2.root.left = Node(2)
    bt2.root.right = Node(3)
    bt2.root.left.left = Node(4)
    bt2.root.left.right = Node(5)

    print("Is tree balanced?", bt2.is_balanced(bt2.root))  # True