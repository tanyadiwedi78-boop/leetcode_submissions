1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        if not strs:
4            return " "
5
6        for i in range(len(strs[0])):
7            chr = strs[0][i]
8
9            for string in strs[1:]:
10                # if the current string is shorter and chr do not match
11                if i == len(string) or string[i] != chr:
12                    return strs[0][:i]
13
14        return strs[0]
15
16        