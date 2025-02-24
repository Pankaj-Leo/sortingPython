from typing import List
class Solution:
    def insert (self, intervals: List [List[int]], newInterval: List [int]) -> List [List[int]]:
        merged = []
        i = 0
        #Step 1: Add all interval that end before newInterval starts
        while i < len (intervals) and intervals [i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Step 2: Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1

        # Step 3: Add the merged newInterval
        merged.append(newInterval)

        # Step 4: Add remaining intervals after newInterval
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged

# Example Test Case
if __name__ == "__main__":
    solution = Solution()
    print(solution.insert([[1, 3], [6, 9]], [2, 5]))  # Output: [[1,5], [6,9]]
    print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))


