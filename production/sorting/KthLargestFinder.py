#TIme: 0(nlogn)
# Space: 0(1)

import heapq
from typing import List

class KthLargestFinder:
    @staticmethod
    def find_kth_largest_max_heap(nums: List[int], k: int)-> int:
        """Finds the k-th largest element using a max heap (negating values)."""
        for i in range(len(nums)):
            nums[i] = -nums[i]  # Convert to max heap representation

        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)

    # Max Heap of size n
    # Time: O(n + k log n)
    # Space: O(1)

    def find_kth_largest_min_heap(nums: List[int], k: int) -> int:
        """Finds the k-th largest element using a min heap of size k."""
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]

        # Min heap of size k
        # Time: O(n log k)
        # Space: O(k)
if __name__ == "__main__":
        nums = [3, 2, 1, 5, 6, 4, 8, 9]
        k = 3

        print("Using Max Heap:", KthLargestFinder.find_kth_largest_max_heap(nums.copy(), k))
        print("Using Min Heap:", KthLargestFinder.find_kth_largest_min_heap(nums.copy(), 4))

