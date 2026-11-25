# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        tail = dummy

        p1 = l1
        p2 = l2
        carry = 0
        
        while p1 or p2 or carry:
            digit1 = p1.val if p1 else 0
            digit2 = p2.val if p2 else 0

            total = digit1 + digit2 + carry

            digit = total%10
            carry = total//10
            tail.next = ListNode(digit)
            tail = tail.next

            if p1:
                p1 = p1.next

            if p2:
                p2 = p2.next

        return dummy.next
        