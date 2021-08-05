"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        newNode = Node(insertVal)
        
        if not head:
            newNode.next = newNode
            return newNode
        
        prev = head
        node = head.next
        
        while node:
            if prev.val > node.val and (insertVal < node.val or insertVal > prev.val):
                break
            
            if prev.val <= insertVal <= node.val:
                break
            
            if node == head:
                break
            
            prev = node
            node = node.next 
            
        prev.next = newNode
        newNode.next = node
        
        return head

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        insertNode = Node(insertVal)
        
        if head is None:
            insertNode.next = insertNode
            return insertNode
        
        node = head
        
        while node:
            if node.next.val < node.val and (insertVal <= node.next.val or insertVal > node.val):
                break
            
            if node.val <= insertVal <= node.next.val:
                break
            
            elif node.next == head:
                break
            
            node = node.next 

        insertNode.next = node.next
        node.next = insertNode
        
        return head