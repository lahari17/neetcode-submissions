# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        curr = head 

        while curr:
            values.append(curr.val)
            curr = curr.next

        values.sort()

        dummy = ListNode(0)
        prev = dummy
        for i in range(len(values)):
            curr_node = ListNode(values[i])
            prev.next = curr_node
            prev = curr_node

        return dummy.next
        