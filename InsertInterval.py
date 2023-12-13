from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Append the new interval to the list of intervals.
        intervals.append(newInterval)

        # Sort the list of intervals based on the starting points of each interval.
        intervals = sorted(intervals, key=lambda x: x[0])

        # Initialize a result list with the first interval.
        ans = [intervals[0]]

        # Iterate through the sorted intervals to merge overlapping intervals.
        for interval in intervals:
            # If the starting point of the current interval is greater than the end of the last interval in the result,
            # add the current interval to the result list.
            if interval[0] > ans[-1][1]:
                ans.append(interval)
            # If the end of the current interval is greater than the end of the last interval in the result,
            # update the end of the last interval in the result to be the end of the current interval.
            elif interval[1] > ans[-1][1]:
                ans[-1][1] = interval[1]

        # Return the merged intervals.
        return ans
