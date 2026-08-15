1class Solution:
2    def findMiddleIndex(self, nums: List[int]) -> int:
3        n = len(nums)
4        left_sum = 0
5        total_sum = sum(nums)
6        for i in range(n):
7            right_sum = total_sum - left_sum - nums[i]
8            if left_sum == right_sum:
9                return i
10            left_sum += nums[i]
11        return -1
12
13
14        