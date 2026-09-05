1class Solution:
2    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
3        if k <= 1:
4            return 0
5        left = 0
6        product = 1
7        count = 0
8        for right in range(len(nums)):
9            product *= nums[right]
10            while product >= k:
11                product //= nums[left]
12                left += 1
13            count += right - left + 1
14        return count
15
16        