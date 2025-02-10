from typing import List

class nextGreaterElementClass:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int])-> List[int]:
        next_greater= {}
        stack = []

        # Traverse nums2 and find next greater elements
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()]= num
            stack.append(num)

            #Fill the result array for nums1
        return [next_greater.get(num,-1) for num in nums1]

# Example usage
sol = nextGreaterElementClass()
print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))  # Output: [-1,3,-1]
print(sol.nextGreaterElement([2,4], [1,2,3,4]))    # Output: [3,-1]   # Output: [3,-1]