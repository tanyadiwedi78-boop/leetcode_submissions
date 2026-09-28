1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
9        inorder_idx = {val : idx for idx , val in enumerate(inorder)}
10
11        def helper(left_in , right_in)-> TreeNode | None:
12            if left_in > right_in:
13                return None
14
15            root_val = postorder.pop() # pop the last value from the post order 
16            root = TreeNode(root_val)
17            
18            root_idx = inorder_idx[root_val]
19
20            root.right = helper(root_idx+1 , right_in)
21            root.left = helper(left_in , root_idx - 1)
22        
23
24            return root
25
26        return helper(0 , len(inorder) - 1)
27
28        
29
30        