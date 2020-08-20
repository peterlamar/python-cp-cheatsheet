  def remove_duplicates(self):
    ht = {}
    myNode = self.head 

    if myNode is None:
      return

    while myNode: 
      tmp = myNode.next
      if myNode.data not in ht:
        ht[myNode.data] = True
      else:
        self.delete_node(myNode)
      myNode = tmp
  
  def delete_node(self, node):
    cur = self.head
    while cur:
      if cur == node and cur == self.head:
        # Case 1:
        if not cur.next:
          cur = None 
          self.head = None
          return

        # Case 2:
        else:
          nxt = cur.next
          cur.next = None 
          nxt.prev = None
          cur = None
          self.head = nxt
          return 

      elif cur == node:
        # Case 3:
        if cur.next:
          nxt = cur.next 
          prev = cur.prev
          prev.next = nxt
          nxt.prev = prev
          cur.next = None 
          cur.prev = None
          cur = None
          return

        # Case 4:
        else:
          prev = cur.prev 
          prev.next = None 
          cur.prev = None 
          cur = None 
          return 
      cur = cur.next