# Todo 1: Kth Smallest & Kth Largest in BST

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

    # Todo 1.1: Kth Smallest (Inorder Traversal)
    def kth_smallest(self, root, k):
        self.count = 0
        self.result = None

        def inorder(node):
            if not node or self.result:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node
                return
            inorder(node.right)

        inorder(root)
        return self.result

    # Todo 2: Kth Largest Element in BST
    def kth_largest(self, root, k):
        self.count = 0
        self.result = None

        def reverse_inorder(node):
            if not node or self.result:
                return
            reverse_inorder(node.right)
            self.count += 1
            if self.count == k:
                self.result = node
                return
            reverse_inorder(node.left)

        reverse_inorder(root)
        return self.result

    # Todo 3: Convert Sorted Array to Balanced BST
    def sorted_array_to_bst(self, arr):
        def build(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = Node(arr[mid])
            node.left = build(start, mid - 1)
            node.right = build(mid + 1, end)
            return node

        return build(0, len(arr) - 1)

    # Todo: Add Inorder Method
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

    print("Kth Smallest Tests:")
    for k in range(1, 6):
        node = bst.kth_smallest(bst.root, k)
        print(f"{k}th Smallest:", node.data if node else None)

    print("\nKth Largest Tests:")
    for k in range(1, 6):
        node = bst.kth_largest(bst.root, k)
        print(f"{k}th Largest:", node.data if node else None)

    bst = BST()
    root = None
    root = bst.insert(root, 50)
    bst.insert(root, 30)
    bst.insert(root, 70)
    bst.insert(root, 20)
    bst.insert(root, 40)
    bst.insert(root, 60)
    bst.insert(root, 80)

    k = 2
    node = bst.kth_largest(root, k)
    print(f"\n{k}th Largest Element:", node.data if node else "Not Found")  # 70

    bst = BST()
    arr = [10, 20, 30, 40, 50, 60, 70]
    root = bst.sorted_array_to_bst(arr)

    print("\nInorder traversal of BST from sorted array:")
    bst.inorder(root)                                                       # Should print sorted order: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> 70
    print()