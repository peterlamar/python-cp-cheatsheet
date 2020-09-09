# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        def getNextNode(node):               
            if node:
                if node.val != val:
                    return node
                else:
                    return getNextNode(node.next)
            else:
                return None
            
        node = newHead = getNextNode(head)
        
        while node:
            if node.next and node.next.val == val:
                node.next = getNextNode(node.next)
                   
            node = node.next
        
        return newHead

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        curr = head
        prev = dummy
        while curr:
            if curr.val == val:
                prev.next = curr.next 
            else:
                prev = curr
            
            curr = curr.next
                
        
        return dummy.next