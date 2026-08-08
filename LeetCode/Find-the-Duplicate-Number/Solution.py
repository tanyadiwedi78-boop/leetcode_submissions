1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        slow  = nums[0]
4        fast = nums[0]
5        # 1ST PART -> CYCLE EXISTS OR NOT
6        while True:
7            slow = nums[slow]
8            fast = nums[nums[fast]]
9            if slow == fast:
10                break
11        # 2ND PART -> Find Entrance Part
12        slow = nums[0]
13        while slow != fast:
14            slow = nums[slow]
15            fast = nums[fast]
16        return slow
17