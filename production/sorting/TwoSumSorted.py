class TwoSumSorted:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def findTwoSum(self):
        left, right = 0, len(self.numbers) - 1

        while left < right:
            curr_sum = self.numbers[left] + self.numbers[right]
            if curr_sum == self.target:
                return [left + 1, right + 1]  # Convert to 1-based index
            elif curr_sum < self.target:
                left += 1
            else:
                right -= 1
        return []

# Example Usage:
numbers = [2,7,11,15]
target = 9
solver = TwoSumSorted(numbers, target)
print(solver.findTwoSum())  # Output: [1,2]