# Todo 1: Check if Two BSTs are identical

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

    def is_identical(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (root1.data == root2.data and self.is_identical(root1.left, root2.left) and self.is_identical(root1.right, root2.right))

    # Todo 2: Convert BST into Doubly Linked List(DLL)
    def bst_to_dll(self, root):
        if not root:
            return None

        self.prev = None
        self.next = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            # If it's the first Node, set it as head.
            if self.prev is None:
                self.head = node
            else:
                self.prev.right = node
                node.left = self.prev

            self.prev = node # Move prev to curr
            inorder(node.right)

        inorder(root)
        return self.head

    # Todo 3: Find the Lowest Value Greater than a Given Key in BST (also called Ceiling in BST)
    def find_ceiling(self, root, key):
        ceil = None
        cur = root
        while cur:
            if cur.data == key:
                return cur
            elif cur.data < key:
                cur = cur.right
            else:
                ceil = cur
                cur = cur.left
            return ceil

if __name__ == "__main__":
    bst1 = BST()
    bst1.root = bst1.insert(None, 50)
    bst1.insert(bst1.root, 30)
    bst1.insert(bst1.root, 70)

    bst2 = BST()
    bst2.root = bst2.insert(None, 50)
    bst2.insert(bst2.root, 30)
    bst2.insert(bst2.root, 70)

    print("\nAre BST-1 and BST-2 Identical?")
    print("Answer: ",bst1.is_identical(bst1.root, bst2.root)) # True

    bst2.insert(bst2.root, 20)
    print("\nAre BST-1 and BST-2 Identical?")
    print("Answer: ",bst1.is_identical(bst1.root, bst2.root)) # False

    bst = BST()
    bst.root = bst.insert(None, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)

    dll_head = bst.bst_to_dll(bst.root)

    # Traverse DLL forward
    print("\nBST converted to DLL (forward):")
    curr = dll_head
    while curr:
        print(curr.data, end=" <-> ")
        last = curr
        curr = curr.right
    print("None")

    # Traverse DLL backward
    print("\nBST converted to DLL (backward):")
    while last:
        print(last.data, end=" <-> ")
        last = last.left
    print("None")

    key = 65
    node = bst.find_ceiling(bst.root, key)
    print(f"\nCeiling of {key}:", node.data if node else "Not Found")  # 70

    key = 25
    node = bst.find_ceiling(bst.root, key)
    print(f"Ceiling of {key}:", node.data if node else "Not Found")    # 30

    key = 85
    node = bst.find_ceiling(bst.root, key)
    print(f"Ceiling of {key}:", node.data if node else "Not Found")    # Not Found
