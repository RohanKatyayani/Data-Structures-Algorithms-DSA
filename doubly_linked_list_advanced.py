class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None # Back pointer

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    def delete_by_value(self, key):
        cur = self.head
        while cur:
            if cur.data == key:
                if cur.prev:                 # Middle or Tail
                    cur.prev.next = cur.next
                else:                        # Head
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                return True
            cur = cur.next
        return False

    def traverse_forward(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    def traverse_backward(self):
        cur = self.head
        if not cur:
            print("None")
            return
        while cur.next:
            cur = cur.next
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.prev
        print("None")

    # Todo 1: Delete at the Beginning

    def delete_at_beginning(self):
        if self.head is None:
            raise IndexError("Delete from empty list")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # Todo 2: Delete at the End

    def delete_at_end(self):
        if self.head is None:
            raise IndexError("Delete from empty list")
        if self.head.next is None:
            self.head = None
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        # current is tail
        cur.prev.next = None

    # Todo 3: Insert at position (0 based)

    def insert_at_position(self, data, pos):
        if pos < 0:
            raise IndexError("Negative Position not allowed")
        if pos == 0:
            self.insert_at_beginning(data)
            return
        if self.head is None:
            raise IndexError("Position out of Range")
        cur = self.head
        idx = 0
        while cur and idx < pos -1:
            cur = cur.next
            idx += 1
        if cur is None:
            raise IndexError("Position out of Range")
        new_node = Node(data)
        new_node.prev = cur
        new_node.next = cur.next
        if cur.next:
            cur.next.prev = new_node
        cur.next = new_node

    # Todo 4: Reverse Doubly Linked List (in-place)

    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            cur.prev, cur.next = cur.next, cur.prev # Swap Pointers
            last = cur
            cur = cur.prev                          # Because Pointers swapped, new head is the last node visited.
        if last:
            self.head = last

# Todo: Perform some Actions!

if __name__ == "__main__":
    dll = DoublyLinkedList()
    for x in [10, 20, 30]:
        dll.insert_at_beginning(x)
    print("start (forward):")
    dll.traverse_forward()  # 10 -> 20 -> 30 -> None

    print("delete_at_beginning:")
    dll.delete_at_beginning()  # remove 10
    dll.traverse_forward()  # 20 -> 30 -> None

    print("delete_at_end:")
    dll.delete_at_end()  # remove 30
    dll.traverse_forward()  # 20 -> None

    print("insert_at_position(15, 0)  (head)")
    dll.insert_at_position(15, 0)  # 15 -> 20
    dll.traverse_forward()

    print("insert_at_position(25, 2)  (tail/end)")
    dll.insert_at_position(25, 2)  # 15 -> 20 -> 25
    dll.traverse_forward()

    print("insert_at_position(18, 2)  (middle)")
    dll.insert_at_position(18, 2)  # 15 -> 20 -> 18 -> 25
    dll.traverse_forward()
    print("backward:")
    dll.traverse_backward()  # 25 -> 18 -> 20 -> 15 -> None

    print("reverse:")
    dll.reverse()  # 25 -> 18 -> 20 -> 15
    dll.traverse_forward()
    print("backward after reverse:")
    dll.traverse_backward()