1class Solution:
2    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
3        result = []
4        i = 0
5        n = len(intervals)
6
7        # Phase 1: Add all intervals that end before the new interval starts
8        while i < n and intervals[i][1] < newInterval[0]:
9            result.append(intervals[i])
10            i += 1
11
12        # Phase 2: Merge all overlapping intervals with the new interval
13        while i < n and intervals[i][0] <= newInterval[1]:
14            newInterval[0] = min(newInterval[0] , intervals[i][0])
15            newInterval[1] = max(newInterval[1] , intervals[i][1])
16            i += 1
17
18
19        result.append(newInterval)
20
21        # Add all the remianing intervals that start after the newInterval
22        while i < n:
23            result.append(intervals[i])
24            i += 1
25
26        return result
27        