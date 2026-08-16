1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head or not head.next:
9            return head
10        odd = head
11        even = head.next
12        even_head = even
13        while even and even.next:
14            odd.next = even.next
15            odd = odd.next
16
17            even.next = odd.next
18            even = even.next
19        odd.next = even_head
20        return head
21
22        # not even odd val its about positions
23
24
25
26
27        