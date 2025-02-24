from typing import List

def maxSegments(n: int, x: int, y: int, z: int) -> int:
    # Initialize DP array with -1 (impossible states)
    dp = [-1] * (n + 1)
    dp[0] = 0  # Base case: 0-length rod has 0 segments

    # Iterate over all rod lengths
    for i in range(n + 1):
        if dp[i] != -1:  # If it's possible to reach this length
            if i + x <= n:
                dp[i + x] = max(dp[i + x], dp[i] + 1)
            if i + y <= n:
                dp[i + y] = max(dp[i + y], dp[i] + 1)
            if i + z <= n:
                dp[i + z] = max(dp[i + z], dp[i] + 1)

    return dp[n] if dp[n] != -1 else 0  # If we can't reach `n`, return 0

# Example Test Cases
print(maxSegments(7, 5, 2, 3))  # Output: 3 (Segments: 2+2+3 or 5+2)
print(maxSegments(10, 2, 3, 5))  # Output: 5 (Segments: 2+2+2+2+2)