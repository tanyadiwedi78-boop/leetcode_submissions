1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left = 0
4        right = len(nums) - 1
5        while left < right:
6            mid = (left + right) // 2
7            if nums[mid] > nums[right]:
8                left = mid + 1
9            else:
10                right = mid
11        return nums[left]
12
13
14        