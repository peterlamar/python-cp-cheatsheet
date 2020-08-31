import unittest



#DFS InOrder 4 2 5 1 3 (Left-Root-Right)
def inOrder(tree_root):
  current = tree_root  
  stack = [] 
  while True: 
    if current: 
      stack.append(current) 
      current = current.left  
    elif(stack): 
      current = stack.pop() 
      print(current.value, end=" ") 
      current = current.right  
    else: 
      break
  return True 

















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
        result = inOrder(tree)
        self.assertTrue(result)

unittest.main(verbosity=2)