1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3
4        nums.sort()
5        n = len(nums)
6        ans = []
7        for i in range(n-3):
8            if i > 0 and nums[i] == nums[i-1]:
9                continue
10            for j in range(i + 1 , n-2):
11                if j > i + 1 and nums[j] == nums[j -1]:
12                    continue
13                left = j + 1
14                right = n - 1
15                while left < right:
16                    total = nums[i] + nums[j] + nums[left] + nums[right]
17                    if total == target:
18                        ans.append([nums[i] , nums[j] , nums[left] , nums[right]])
19                        left += 1
20                        right -= 1
21                        while left < right and nums[left] == nums[left - 1]:
22                            left += 1
23                        while left < right and nums[right] == nums[right + 1]:
24                            right -= 1
25                    elif total < target:
26                        left +=1
27                    else: 
28                        right -= 1
29        return ans                
30
31                    
32        
33        