1# Definition for singly-linked list.
2class ListNode:
3         def __init__(self, val=0, next=None):
4            self.val = val
5            self.next = next
6class Solution:
7    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode(0)
9        dummy.next = head
10        prev = dummy
11        while prev.next and prev.next.next:
12            first = prev.next
13            second = first.next
14
15            #swap
16            prev.next = second
17            first.next = second.next
18            second.next = first
19            # Move to the next pair
20            prev = first
21        return dummy.next
22
23        # dummy -> 1 -> 2 -> 3 -> 4
24
25        