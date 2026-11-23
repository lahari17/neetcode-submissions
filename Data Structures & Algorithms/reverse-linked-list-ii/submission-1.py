# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        nodes[left - 1:right] = nodes[left - 1:right][::-1]

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        nodes[-1].next = None

        return nodes[0]


