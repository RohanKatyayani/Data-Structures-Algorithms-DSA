# Todo 1: Problem 1: Next Greater Element (NGE)

def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n  # Default = -1
    stack = []         # This will store "Candidates" for next greater

    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Remove all elements smaller/equal to arr[i]
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If stack is not empty, top is the next greater
        if stack:
            result[i] = stack[-1]

        # Push this element into Stack
        stack.append(arr[i])

    return result

if __name__ == "__main__":
    arr = [4, 5, 2, 25]
    print("Array: ", arr)
    print("Next Greater Elements: ", next_greater_element(arr))

# Todo 2: Problem 2: Min Stack (Get Minimum in O(1))

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [] # Keeps track of minimums

    def push(self, val):
        self.stack.append(val)
        # Push to the min_stack if it's the first element or smaller than the current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            raise IndexError("Stack is empty")
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def peek(self):
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            raise IndexError("Stack is empty")
        return self.min_stack[-1]

if __name__ == "__main__":
    s = MinStack()
    s.push(5)
    s.push(2)
    s.push(10)
    s.push(1)
    print("Current Min: ", s.get_min()) # 1
    s.pop()                             # Removes 1
    print("Current Min: ", s.get_min()) # 2
    s.pop()                             # Removes 10
    print("Current Min: ", s.get_min()) # 2

# Todo 3: Problem 3: Infix -> Postfix Conversion (Shunting Yard Algorithm)

"""
What is Shunting Yard Algorithm?
Shunting Yard Algorithm is just a set of rules to convert a normal math expression (Infix) into a form (Postfix) that's
easy for computers to calculate. Like, Operands (A,B,1,2) -> go straight to the output while Operators (+,-,*,/) wait
in the stack until they can be places correctly (Based on precedence and parentheses). And at the end dump everything 
from the stack to the output. 
"""

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for ch in expression:
        if ch.isalnum(): # Operand (A, B, 1, 2, ...)
            output.append(ch)
        elif ch == '(': stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(': output.append(stack.pop())
            stack.pop() # Remove (
        else: # Operator
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[ch]:
                output.append(stack.pop())
            stack.append(ch)

    while stack:
        output.append(stack.pop())
    return ''.join(output)

if __name__ == "__main__":
    expr = "A+(B*C)"
    print("Infix: ", expr)
    print("Postfix: ", infix_to_postfix(expr))  # ABC*+