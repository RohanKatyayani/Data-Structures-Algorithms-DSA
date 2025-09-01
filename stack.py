"""
Stack. What is Stack? Just like the name suggests Stack is like a pile of boxes or plates. You keep on adding things
onto the Stack in a form that the new thing goes on top of the old thing. Now when you remove something from a Stck
you remove the top thing first, this is called 'Last in First Out' or LIFO. This is how Stack Works.
You Push the first element in an empty stack and keep on pushing elements as many as you want but when you Pop (Remove)
an element, the last pushed element will be removed from the Stack. Let's see how this works in the Code.
"""

# Todo 1: Implement Stack using Python List

class Stack:
    def __init__(self):
        self.stack = [] # An empty list

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Cannot Pop from empty Stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Cannot Peek from empty Stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Let's fo some Push Pop now.
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top element:", s.peek())  # 30
    print("Popped:", s.pop())        # 30
    print("Stack now:", s.stack)     # [10, 20]

# Todo 2: Implement Stack using Linked List

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top # New node points to old top
        self.top = new_node      # Update Top

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot Pop from empty Stack")
        popped = self.top.data
        self.top = self.top.next # Move top down
        return popped

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot Peek from empty Stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def traverse(self):
        cur = self.top
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

if __name__ == "__main__":
    s = StackLL()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top element:", s.peek()) # 30
    print("Popped:", s.pop())       # 30
    s.traverse()                    # 20 -> 10 -> None

# Todo 3: Problem 1: Reverse a String using Stack

def reverse_string(s):
    stack = []
    for ch in s:
        stack.append(ch)    # Push

    rev = ""
    while stack:
        rev += stack.pop()  # Pop

    return rev

if __name__ == "__main__":
    print(reverse_string("Hello!")) # !olleh
    print(reverse_string("Rohan"))  # nahor

# Todo 4: Problem 2: Balanced Parentheses

def is_balanced(expr):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop() # Matched and Removed from Stack

    return len(stack) == 0

if __name__ == "__main__":
    print(is_balanced("({[]})"))  # True
    print(is_balanced("((])"))    # False
    print(is_balanced("{[()]}"))  # True
    print(is_balanced("{[(])}"))  # False