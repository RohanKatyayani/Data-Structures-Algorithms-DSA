"""
QUEUE: - Just like it's name a Queue is like a line of elements in which the first element that enters is the first
element that exits unline stack, Queue works with FIFO or First in First Out.
"""

# Todo 1: Implement Queue using Python List

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data) # Add at End

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) # Remove first element from front
        raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Front element:", q.peek())  # 10
    print("Dequeued:", q.dequeue())  # 10
    print("Queue now:", q.queue)  # [20, 30]

# Todo 2: Implement Queue using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None: # Queue is Empty
            self.front = self.rear = new_node
            return
        self.rear.next = new_node # Link old rear to new node
        self.rear = new_node      # Update rear

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        val = self.front.data
        self.front = self.front.next
        if self.front is None: # Queue became empty
            self.rear = None
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def traverse(self):
        cur = self.front
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

if __name__ == "__main__":
    q = QueueLL()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.traverse()                # 10 -> 20 -> 30 -> None
    print("Front element:", q.peek())  # 10
    print("Dequeued:", q.dequeue())    # 10
    q.traverse()                # 20 -> 30 -> None

# Todo 3: Implement Queue using collections.deque

from collections import deque

class QueueDeque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data) # At Rear

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.popleft() # Remove from Front

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __str__(self):
        return " -> ".join(map(str, self.queue)) + " -> None"

if __name__ == "__main__":
    q = QueueDeque()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue:", q)           # 10 -> 20 -> 30 -> None
    print("Front:", q.peek())    # 10
    print("Dequeued:", q.dequeue())  # 10
    print("Queue now:", q)       # 20 -> 30 -> None

# Todo 4: Implement Circular Queue

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear +1) % self.capacity == self.front

    def enqueue(self, data):
        if self.is_full():
            raise OverflowError("Queue is full")

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        val = self.queue[self.front]

        if self.front == self.rear: # Single Element in the Queue
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def __str__(self):
        if self.is_empty():
            return "Empty Queue"

        result = []
        i = self.front
        while True:
            result.append(str(self.queue[i]))
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        return " -> ".join(result) + " -> None"

if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    print(cq)  # 10 -> 20 -> 30 -> 40 -> None
    print("Dequeued:", cq.dequeue())  # 10
    print(cq)  # 20 -> 30 -> 40 -> None
    cq.enqueue(50)
    cq.enqueue(60)
    print(cq)  # 20 -> 30 -> 40 -> 50 -> 60 -> None
    print("Front:", cq.peek())  # 20