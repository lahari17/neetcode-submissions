"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        curr = head
        while curr:
            copied_node = Node(curr.val)
            copied_node.next  = curr.next
            curr.next = copied_node
            curr = copied_node.next

        curr = head
        while curr:
            copied_node = curr.next
            if curr.random is not None:
                copied_node.random = curr.random.next

            curr = copied_node.next

        copy_head = head.next
        curr = head
        while curr:
            copied_node = curr.next
            next_original = copied_node.next

            curr.next = next_original
            if next_original is not None:
                copied_node.next = next_original.next
            else:
                copied_node.next = None

            curr = next_original
        return copy_head
        