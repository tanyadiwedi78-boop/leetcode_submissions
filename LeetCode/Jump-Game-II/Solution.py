1class Solution:
2    def jump(self, nums: list[int]) -> int:
3        jumps = 0
4        current_end = 0
5        farthest = 0
6        for i in range(len(nums) - 1):
7            farthest = max(farthest , i + nums[i])
8            if i == current_end:
9
10                jumps += 1
11                current_end = farthest
12        return jumps
13        