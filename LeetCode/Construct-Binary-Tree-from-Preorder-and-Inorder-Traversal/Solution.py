1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
9        inorder_map = {val : idx for idx , val in enumerate(inorder)}
10
11        pre_idx = 0 # root of preorder 
12
13        def helper(left_in , right_in):
14            nonlocal pre_idx 
15
16            if left_in > right_in:
17                return None
18
19            root_val = preorder[pre_idx]
20            root = TreeNode(root_val)
21            pre_idx += 1
22            mid_idx = inorder_map[root_val]
23            root.left = helper(left_in, mid_idx - 1)
24            root.right = helper(mid_idx + 1, right_in)
25
26            return root
27
28        return helper(0, len(inorder) - 1)
29
30        