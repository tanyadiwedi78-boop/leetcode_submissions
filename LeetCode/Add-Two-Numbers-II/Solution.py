class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def convertToNum(head):
            n = 0
            while head:
                n = n * 10 + head.val
                head = head.next
            return n

        n1 = convertToNum(l1)
        n2 = convertToNum(l2)
        total = n1 + n2
        result = None
        while total or not result: # to handle total = 0
            total, digit = divmod(total, 10)
            node = ListNode(digit)
            node.next = result
            result = node
        return result