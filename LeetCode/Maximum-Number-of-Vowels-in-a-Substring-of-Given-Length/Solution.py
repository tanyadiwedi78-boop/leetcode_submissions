1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        vowels = set("aeiou")
4        count = sum(1 for char in s[:k] if char in vowels)
5        max_count = count
6        
7        for i in range(k , len(s)):
8            if s[i] in vowels:
9                count += 1
10
11            if s[i - k] in vowels:
12                count -= 1
13
14            max_count = max(max_count , count)
15
16        return max_count
17            