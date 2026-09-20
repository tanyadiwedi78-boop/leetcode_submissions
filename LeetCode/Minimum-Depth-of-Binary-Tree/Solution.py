1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def minDepth(self, root: TreeNode | None) -> int:
9        if not root:
10            return 0
11        if not root.left:
12            return self.minDepth(root.right) + 1
13        if not root.right:
14            return self.minDepth(root.left) + 1
15
16        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
17        