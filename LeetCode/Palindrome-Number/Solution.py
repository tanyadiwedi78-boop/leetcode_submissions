1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0 or (x % 10 == 0 and x!=0):
4            return False
5
6        reversed_half = 0
7        while x > reversed_half:
8            reversed_half = (reversed_half * 10) + (x % 10)
9            x //= 10
10
11        return x == reversed_half or x == reversed_half // 10
12
13        