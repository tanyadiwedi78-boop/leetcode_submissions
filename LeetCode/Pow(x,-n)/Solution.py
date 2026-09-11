1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        if n < 0:
4            x = 1 / x
5            n = -n
6        ans = 1
7        while n > 0:
8            if n % 2 == 1:
9                ans *= x
10            x *= x
11            n //= 2
12        return ans
13        