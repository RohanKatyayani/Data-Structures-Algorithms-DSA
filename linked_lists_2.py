class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Todo 1: Insert at a specific position in a Linked List

    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if pos == 0: # Insert at head
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for i in range(pos - 1):
            if current is None:
                print("Position is out of range")
                return
            current = current.next

        new_node.next = current.next
        current.next = new_node

    # Todo 2: Delete by value (First Occurrence)

    def delete_by_value(self, key):
        cur = self.head
        prev = None

        while cur:
            if cur.data == key:
                if prev is None: # Deleting Head
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return True # Deleted
            prev, cur = cur, cur.next
        return False

    # Todo 3: Delete at position (0-based)

    def delete_at_position(self, pos):
        if pos < 0:
            raise IndexError("Negative Position not allowed")

        if self.head is None:
            raise IndexError("Delete from empty list")

        if pos == 0:
            self.head = self.head.next
            return

        cur = self.head
        idx = 0
        while cur and idx < pos - 1:
            cur = cur.next
            idx += 1

        if cur is None or cur.next is None:
            raise IndexError("Position out of range")

        cur.next = cur.next.next

    # Todo 4: Search for a Value

    def search(self, key):
        cur = self.head
        idx = 0
        while cur:
            if cur.data == key:
                return idx
            cur = cur.next
            idx += 1
        return -1

    # Todo 5: Reverse a Linked List
    # Todo 5.1: Iterative (Three pointers)

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    # Todo 5.2: Recursive

    def reverse_recursive(self):
        def _rev(node, prev=None):
            if node is None:
                return prev
            next = node.next
            return _rev(next, node)

        self.head = _rev(self.head)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example
ll = LinkedList()
ll.insert_at_position(10, 0)
ll.insert_at_position(20, 1)
ll.insert_at_position(30, 1)
ll.print_list() # 10 -> 30 -> 20 -> None
ll.delete_by_value(30)  # remove 30
ll.print_list()         # 10 -> 20 -> None
ll.delete_by_value(99)  # not present -> False
# Current: 10 -> 20 -> None
ll.insert_at_position(40, 2)  # 10 -> 20 -> 40
ll.print_list()
ll.delete_at_position(1)      # delete 20
ll.print_list()               # 10 -> 40 -> None
ll.search(10)  # 0
ll.search(40)  # 1
ll.search(99)  # -1
# Current: 10 -> 40 -> None
ll.reverse_iterative()
ll.print_list()  # 40 -> 10 -> None
ll.reverse_recursive()
ll.print_list()  # 10 -> 40 -> None  (back to original order)