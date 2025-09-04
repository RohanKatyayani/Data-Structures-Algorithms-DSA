# Todo 1: Problem 1: Implement Stack using Queue

from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if not self.q1:
            raise IndexError("Pop from empty stack")

        # Leave last element in q1, push others to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        popped = self.q1.popleft()

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        return popped

    def peek(self):
        if not self.q1:
            raise IndexError("Peek from empty stack")

        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        top = self.q1.popleft()
        self.q2.append(top)  # put it back

        # Swap queues
        self.q1, self.q2 = self.q2, self.q1
        return top

    def is_empty(self):
        return not self.q1

if __name__ == "__main__":
    s = StackUsingQueues()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top:", s.peek())    # 30
    print("Pop:", s.pop())     # 30
    print("Pop:", s.pop())     # 20
    print("Is empty:", s.is_empty())  # False
    print("Pop:", s.pop())     # 10
    print("Is empty:", s.is_empty())  # True

# Todo 2: Problem 2: Implement Queue using Stack

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:   # if stack2 empty, refill from stack1
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Dequeue from empty queue")
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Peek from empty queue")
        return self.stack2[-1]

    def is_empty(self):
        return not (self.stack1 or self.stack2)


if __name__ == "__main__":
    q = QueueUsingStacks()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Front:", q.peek())     # 10
    print("Dequeued:", q.dequeue())  # 10
    print("Dequeued:", q.dequeue())  # 20
    print("Is empty:", q.is_empty()) # False
    print("Dequeued:", q.dequeue())  # 30
    print("Is empty:", q.is_empty()) # True

# Todo 3: **Problem 3: ROTTEN ORANGES (BFS WITH QUEUE) (LEETCODE #994)**

from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    # Step 1: Count fresh oranges + enqueue all rotten ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c, 0))  # store row, col, time
            elif grid[r][c] == 1:
                fresh += 1

    # Directions for 4 neighbors
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    minutes = 0

    # Step 2: BFS
    while q:
        r, c, minutes = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc, minutes + 1))

    return minutes if fresh == 0 else -1


if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print("Minutes to rot:", orangesRotting(grid))  # 4

# Todo 4: Problem 4: Sliding Window Maximum (LeetCode #239)

from collections import deque

def max_sliding_window(nums, k):
    q = deque()  # store indexes
    result = []

    for i, num in enumerate(nums):
        # 1. Remove smaller elements from back
        while q and nums[q[-1]] < num:
            q.pop()

        # 2. Add current index
        q.append(i)

        # 3. Remove front if out of window
        if q[0] <= i - k:
            q.popleft()

        # 4. Append max (front) to result once window forms
        if i >= k - 1:
            result.append(nums[q[0]])

    return result


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print("Array:", nums)
    print("Sliding Window Max:", max_sliding_window(nums, k))