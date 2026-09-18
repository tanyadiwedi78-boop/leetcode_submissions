1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: TreeNode | None) -> bool:
9        if not root:
10            return True
11
12        # helper function ot see the symmetric nodes in both trees
13        def symmetric(t1 , t2):
14            if not t1 and not t2:
15                return True
16            if not t1 or not t2:
17                return False
18
19            return ( t1.val == t2.val and symmetric(t1.left , t2.right) and symmetric(t1.right , t2.left))
20
21        return symmetric(root.left , root.right)
22        