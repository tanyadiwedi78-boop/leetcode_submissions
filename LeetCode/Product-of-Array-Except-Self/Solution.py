1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        result = [1] * n
5
6        # Left product tracks
7        left_product = 1
8        for i in range(n):
9
10            result[i] = left_product
11            left_product *= nums[i]
12
13        right_product = 1
14        for i in range(n - 1 , -1 ,-1):
15            result[i] *= right_product
16            right_product *= nums[i]
17
18        return result
19
20
21
22
23
24
25
26        