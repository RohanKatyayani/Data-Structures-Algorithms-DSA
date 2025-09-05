"""
RECURSION: - When a Function calls itself again & again it's called Recursion. Like when you want to find out the
factorial of 5, we do 5! -> 5 * 4! -> 5 * 4 * 3! and so on which gives us the answer 120 after calling itself for 5
times but as you notice, it will stop somewhere, at 0! in this case hence it keeps going deeper until the base case,
then it unwinds back up with results.
"""

# Todo 1: Factorial

def factorial(n):
    if n == 0:                  # Base Case
        return 1
    return n * factorial(n - 1) # Recursive Case

if __name__ == '__main__':
    print("Factorial of 5 is: ",factorial(5)) # 120

# Todo 2: Fibonacci Sequence (0,1,1,2,3,5,8,13,21...)

"""
fib(n) = fib(n-1) + fib(n-2)
"""

def fibonacci(n):
    if n == 0: return 0                       # Base case 1
    if n == 1: return 1                       # Base case 2
    return fibonacci(n-1) + fibonacci(n-2)    # Recursive Case

if __name__ == "__main__":
    print("Fibonacci of 6 is: ",fibonacci(6)) # 8

# Todo 3: Sum of Array (Recursive)

def sum_array(arr):
    if len(arr) == 0: return 0             # Base case
    return arr[0] + sum_array(arr[1:])     # Recursive case

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Sum of Array: ",sum_array(nums)) # 15

# Todo 4: Print Numbers using Recursion

# Todo 4.1: Print 1 -> N

def print_1_to_n(n):
    if n == 0: return   # Base case
    print_1_to_n(n - 1) # Recursive call first
    print(n, end = "")

# Todo 4.2: Print N -> 1

def print_n_to_1(n):
    if n == 0: return   # Base case
    print(n, end = "")
    print_n_to_1(n-1) # Recursive call after printing.