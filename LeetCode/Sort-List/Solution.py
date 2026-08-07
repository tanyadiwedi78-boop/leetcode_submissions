1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        # approach -> merge sort
9        if not head or not head.next:
10            return head
11        # Find middle
12        slow = head
13        fast = head.next
14        while fast and fast.next:
15            slow = slow.next
16            fast = fast.next.next
17        mid = slow.next
18        slow.next = None
19
20        # sort both halves
21        left = self.sortList(head)
22        right = self.sortList(mid)
23
24        # merge
25        return self.merge(left , right)
26
27    def merge(self , l1 , l2):
28        dummy = ListNode(0)
29        tail = dummy
30
31        while l1 and l2:
32            if l1.val < l2.val:
33                tail.next = l1
34                l1 = l1.next
35            else:
36                tail.next = l2
37                l2 = l2.next
38            tail = tail.next
39        tail.next = l1 if l1 else l2
40        return dummy.next
41
42
43
44
45        