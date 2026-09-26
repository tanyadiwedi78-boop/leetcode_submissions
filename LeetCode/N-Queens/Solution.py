1class Solution:
2    def solveNQueens(self, n: int) -> list[list[str]]:
3        res = []
4        cols = set()
5        posDiag = set()
6        negDiag = set()
7
8        board = [["."] * n for _ in range(n)]
9
10        def backtrack(r):
11            # base case if we have successfully placed all queen in all  rows 
12            if r == n :
13                copy = ["".join(row) for row in board]
14                res.append(copy)
15                return 
16
17            # trying placing the queen in each column of the current loop
18            for c in range(n):
19                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
20                    continue
21
22                cols.add(c)
23                posDiag.add(r + c)
24                negDiag.add(r - c)
25                board[r][c] = "Q"
26
27                # Move to the next row
28                backtrack(r + 1)
29
30                cols.remove(c)
31                posDiag.remove(r + c)
32                negDiag.remove(r - c)
33                board[r][c] = "."
34
35        backtrack(0)
36
37        return res
38
39
40        