# Linked Lists store elements in node scattered memory, each node has, Data (Value you store) & Pointer to the next node.
# Types: (Single -->), (--> Double -->), & (--> Circular -->)

# Todo 1: Define a Node

class Node:
    def __init__(self, data):
        self.data = data # Stores Data
        self.next = None # Pointer to next node

# Todo 2: Define LinkedList Class:

class LinkedList:
    def __init__(self):
        self.head = None # Start with an empty list

    # Todo 3: Traversal (Print Linked List)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Empty List")

    # Todo 4: Insert at the Beginning

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head # New node is pointing to old head
        self.head = new_node # Head now becomes new node

    # Todo 5: Insert at th End

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:       # Linked List is empty
            self.head = new_node
            return
        current = self.head
        while current.next:         # Last node Reached
            current = current.next
        current.next = new_node

    # Todo 6: Insert at position (1-based index)

    def insert_at_position(self, data, pos):
        if pos == 1:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        count = 1
        while current and count < pos - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range")
            return

        new_node.next = current.next
        current.next = new_node

    # Todo 7: Delete by Value

    def delete_node(self, key):
        current = self.head

        # if head node is to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print("Value not found")
            return

        prev.next = current.next
        current = None

# Todo 8: Use and provide examples

# Create linked list
ll = LinkedList()

# Insert elements
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.print_list()     # 10 -> 20 -> 30 -> None

ll.insert_at_beginning(5)
ll.print_list()     # 5 -> 10 -> 20 -> 30 -> None

ll.insert_at_position(15, 3)
ll.print_list()     # 5 -> 10 -> 15 -> 20 -> 30 -> None

# Delete a node
ll.delete_node(20)
ll.print_list()     # 5 -> 10 -> 15 -> 30 -> None