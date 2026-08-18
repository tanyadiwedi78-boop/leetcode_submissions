1class Solution:
2    def romanToInt(self, s: str) -> int:
3        values = {
4            "I" : 1,
5            "V" : 5,
6            "X" : 10,
7            "L" : 50,
8            "C" : 100,
9            "D" : 500,
10            "M" : 1000,
11        } 
12
13        total = 0
14        for i in range(len(s)):
15            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
16                total -= values[s[i]]
17            else:
18                total += values[s[i]]
19
20        return total
21        