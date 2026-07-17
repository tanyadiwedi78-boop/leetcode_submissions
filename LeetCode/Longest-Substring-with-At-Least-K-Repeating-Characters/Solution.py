1class Solution:
2    def longestSubstring(self, s: str, k: int) -> int:
3        if len(s) < k:
4            # pattern -> divide and conquer + Hashmap
5            return 0
6        count = Counter(s)
7        for ch in count:
8            if count[ch] < k:
9                return max(self.longestSubstring(part , k ) for part in s.split(ch))
10        return len(s)
11        