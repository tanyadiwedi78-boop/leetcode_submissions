1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        # pattern -> Prefix sum + Hashmap
4        prefix = 0
5        count = 0
6        mp = {0 : 1}
7        for num in nums:
8            prefix += num
9            if prefix - k in mp:
10                count += mp[prefix - k]
11            mp[prefix] = mp.get(prefix , 0) + 1
12        return count
13
14        