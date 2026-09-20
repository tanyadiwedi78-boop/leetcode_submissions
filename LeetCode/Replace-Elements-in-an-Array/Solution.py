1class Solution:
2    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
3        num_to_index = {val : idx for idx , val in enumerate(nums)}
4
5        for old_val , new_val in operations:
6            idx = num_to_index[old_val]
7
8            nums[idx] = new_val
9
10            num_to_index[new_val] = idx
11            del num_to_index[old_val] 
12
13        return nums
14
15        