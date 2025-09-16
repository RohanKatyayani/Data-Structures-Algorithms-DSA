# Todo 1: Diameter of a Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def diameter(self, node):
        if node is None:
            return 0

        # Height
        lh = self.height(node.left)
        rh = self.height(node.right)

        # Diameter
        ld = self.diameter(node.left)
        rd = self.diameter(node.right)

        return max(lh + rh + 1, max(ld, rd))

    # Todo 2: Lowest common ancestor (In Binary Tree not BST)

    def lca(self, root, p, q):
        if root is None:
            return None
        if root.data == p or root.data == q:
            return root

        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)

        if left and right:
            return root
        return left if left else right

    # Todo 3: Count and sum of Nodes in Binary Tree

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def sum_nodes(self, node):
        if node is None:
            return 0
        return node.data + self.sum_nodes(node.left) + self.sum_nodes(node.right)

if __name__ == "__main__":
    bt = Binary_Tree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    # bt.root = Node(3)
    # bt.root.left = Node(5)
    # bt.root.right = Node(1)
    # bt.root.left.left = Node(6)
    # bt.root.left.right = Node(2)
    # bt.root.left.right.left = Node(7)
    # bt.root.left.right.right = Node(4)
    # bt.root.right.left = Node(0)
    # bt.root.right.right = Node(8)

    print("Diameter of Tree", bt.diameter(bt.root))

    # lca_node = bt.lca(bt.root, 6, 4)
    # print("LCA of 6 and 4:", lca_node.data)  # 5
    #
    # lca_node = bt.lca(bt.root, 6, 8)
    # print("LCA of 6 and 8:", lca_node.data)  # 3

    print("Count of nodes:", bt.count_nodes(bt.root))  # 5
    print("Sum of nodes:", bt.sum_nodes(bt.root))  # 15