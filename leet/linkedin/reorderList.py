# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1->2->3->4->5->6, 

# Split middle
1->2->3 4->5->6, 

# Reorder Right
1->2->3 6->5->4,

# Weave two lists
1->6->2->5->3->4
"""
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            
            curr.next = prev
            prev = curr
            curr = tmp
            
        first, second = head, prev
        tmp = None
        
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp
            
            tmp = second.next
            second.next = first
            second = tmp