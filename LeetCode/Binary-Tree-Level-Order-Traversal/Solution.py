1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
9        # base case 
10        if not root:
11            return []
12
13
14        result = []
15        queue = deque([root]) # initialize the queue with the right root
16    
17
18        while queue:
19            level_size = len(queue)
20            current_level = []
21
22            for _ in range(level_size):
23                node = queue.popleft()
24                current_level.append(node.val)
25
26                if node.left: # push the left child if it exists
27                    queue.append(node.left)
28
29                if node.right:
30                    queue.append(node.right)
31
32                # append the complete leval to the final result
33            result.append(current_level)
34
35        return result