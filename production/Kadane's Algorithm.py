
def max_subarray(nums):
    # Initialize variables
    max_sum = float('-inf')  # Track the maximum sum found so far
    current_sum = 0          # Track the sum of the current subarray
    start = 0                # Start index of the maximum subarray
    end = 0                  # End index of the maximum subarray
    temp_start = 0           # Temporary start index for the current subarray

    for i, num in enumerate(nums):
        # If the current sum is negative, reset it and update the temporary start index
        if current_sum < 0:
            current_sum = num
            temp_start = i
        else:
            current_sum += num

        # Update the maximum sum and the start/end indices if the current sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    # Extract the subarray with the maximum sum
    subarray = nums[start:end + 1]

    return max_sum, subarray


# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = max_subarray(nums)
print("Maximum Sum:", max_sum)  # Output: 6
print("Subarray:", subarray)    # Output: [4, -1, 2, 1]