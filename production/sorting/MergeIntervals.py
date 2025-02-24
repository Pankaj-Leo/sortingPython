from typing import List

class MergeIntervals:
    """ Merges overlapping intervals using extra space. """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        merged= []

        for interval in intervals:
            # If merged is empty OR current interval does NOT overlap with last merged interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append (interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
            # Time Complexity: O(n log n) (sorting) + O(n) (merging) = O(n log n)
            # Space Complexity: O(n) (storing merged intervals)

class InPlaceMergeIntervals:
    """ Merges overlapping intervals in-place with O(1) extra space. """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        i = 0  # Index to track merged intervals
        n = len(intervals)

        for j in range(1, n):
            # If current interval overlaps with previous
            if intervals[i][1] >= intervals[j][0]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])  # Merge
            else:
                i += 1
                intervals[i] = intervals[j]  # Move to next non-overlapping interval

        return intervals[:i+1]  # Return only relevant merged portion

        # Time Complexity: O(n log n)
        # Space Complexity: O(1)


if __name__ == "__main__":
    # Taking input from user
    # print("Enter intervals as space-separated pairs (e.g., 1 3 2 6 8 10 15 18):")
    # interval_input = list(map(int, input().split()))
    #
    # # Convert flat input list into list of interval pairs
    # intervals = [[interval_input[i], interval_input[i + 1]] for i in range(0, len(interval_input), 2)]

    intervals = [
        [1, 3],
        [2, 6],
        [8, 10],
        [15, 18]
    ]

    # Running both solutions
    merge_solution = MergeIntervals()
    in_place_solution = InPlaceMergeIntervals()

    print("\nOriginal Intervals:", intervals)
    print("\nMergeIntervals Output:", merge_solution.merge(intervals.copy()))
    print("\nInPlaceMergeIntervals Output:", in_place_solution.merge(intervals.copy()))