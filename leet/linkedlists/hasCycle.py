# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
time: O(n), worst O(n) + K
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        try:
            slow = head
            fast = head.next
            while slow != fast:
                slow = slow.next 
                fast = fast.next.next
            return True
        except:
            return False

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return
        slow = head
        fast = head.next      
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next 
            fast = fast.next.next
        return True