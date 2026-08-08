1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        # problem is where is the cycle starts = return 2
10        slow = head
11        fast = head
12        while fast and fast.next:
13            slow = slow.next
14            fast = fast.next.next
15
16            if slow == fast:
17                break
18        else:
19            return None
20
21        # find starting point
22        slow = head
23        while slow != fast:
24            slow = slow.next
25
26            fast = fast.next
27        return slow
28
29        # approach name - > Floyd's Tortoise and Hare algorithm