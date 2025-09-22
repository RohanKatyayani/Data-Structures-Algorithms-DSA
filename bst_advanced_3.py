# Todo 1: Validate if a given tree is a BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if node is None:
            return Node(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def is_valid_bst(self, node, low=float("-inf"), high=float("inf")):
        if node is None:
            return True
        if not (low < node.data < high):
            return False
        return (self.is_valid_bst(node.left, low, node.data) and self.is_valid_bst(node.right, node.data, high))

    # Todo 2: Lowest Common Ancestor (LCA) in a BST

    def lca(self, node, p, q):
        if node is None:
            return None

        # Todo 2.1: Case 1: Both values smaller -> Go Left
        if p < node.data and q < node.data:
            return self.lca(node.left, p, q)

        # Todo 2.2: Case 2: Both values greater -> Go Right
        if p > node.data and q > node.data:
            return self.lca(node.right, p, q)

        # Todo 2.3: Case 3: Split happens -> Current is LCA
        return node

    # Todo 3: Inorder Successor & Predecessor
    def find_min(self, node):
        while node and node.left:
            node = node.left
        return node

    def find_max(self, node):
        while node and node.right:
            node = node.right
        return node

    # Todo 3.1: Inorder Successor
    def successor(self, root, key):
        succ = None
        cur = root
        while cur:
            if key < cur.data:
                succ = cur
                cur = cur.left
            elif key > cur.data:
                cur = cur.right
            else:
                if cur.right:
                    succ = self.find_min(cur.right)
                break
        return succ

    # Todo 3.2: Inorder Predecessor
    def predecessor(self, root, key):
        pred = None
        cur = root
        while cur:
            if key > cur.data:
                pred = cur
                cur = cur.right
            elif key < cur.data:
                cur = cur.left
            else:
                if cur.left:
                    pred = self.find_max(cur.left)
                break
        return pred

if __name__ == "__main__":
    bst = BST()
    bst.root = bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)

    print("\nIs BST Valid?", bst.is_valid_bst(bst.root))                  # True

    print("\nLCA of 20 and 40:", bst.lca(bst.root, 20, 40).data)    # 30
    print("LCA of 20 and 60:", bst.lca(bst.root, 20, 60).data)      # 50
    print("LCA of 60 and 80:", bst.lca(bst.root, 60, 80).data)      # 70

    print("\nSuccessor of 30:", bst.successor(bst.root, 30).data)    # 40
    print("Predecessor of 30:", bst.predecessor(bst.root, 30).data)  # 20
    print("Successor of 50:", bst.successor(bst.root, 50).data)      # 60
    print("Predecessor of 50:", bst.predecessor(bst.root, 50).data)  # 40

    bst.root.left.right.data = 60
    print("\nIs BST Valid?", bst.is_valid_bst(bst.root))                  # False