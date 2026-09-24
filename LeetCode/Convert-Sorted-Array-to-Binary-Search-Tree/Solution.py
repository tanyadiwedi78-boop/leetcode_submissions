1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
9        def helper(left : int , right : int)-> Optional[TreeNode]:
10
11            if left > right:
12                return None
13
14            mid = (left + right) // 2
15            # create the rootnode
16            root = TreeNode(nums[mid])
17
18            # recursive calls to the helper function 
19            root.left = helper(left , mid - 1)
20            root.right = helper(mid + 1 , right)
21
22            return root
23        return helper(0 , len(nums) - 1)
24        
25        