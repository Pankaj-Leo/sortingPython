def subsetSum(nums, target):
    n = len(nums)
    count = 0
    for mask in range(0, 1 << n):  # Iterate through all subsets
        subset_sum = 0
        for i in range(n):
            if mask & (1 << i):  # Check if the i-th element is in the subset
                subset_sum += nums[i]
        if subset_sum == target:
            count += 1
    return count


# Example
nums = [1, 2, 3]
target = 3
print("Number of subsets:", subsetSum(nums, target))