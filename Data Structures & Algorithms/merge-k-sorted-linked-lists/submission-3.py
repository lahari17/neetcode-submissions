# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []

        for i, head in enumerate(lists):
            if head is not None:
                heapq.heappush(min_heap, (head.val, i, head))
        dummy = ListNode()
        tail = dummy

        while min_heap:
            value, i, node = heapq.heappop(min_heap)

            next_node = node.next

            if next_node is not None:
                heapq.heappush(min_heap, (next_node.val, i, next_node))

            tail.next = node
            tail = node
            tail.next = None

        return dummy.next 