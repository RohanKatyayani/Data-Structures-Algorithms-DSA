'''
Concept Recap: -
Array: A collection of elements stores at contiguous memory location
Supports fast access (O(1)) but slow insert/delete in the middle (O(n))
In Python we use list.
'''

# Todo 1: Find largest and smallest element in an Array

def find_largest_smallest(arr):
    largest = arr[0]
    smallest = arr[0]

    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest

arr = [11, 26, 4, 57, 98, 2, 44]
print("Largest & Smallest: ", find_largest_smallest(arr))


# Todo 2: Reverse an Array

def reverse_array(arr):
    left, right = 0, len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 2, 3, 4, 5]
print("Array Reversed: ", reverse_array(arr))