"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
"""
time: O(n)
space: O(2k)
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque([(root, 0)])
        prev = None
        head = root
        cnt = 0
        
        while queue:    
            node, d = queue.pop()
            if node:
                if cnt == d: # first in new level
                    cnt += 1
                else:
                    node.next = prev
                prev = node

                queue.appendleft((node.right,d+1))
                queue.appendleft((node.left, d+1))
                
        
        return head


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root is None:
            return
        
        leftmost = head = root
        
        while leftmost.left:
            
            node = leftmost
            while node:
                node.left.next = node.right 
                if node.next:
                    node.right.next = node.next.left

                node = node.next 
        
            leftmost = leftmost.left 
        
        return head