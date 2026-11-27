# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        left = head

        left = self.sortList(left)
        right = self.sortList(right)

        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, a:Optional[ListNode], b:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next

            tail = tail.next

        tail.next = a if a else b

        return dummy.next
    

                

        