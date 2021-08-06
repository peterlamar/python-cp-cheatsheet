# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
 5
 5
 
 
"""
class Solution:

        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode(-1)
        carry = 0
        
        while l1 or l2 or carry:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            total = d1 + d2 + carry
            newNode = ListNode(total%10)
            carry = total // 10
            node.next = newNode
            node = node.next 
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next
        
        return head.next 

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = n = ListNode(0)
        carry = 0
        sum = 0
        # loop through, add num and track carry
        # while both pointers valid
        while l1 or l2 or carry > 0:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            n.next = ListNode((sum+carry) % 10)
            n = n.next
            carry = (sum+carry) // 10
            sum = 0
          
        return root.next
