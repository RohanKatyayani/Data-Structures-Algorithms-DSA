from typing import Optional

# Todo 1: Find Min & Max in a BST

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
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    # Todo 1.1: Find Minimum (leftmost)
    def find_min(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current

    # Todo 1.2: Find Maximum (rightmost)
    def find_max(self, node):
        current = node
        while current and current.right:
            current = current.right
        return current

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" -> ")
            self.inorder(node.right)

    # Todo 2: Delete a Node in BST
    def delete(self, node, key):
        if node is None:
            return node

        # Todo 2.1: Traverse the tree
        if key < node.data:
            node.left = self.delete(node.left, key)
        elif key > node.data:
            node.right = self.delete(node.right, key)
        else:
            # Found the Node to Delete

            # Todo 2.2: Node is a Leaf (no children)
            if node.left is None and node.right is None:
                return none

            # Todo 2.3: Node has one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Todo 2.4: Node has two children
            temp = self.find_min(node.right) # Inorder Successor
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)

        return node

    # Todo 3: Check if a Tree is BST

    def is_bst_until(self, node, low, high):
        if node is None:
            return True
        if not (low < node.data < high):
            return False
        return (self.is_bst_until(node.left, low, node.data) and
                self.is_bst_until(node.right, node.data, high))

    def is_bst(self, node):
        return self.is_bst_until(node, float("-inf"), float("inf"))

    # Todo 4: Height of a Tree

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

if __name__ == "__main__":
    bst = BST()
    bst.root = bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)

    print("\nMin value:", bst.find_min(bst.root).data) # 20
    print("Max value:", bst.find_max(bst.root).data)   # 80

    print("\nInorder before deletion:")
    bst.inorder(bst.root)                              # 20 30 40 50 60 70 80
    print()

    bst.root = bst.delete(bst.root, 50)

    print("Inorder after deleting 50:")
    bst.inorder(bst.root)                             # 20 30 40 60 70 80

    print("\nIs BST?:", bst.is_bst(bst.root))         # True

    print("\nHeight of tree:", bst.height(bst.root))  # e.g. 3
