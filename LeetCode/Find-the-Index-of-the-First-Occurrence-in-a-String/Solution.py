1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        n = len(haystack)
4        m = len(needle)
5        for i in range(n - m + 1):
6            j = 0
7            while j < m and haystack[i + j] == needle[j]:
8                j += 1
9                
10            if j == m:
11                return i
12        return -1
13
14         