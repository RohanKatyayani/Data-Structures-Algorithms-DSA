# Todo: Fractional Knapsack Problem
"""
Definition: Consider you have a bag which has a limited weight (capacity) and some items each with a weight and a value. The goal is
to carry the maximum value you can in the capacity. You can carry fraction of items, such as let's say, half a gold bar.
"""
'''
Strategy: At each step, pick the item that gives you the highest value per unit weight (value / weight).
Keep adding items (or fractions) until your knapsack is full.
Algorithm
	1.	Compute value_per_weight for each item.
	2.	Sort items in descending order of value_per_weight.
	3.	Keep adding items:
	    •	If it fits entirely → add it fully.
	    •	If not → take the fraction that fits.
	4.	Stop when capacity is full.
Time complexity → O(n log n) (for sorting)
Space → O(1) (in-place or minimal extra)
'''

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(items, capacity):
    # Sort by value/weight ratio (descending)
    items.sort(key=lambda item: item.value/item.weight, reverse=True)

    total_value = 0.0
    for item in items:
        if capacity <= 0:
            break
        if item.weight <= capacity:
            # Take the whole item
            total_value += item.value
            capacity -= item.weight
        else:
            # Take fraction of item
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0

    return total_value

if __name__ == "__main__":
    items = [
        Item(60, 10),   # value, weight
        Item(100, 20),
        Item(120, 30)
    ]
    capacity = 50

    max_value = fractional_knapsack(items, capacity)
    print(f"Maximum value in Knapsack = {max_value}")