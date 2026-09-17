1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
9        result = []
10        def traverse(node):
11            if not node:
12                return
13
14            traverse(node.left)
15
16            traverse(node.right)
17
18            result.append(node.val)
19
20        traverse(root)
21        return result
22
23        