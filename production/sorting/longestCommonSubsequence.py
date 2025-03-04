from functools import lru_cache

def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    @lru_cache(None)  # Memoization
    def lcs(i, j):
        if i == m or j == n:
            return 0
        if text1[i] == text2[j]:
            return 1 + lcs(i + 1, j + 1)
        return max(lcs(i + 1, j), lcs(i, j + 1))

    return lcs(0, 0)

# Example Test Cases
print(longestCommonSubsequence("abcde", "ace"))  # Output: 3
print(longestCommonSubsequence("abc", "abc"))  # Output: 3
print(longestCommonSubsequence("abc", "def"))  # Output: 0