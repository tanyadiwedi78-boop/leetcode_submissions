1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
8        # make two separate list and then combine in one one list
9        small_dummy = ListNode(0)
10        large_dummy = ListNode(0)
11        small = small_dummy
12        large = large_dummy
13        
14        curr = head
15        while curr:
16            if curr.val < x:
17                small.next = curr
18                small = small.next
19
20            else:
21                large.next = curr
22                large = large.next
23            
24            curr = curr.next
25            # connect small list with large list
26        small.next = large_dummy.next
27        large.next = None
28        return small_dummy.next
29
30
31        