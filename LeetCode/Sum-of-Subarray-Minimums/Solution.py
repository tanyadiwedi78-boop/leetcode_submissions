1class Solution:
2    def sumSubarrayMins(self, arr: List[int]) -> int:
3        # monotonic stack contribution
4        MOD = 10**9 + 7
5        n = len(arr)
6        stack = []
7        left = [0] * n
8        right = [0] * n
9        # previous less
10        for i  in range(n):
11            while stack and arr[stack[-1]] > arr[i]:
12                stack.pop()
13            if stack:
14
15                left[i] = i - stack[-1]
16
17            else:
18                left[i] = i+1
19            stack.append(i)
20        stack = []
21        for i in range(n - 1 , -1 , -1):
22            while stack and arr[stack[-1]] >= arr[i]:
23                stack.pop()
24            if stack:
25                right[i] = stack[-1] - i
26            else:
27                right[i] = n - i
28            stack.append(i)
29        ans = 0
30        for i in range(n):
31            ans = (ans + arr[i] * left[i] * right[i]) % MOD
32
33        return ans
34
35
36
37        