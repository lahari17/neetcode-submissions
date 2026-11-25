# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currl1 = l1
        num1 = 0
        prev1 = None
        while currl1:
            # if currl1.next is not None:
                next_node = currl1.next
                currl1.next = prev1
                prev1 = currl1
                currl1 = next_node
        currl1= prev1
        while currl1:
            num1 = num1* 10 + currl1.val
            currl1 = currl1.next

        currl2 = l2
        num2 = 0
        prev2 = None
        while currl2:
            # if currl2.next is not None:
                next_node = currl2.next
                currl2.next = prev2
                prev2 = currl2
                currl2 = next_node
        currl2= prev2
        while currl2:
            num2 = num2* 10 + currl2.val
            currl2 = currl2.next

        sum = num1 + num2
        if sum==0:
            return ListNode(0)
        nodes=[]
        while sum:
            nodes.append(ListNode(sum%10))
            sum = sum//10
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        return nodes[0]
        
