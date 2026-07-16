1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        n = len(s)
4        left , right = 0 , len(s) - 1
5        while left < right:
6            while left < right and not s[left].isalnum():
7                left += 1
8
9            while left < right and not s[right].isalnum():
10                right -= 1
11
12            if s[left].lower() != s[right].lower():
13                    return False
14
15            left += 1
16            right -= 1
17        return True
18
19
20            
21        