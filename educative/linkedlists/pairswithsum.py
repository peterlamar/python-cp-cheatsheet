  """
  Go through with hash table,
  Once pair is found, append to return list

  sum_val = 5
  12345

  [4]=0
  [3]=1
  

  """
  
  def pairs_with_sum(self, sum_val):  

    node = self.head

    ht = {}
    idx = 0
    rtnLst = []

    if node is None:
      return rtnLst

    while node:
      if node.data not in ht:
        ht[sum_val - node.data] = idx
      else:
        rtnLst.insert(0, "(" + str(sum_val - node.data) + "," + str(node.data) + ")")
      idx += 1
      node = node.next
    
    return rtnLst