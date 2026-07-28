1class Solution:
2    def findRepeatedDnaSequences(self, s: str) -> List[str]:
3        seen = set()
4        repeated = set()
5        left = 0
6        k = 10
7        while left + k <= len(s):
8            window = s[left:left+k]
9
10            if window in seen:
11                repeated.add(window)
12
13            else:
14                seen.add(window)
15
16            left += 1
17        return list(repeated)
18        