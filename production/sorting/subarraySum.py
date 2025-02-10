def subarraySum(nums, k):
    prefix_sum_count = {0: 1}  # Initialize with 0 sum count
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num  # Compute prefix sum
        if prefix_sum - k in prefix_sum_count:
            count += prefix_sum_count[prefix_sum - k]  # Increment count if (prefix_sum - k) exists
        prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

    return count

# Example usage:
nums1 = [1, 1, 1]
k1 = 2
print(subarraySum(nums1, k1))  # Output: 2

nums2 = [1, 2, 3]
k2 = 3
print(subarraySum(nums2, k2))  # Output: 2