1class Solution:
2    def arrangeCoins(self, n: int) -> int:
3        left , right = 0 , n
4        while left <= right:
5            mid = (left + right) // 2
6            curr_coins = mid * (mid + 1) // 2
7        
8            if curr_coins == n:
9
10                return mid
11            elif curr_coins < n:
12                left = mid + 1
13            else:
14                right = mid - 1
15            
16        return right
17
18        