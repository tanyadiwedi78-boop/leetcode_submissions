1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
9        if root is None:
10
11            return None
12
13        root.left , root.right = root.right , root.left
14
15        # invert left subtree
16        self.invertTree(root.left)
17
18        # invert right subtree
19        self.invertTree(root.right)
20
21        return root
22        