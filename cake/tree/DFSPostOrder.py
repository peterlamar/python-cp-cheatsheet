import unittest
"""
     1
    / \
   2   3
  / \
 4   5
"""

#DFS PostOrder  4 5 2 3 1  (Left-Right-Root)
def is_balancedRecurive(tree_root):
    def postorder(node):
        if node is None:
            return
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=' ')

    postorder(tree_root)
    return True


def postOrderHack(tree_root):
  res, stack = [], [tree_root]
  while stack:
    node = stack.pop()
    if node:
      res.append(node.value)
      stack.append(node.left)
      stack.append(node.right)
  print(res[::-1])
  return True

#DFS PostOrder  4 5 2 3 1  (Left-Right-Root)
def postOrder(tree_root):
  stack = [(tree_root, False)]
  while stack:
    node, visited = stack.pop()
    if node:
      if visited:
        print(node.value, end=' ')
      else:
        stack.append((node, True))
        stack.append((node.right, False))
        stack.append((node.left, False))

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
        result = postOrder(tree)
        self.assertTrue(result)

unittest.main(verbosity=2)