from typing import List


class Permutations:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res


# Example Usage
nums = [1, 2, 3, 4, 5]
solution = Permutations()
output = solution.permute(nums)
print(output)
