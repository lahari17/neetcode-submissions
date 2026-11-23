# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes  = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        for i in range(0, len(nodes)-1- (k-2), k):
            nodes[i:i+k] = nodes[i:i+k][::-1]

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        if nodes:
            nodes[-1].next = None
            return nodes[0]    

        return None    