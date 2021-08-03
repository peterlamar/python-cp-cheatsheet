# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # get midpoint
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
            
        # reverse 2nd half
        prev, node = None, slow 
        while node:
            node.next, prev, node = prev, node, node.next 
        
        # compare
        mid = prev
        start = head
        while start and mid:
            if start.val != mid.val:
                return False
            start = start.next 
            mid = mid.next 
        
        return True