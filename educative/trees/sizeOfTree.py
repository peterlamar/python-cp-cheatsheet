    def size_(self, node):
      if node is None:
        return 0
      return 1 + self.size_(node.left) + self.size_(node.right)


    def size_(self, node):

      if node is None:
        return 0

      size = 1
      stk = []
      myNode = node
      stk.append(myNode)

      while stk:
        myNode = stk.pop()
        if myNode.left:
            size += 1
            stk.append(myNode.left)
        if myNode.right:
            size += 1
            stk.append(myNode.right)

      return size