import unittest
from collections import deque

#BFS levelOrder 1 2 3 4 5 
def levelOrder(tree_root):
  queue = deque([tree_root])
  while queue:
    node = queue.popleft()
    if node:
        print(node.value, end=' ')
        queue.append(node.left)
        queue.append(node.right)

def levelOrderStack(tree_root):
    stk = [(tree_root, 0)]
    rtn = []
    while stk:
        node, depth = stk.pop()
        if node:
            if len(rtn) < depth + 1:
                rtn.append([])
            rtn[depth].append(node.value)            
            stk.append((node.right, depth+1))
            stk.append((node.left, depth+1))
    print(rtn)
    return True     

def levelOrderStackRec(tree_root):
    rtn = []
        
    def helper(node, depth):
        if len(rtn) == depth:
            rtn.append([])
        rtn[depth].append(node.value)
        if node.left:
            helper(node.left, depth + 1)
        if node.right:
            helper(node.right, depth + 1)
            
    helper(tree_root, 0)
    print(rtn)
    return rtn










# Tests

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_traversal(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(2)
        tree.insert_right(3)
        left.insert_left(4)
        left.insert_right(5)
        result = levelOrderStackRec(tree)
        self.assertTrue(result)

unittest.main(verbosity=2)