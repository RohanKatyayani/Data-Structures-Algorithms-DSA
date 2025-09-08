# Todo 1: Lowest Common Ancestor (LCA) in BST

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

    # Lowest Common Ancestor
    def lca(self, node, p, q):
        if node is None:
            return None

        if p < node.data and q < node.data:
            return self.lca(node.left, p, q)

        if p > node.data and q > node.data:
            return self.lca(node.right, p, q)

        return node

if __name__ == "__main__":
    bst = BST()
    bst.root = bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)

    print("LCA of 20 and 40:", bst.lca(bst.root, 20, 40).data)  # 30
    print("LCA of 20 and 60:", bst.lca(bst.root, 20, 60).data)  # 50
    print("LCA of 60 and 80:", bst.lca(bst.root, 60, 80).data)  # 70

# Todo 2: Level Order Traversal (Breadth First Search with Queue)

from collections import deque

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

    def lca(self, node, p, q):
        if node is None:
            return None

        if p < node.data and q < node.data:
            return self.lca(node.left, p, q)

        if p > node.data and q > node.data:
            return self.lca(node.right, p, q)

        return node

    def level_order(self, node):
        if node is None:
            return
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            print(cur.data, end=" -> ")
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

if __name__ == "__main__":
    bst = BST()
    bst.root = bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)

    print("Level Order Traversal:")
    bst.level_order(bst.root)  # 50 -> 30 -> 70 -> 20 -> 40 -> 60 -> 80

# Todo 3: Left & Right View of Binary Tree

from collections import deque

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

    def lca(self, node, p, q):
        if node is None:
            return None

        if p < node.data and q < node.data:
            return self.lca(node.left, p, q)

        if p > node.data and q > node.data:
            return self.lca(node.right, p, q)

        return node

    def level_order(self, node):
        if node is None:
            return
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            print(cur.data, end=" -> ")
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

    def left_view(self, node):
        if not node:
            return
        queue = deque([node])
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                if i == 0:
                    print(cur.data, end=" -> ")
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        print("None")

    def right_view(self, node):
        if not node:
            return
        queue = deque([node])
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                if i == n - 1:
                    print(cur.data, end=" -> ")
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        print("None")

if __name__ == "__main__":
    bst = BST()
    bst.root = bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)

    print("Left View:")
    bst.left_view(bst.root)   # 50 -> 30 -> 20 -> None

    print("Right View:")
    bst.right_view(bst.root)  # 50 -> 70 -> 80 -> None