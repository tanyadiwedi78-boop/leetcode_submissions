1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        if len(nums) <= 1:
4            return nums
5
6        mid = len(nums) // 2
7        left = self.sortArray(nums[ :mid])
8        right = self.sortArray(nums[mid: ])
9        return self.merge(left , right)
10
11    def merge(self , left , right):
12        result = []
13        i = j = 0
14        while i < len(left) and j < len(right):
15            if left[i] <= right[j]:
16                result.append(left[i])
17                i += 1
18            else:
19                result.append(right[j])
20                j += 1
21
22        result.extend(left[i: ])
23        result.extend(right[j: ])
24        return result
25
26
27
28        