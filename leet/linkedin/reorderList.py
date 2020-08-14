# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
BF
loop through to end
ptr at beginning point to end
end point to next

head
tail

Handle Tail Edge case

tmp = frontNode.next
frontNode.next = backNode
backNode.next = tmp

d[2] = 1
d[3] = 2
d[4] = 3
d[5] = 4

1->2->3->4->5

1->5->2->4->3

frontNode 2
backNode 4

1->2->3->4->5
f           t

1->5->2->3->4
   f        t

1->5->2->3->4
      f     t
      
      
      
"""
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = frontNode = tailNode = head
        hm = {}
        
        if not head:
            return
        
        # Get tail node and fill hm
        while node:
            print(node.val)
            if not node.next:
                tailNode = node
                break                
            else: 
                hm[node.next] = node
            node = node.next
        
        while frontNode.next and (frontNode.next).next:
        
            # point new tail to null
            newTail = hm[tailNode]
            newTail.next = None             
            # Start swapping
            tmp = frontNode.next
            frontNode.next = tailNode
            tailNode.next = tmp   

            tailNode = newTail

            if frontNode.next:
                frontNode = frontNode.next
                if frontNode.next:
                    frontNode = frontNode.next
            
            
        
        
        