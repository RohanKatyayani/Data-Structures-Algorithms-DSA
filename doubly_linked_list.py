# Todo 1: Implement Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None # Has both forward and backward pointers

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Todo 2: Insert at the Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    # Todo 3: Insert at the End
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Todo 4: Delete a node by value
    def delete(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                # If it's the head
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next

    # Todo 5: Traverse Forward
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Todo 6: Traverse Backwards
    def traverse_backward(self):
        temp = self.head
        if temp is None:
            return
        # Go to last Node
        while temp.next:
            temp = temp.next
        # Now Traverse Backwards
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("None")

dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_beginning(5)
dll.insert_at_end(30)
print("Forward Traversal:")
dll.traverse_forward()
print("Backward Traversal:")
dll.traverse_backward()
print("Deleting 20...")
dll.delete(20)
print("Forward Traversal after deletion:")
dll.traverse_forward()