1class Solution:
2    def reverseWords(self, s: str) -> str:
3        # pattern -> string manipulation
4        ans = []
5        i = len(s) - 1
6        while i >= 0:
7
8            while i >= 0 and s[i] == " ":
9                i -= 1
10            if i < 0:
11                break
12
13            # find start of the current word
14            j = i
15            while i >= 0 and s[i] != " ":
16                i -= 1
17            ans.append(s[i + 1 : j + 1])
18
19            
20        return " ".join(ans)
21        