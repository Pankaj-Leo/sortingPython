from typing import List


class maxSumNonAdjacentClass:
    def maxSumNonAdjacent(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n + 1....]

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2


# Example Input
nums = [3, 2, 5, 10, 7, 9]
sol = maxSumNonAdjacentClass()
print("Maximum Sum of Non-Adjacent Elements:", sol.maxSumNonAdjacent(nums))