from collections import Counter
import heapq
from typing import List

class HeapSolution:
    """Heap-based solution to find the k most frequent elements."""
    def topKFrequent (self, nums: List[int], k: int) -> List [int]:
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val,key))
            else:
                heapq.heappushpop (heap, (val, key))
            return [h[1] for h in heap]
        # Time: O(n log k), Space: O(k)


class BucketSolution:
    """Bucket sort-based solution to find the k most frequent elements."""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * (n + 1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)

            ret = []
            for i in range(n, -1, -1):
                if buckets[i] != 0:
                    ret.extend(buckets[i])
                if len(ret) == k:
                    break
            return ret

if __name__ == "__main__":
    # Example values for nums and k
    nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5]
    k = 2

    print("Given nums:", nums)
    print("Value of k:", k)

    # Running both solutions
    heap_solution = HeapSolution()
    bucket_solution = BucketSolution()

    print("Heap Solution Output:", heap_solution.topKFrequent(nums, k))
    print("Bucket Solution Output:", bucket_solution.topKFrequent(nums, k))


