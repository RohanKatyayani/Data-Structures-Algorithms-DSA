"""
What is a TREE??
A Tree is a hierarchical data structure. Instead of being linear like arrays, stacks, and queues, tree branches out.
"""

# Todo 1: Node + Binary Tree Class

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Todo 1.1: Preorder Traversal (Root -> Left -> Right)
    def preorder(self, node):
        if node:
            print(node.data, end=" -> ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Todo 1.2: Inorder Traversal (Left -> Root -> Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" -> ")
            self.inorder(node.right)

    # Todo 1.3: Postorder Traversal (Left -> Right -> Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" -> ")

    # Todo 2: Level Order Traversal (BSF using Queue)
    def level_order(self, node):
        if not node:
            return
        queue = [node]
        while queue:
            cur = queue.pop(0)
            print(cur.data, end=" -> ")
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

if __name__ == "__main__":
    # Build tree
    bt = BinaryTree()
    bt.root = Node(10)
    bt.root.left = Node(20)
    bt.root.right = Node(30)
    bt.root.left.left = Node(40)
    bt.root.left.right = Node(50)
    bt.root.right.right = Node(60)

    print("Preorder:")
    bt.preorder(bt.root)     # 10 20 40 50 30 60

    print("\nInorder:")
    bt.inorder(bt.root)      # 40 20 50 10 30 60

    print("\nPostorder:")
    bt.postorder(bt.root)    # 40 50 20 60 30 10

    print("\nLevel Order:")
    bt.level_order(bt.root)  # 10 20 30 40 50 60

# Todo 3: Binary Search Tree (BST)
"""
Rules: - Left Child  < Node
         Right Child > Node 
Searching & Inserting: - O(log n) 
"""

class BST:
    def __init__(self):
        self.root = None

    # Todo 3.1: Insert into BST
    def insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        return node

    # Todo 3.2: Search in BST
    def search(self, node, key):
        if node is None or node.data == key:
            return node
        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    # Todo 3.3: Inorder Traversal (sorted output)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" -> ")
            self.inorder(node.right)

if __name__ == "__main__":
    bst = BST()
    bst.root = bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)

    print("Inorder (sorted):")
    bst.inorder(bst.root)   # 20 30 40 50 60 70 80

    print("\nSearch for 60:")
    found = bst.search(bst.root, 60)
    print("Found" if found else "Not Found")

    print("Search for 25:")
    found = bst.search(bst.root, 25)
    print("Found" if found else "Not Found")