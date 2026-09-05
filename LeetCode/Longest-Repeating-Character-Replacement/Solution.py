1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        count = {}
4        max_freq = 0
5        left = 0
6        max_length = 0
7        for right in range(len(s)):
8
9        # Include the right character in the window
10            count[s[right]] = count.get(s[right], 0) + 1
11            max_freq = max(max_freq, count[s[right]])
12        
13        # Current window length is (right - left + 1)
14        # If invalid, shrink the window from the left
15            if (right - left + 1) - max_freq > k:
16                count[s[left]] -= 1
17                left += 1
18            
19        # Update the max length found so far
20        max_length = max(max_length, right - left + 1)
21        
22        return max_length
23        