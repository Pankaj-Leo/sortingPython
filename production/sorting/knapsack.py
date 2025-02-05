def knapsack(W, weights, values, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build DP table in bottom-up manner
    for i in range(1, n + 1):  # Items
        for w in range(W + 1):  # Capacity from 0 to W
            if weights[i - 1] <= w:
                # Max of including or excluding the item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # Item can't be included
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]  # Maximum value in knapsack


values = [3, 4, 5, 6] # Values of items
weights = [2, 3, 4, 5] # Weights of items
W = 50  # Knapsack capacity
n = len(values)
print (" Maximum value in the Knapsack =", knapsack (W,weights, values, n))