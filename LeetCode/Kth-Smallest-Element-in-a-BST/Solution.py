1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
9        stack = []
10        curr = root
11
12        while curr or stack:
13            while curr:
14                stack.append(curr)
15
16                curr = curr.left
17
18            curr = stack.pop()
19            k -= 1
20
21            if k == 0:
22                return curr.val
23            curr = curr.right
24
25        
26        