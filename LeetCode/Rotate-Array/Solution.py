1class Solution:
2    def rotate(self, nums: list[int], k: int) -> None:
3        n = len(nums)
4        k = k %  n
5        def reverse(left , right):
6            while left < right:
7
8                nums[left] , nums[right] = nums[right] , nums[left]
9                left += 1
10                right -= 1
11        reverse(0 , n-1)
12
13        reverse(0, k-1)
14
15        reverse(k , n-1)
16        