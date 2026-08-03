1class Solution:
2    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
3        
4
5
6        n = len(matrix)
7        # using Binary Search 
8        def countLessEqual(mid):
9            row = n - 1
10            col = 0
11            count = 0
12            while row >= 0 and col < n:
13                if matrix[row][col] <= mid:
14                    count += row + 1
15                    col += 1
16                else:
17                    row -= 1
18            return count
19        low = matrix[0][0]
20        high = matrix[-1][-1]
21        while low < high:
22            mid = (low + high) // 2
23            if countLessEqual(mid) < k:
24                low = mid + 1
25            else:
26                high = mid
27        return low
28