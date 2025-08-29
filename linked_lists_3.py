# Todo 1: Find the middle element in a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def find_middle(self): # Find middle element using slow and fast pointers
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next        # Move 1 Step
            fast = fast.next.next   # Move 2 Steps

        if slow:
            return slow.data
        return None

    # Todo 2: Detect a cycle in a linked list (loop detection)

    def detect_cycle(self): # Using Floyd's Cycle Detection Algorithm
        """
        Floyd's Cycle Detection Algorithm uses two pointers, Slow and Fast. We move Slow by 1 step, and Fast by 2 steps.
        If there's a cycle, Slow and Fast will meet at some point. If there's no cycle, Fast will reach None.
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True # Cycle Detected

        return False # Cycle Not Detected

    # Todo 3: Detect the starting node of the cycle.
    """
    First, we'll use Floyd's Cycle Detection Algorithm until the Fast and the Slow pointers meet. Once they meet, 
    we will reset one pointer to head, then move both pointers one step at a time. The Node where they will meet 
    again, will the be the starting node of the cycle.    
    """

    def find_cycle_start(self):
        slow = self.head
        fast = self.head

        # Step 1: Detect Cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None # No Cycle

        # Step 2: Find cycle start
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow # Start of the Cycle.

    # Todo 4: Removing the Cycle in a linked list
    """
    Cycle's mess up traversals, so to remove them, first we detect the cycle using Floyd's Cycle Detection Algorithm.
    Find the start of the Cycle, traverse the cycle until we reach the last node and change that node's next = None. 
    """

    def remove_cycle(self):
        slow = self.head
        fast = self.head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return # No Cycle

        # Step 2: Find start of Cycle
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Step 3: Find the last node in the Cycle
        cycle_start = slow
        ptr = cycle_start
        while ptr.next != cycle_start:
            ptr = ptr.next

        # Break the cycle
        ptr.next = None

# Example usage
ll = LinkedList()
for i in [10, 20, 30, 40, 50]:
    ll.append(i)
ll.print_list()
print("Middle Element: ", ll.find_middle())
ll = LinkedList() # Create a linked list
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.head.next.next.next.next = ll.head.next # Creating a cycle manually (40 → 20)
print(ll.detect_cycle())  # True
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
# Create cycle: 50 → 30
ll.head.next.next.next.next.next = ll.head.next.next
start = ll.find_cycle_start()
if start:
    print("Cycle starts at node:", start.data)
else:
    print("No cycle found")
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
# Create cycle: 50 → 30
ll.head.next.next.next.next.next = ll.head.next.next
print("Cycle start before removal:", ll.find_cycle_start().data)
ll.remove_cycle()
print("Cycle after removal:", ll.find_cycle_start())