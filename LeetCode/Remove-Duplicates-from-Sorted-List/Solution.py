1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        curr = head
9        while curr and curr.next:
10            if curr.val == curr.next.val:
11                curr.next = curr.next.next
12            else:
13                curr = curr.next
14        return head
15        