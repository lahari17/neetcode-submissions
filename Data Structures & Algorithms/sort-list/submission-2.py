# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length +=1
            curr = curr.next

        dummy = ListNode(0, head)
        size = 1

        while size<length:
            curr = dummy.next
            tail = dummy

            while curr:

                left = curr

                right = self.split(left, size)

                curr = self.split(right, size)

                merged_head, merged_tail = self.merge(left, right)

                tail.next = merged_head
                tail = merged_tail

            size = size*2

        return dummy.next

        



    def split(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        if not head:
            return None

        curr = head

        for _ in range(size-1):
            if curr.next is None:
                break
            
            curr = curr.next

        next_head = curr.next
        curr.next = None

        return next_head

    def merge(self, a:Optional[ListNode], b:Optional[ListNode])-> tuple[[Optional][ListNode], Optional[ListNode]]:
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

        while tail.next:
            tail = tail.next

        return dummy.next, tail
            


        