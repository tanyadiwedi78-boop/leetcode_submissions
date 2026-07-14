1class Solution:
2
3    def maxProduct(self, nums: List[int]) -> int:
4        max_product = nums[0]
5        min_product = nums[0]
6        result = nums[0]
7    
8        for i in range(1, len(nums)):
9            num = nums[i]
10        
11        # if num is negative, max and min swap roles
12            if num < 0:
13                max_product, min_product = min_product, max_product
14        
15            max_product = max(num, max_product * num)
16            min_product = min(num, min_product * num)
17        
18            result = max(result, max_product)
19    
20        return result
21
22
23
24
25            
26        