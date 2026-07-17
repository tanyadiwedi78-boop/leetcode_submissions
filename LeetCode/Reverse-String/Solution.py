1class Solution:
2    def reverseString(self, s: List[str])-> None:
3        left , right = 0 , len(s) - 1
4        while left < right:
5            s[left] , s[right] = s[right] , s[left]
6            left += 1
7            right -= 1
8
9        
10
11        