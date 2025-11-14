# Todo: 0/1 Knapsack Problem using Dynamic Programming

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],  # include item
                    dp[i - 1][w]                                    # exclude item
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # The last cell dp[n][capacity] holds the answer
    return dp[n][capacity]

def knapsack_with_items(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w-weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    # 🔍 Backtrack to find selected items
    result = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:  # means item was chosen
            result.append(i-1)      # store index
            w -= weights[i-1]

    return dp[n][capacity], list(reversed(result))


if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    print("Maximum value in 0/1 Knapsack:", knapsack(values, weights, capacity))

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    max_value, items = knapsack_with_items(values, weights, capacity)

    print("Max value:", max_value)
    print("Items included (indices):", items)