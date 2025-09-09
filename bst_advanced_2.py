# Todo 1: Print all Root-to-Leaf Paths

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

    def print_paths(self, node, path=[]):
        if node is None:
            return
        path.append(node.data) # Adding current node to the Path

        # If leaf -> print the path
        if node.left is None and node.right is None:
            print(" -> ".join(map(str, path)))
        else:
            self.print_paths(node.left, path[:])   # Copy the path for left side
            self.print_paths(node.right, path[:])  # Copy the path for right side

    # Todo 2: Check if two Trees are identical

    def is_identical(self, node1, node2):
        if node1 is None and node2 is None: # Both empty
            return True
        if node1 is None or node2 is None:  # One empty, One not.
            return False
        # If both are non-empty -> check root + recurse
        return (node1.data == node2.data and
                self.is_identical(node1.left, node2.left) and
                self.is_identical(node1.right, node2.right))

    # Todo 3: Check if the Tree is height Balanced

    def is_balanced(self, node):
        def check(node):
            if node is None:
                return 0  # height = 0
            left = check(node.left)
            if left == -1:  # left not balanced
                return -1
            right = check(node.right)
            if right == -1:  # right not balanced
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)  # return height if balanced

        return check(node) != -1

if __name__ == "__main__":
    bst = BST()
    bst.root = bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)

    print("All Root-to-Leaf Paths:")
    bst.print_paths(bst.root)
    # Output:
    # 50 -> 30 -> 20
    # 50 -> 30 -> 40
    # 50 -> 70 -> 60
    # 50 -> 70 -> 80

    bst2 = BST()
    bst2.root = bst2.insert(bst2.root, 50)
    bst2.insert(bst2.root, 30)
    bst2.insert(bst2.root, 70)
    bst2.insert(bst2.root, 20)
    bst2.insert(bst2.root, 40)
    bst2.insert(bst2.root, 60)
    bst2.insert(bst2.root, 80)

    print("Are BST1 and BST2 identical?")
    print("Yes" if bst.is_identical(bst.root, bst2.root) else "No")

    print("Is tree balanced?", bst.is_balanced(bst.root))                # True

    # Create unbalanced tree
    unbalanced = BST()
    unbalanced.root = Node(10)
    unbalanced.root.left = Node(5)
    unbalanced.root.left.left = Node(2)
    print("Is tree balanced?", unbalanced.is_balanced(unbalanced.root))  # False