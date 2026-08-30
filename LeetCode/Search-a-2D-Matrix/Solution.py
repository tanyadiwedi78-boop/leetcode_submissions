1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        rows = len(matrix)
4        cols = len(matrix[0])
5        left = 0
6        right = rows * cols - 1 # 60
7        while left <= right:
8            mid = (left + right) // 2
9            row = mid // cols
10            col = mid % cols
11
12            if matrix[row][col] == target:
13                return True
14
15            elif matrix[row][col] < target:
16                left = mid + 1
17
18            else: 
19                right = mid - 1
20        return False
21
22        