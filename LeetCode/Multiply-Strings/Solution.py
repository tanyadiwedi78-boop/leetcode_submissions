1class Solution:
2    def multiply(self, num1: str, num2: str) -> str:
3        if num1 == "0" or num2 == "0":
4            return "0"
5
6        m = len(num1)
7        n = len(num2)
8        res = [0] * (m + n)
9
10        for i in range(m - 1 , -1 , -1):
11            for j in  range(n - 1 , -1 , -1):
12                digit1 = ord(num1[i]) - ord("0")
13                digit2 = ord(num2[j]) - ord("0")
14
15                product = digit1 * digit2
16
17                pos1 = i + j
18                pos2 = i + j + 1
19                total = product + res[pos2]
20                res[pos2] = total % 10
21                res[pos1] += total // 10
22        return "".join(map(str , res)).lstrip("0")
23        