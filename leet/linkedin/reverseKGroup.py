# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseK(head, k):
            i = 0
            prev, node = None, head
            while node and i < k:
                node.next, prev, node = prev, node, node.next
                i += 1
            return (prev, node)

        newHead = None
        kt = None
        ptr = head
        prev = None
        
        while ptr:
            
            ptr = head
            cnt = k
            while ptr and cnt > 0:
                ptr = ptr.next
                cnt -= 1
            
            if cnt == 0:
                prev, node = reverseK(head, k)
            
                if newHead is None:
                    newHead = prev

                if kt:
                    kt.next = prev

                kt = head
                head = ptr
                    
        if kt:
            kt.next = head    
            
        return newHead if newHead else head
            