1class Solution:
2    def reverse(self, x: int) -> int:
3        sign = -1 if x < 0 else 1
4        x = abs(x)
5    
6        result = 0
7        while x != 0:
8            digit = x % 10
9            x = x // 10
10            result = result * 10 + digit
11    
12        result = sign * result
13    
14        # 32-bit signed integer range check
15        if result < -2**31 or result > 2**31 - 1:
16            return 0
17    
18        return result
19
20        