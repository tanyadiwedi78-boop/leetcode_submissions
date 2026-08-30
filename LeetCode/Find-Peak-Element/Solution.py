1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        left = 0
4        right = len(nums) - 1
5        while left < right:
6            mid = (left + right) // 2
7            if nums[mid] > nums[mid + 1]:
8                right = mid
9            else:
10                left = mid + 1
11        return left
12
13