import unittest
"""
     1
    / \
   2   3
  / \
 4   5
"""

#DFS PreOrder  1 2 4 5 3 (Root-Left-Right)
def preOrder(tree_root):
  nodes = [tree_root]
  while nodes:
    node = nodes.pop()
    print(node.value, end=" ")
    if node.left: 
      nodes.append(node.left)
    if node.right: 
      nodes.append(node.right)
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
        result = preOrder(tree)
        self.assertTrue(result)

unittest.main(verbosity=2)