1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        length = len(nums)
4        if length <= 2:
5            return length
6
7        k = 2
8        for i in range(2 , length):
9            if nums[i] != nums[k -2]:
10                nums[k] = nums[i]
11                k += 1
12
13        return k
14        