1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        i = len(a) - 1
4        j = len(b) - 1
5        carry = 0
6        result = []
7        while i >= 0 or j >=0 or carry:
8            total = carry
9            if i >= 0:
10                total += int(a[i])
11                i -= 1
12            if j >= 0:
13                total += int(b[j])
14                j -= 1
15            result.append(str(total % 2))
16            carry = total // 2
17        return "".join(result[::-1])
18        