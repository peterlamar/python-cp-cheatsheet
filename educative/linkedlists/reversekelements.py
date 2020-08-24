from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()

def reverse_every_k_elements(head, k):
  def reverseK(subhead, cnt):
      i = 0
      prev = None
      node = subhead
      while node and i < cnt:
        node.next, prev, node = prev, node, node.next 
        i += 1
      return (prev, node)
      
  node = head 
  pp = None 
  sl = None 
  newHead = None
  tmp = None

  while node:    
    pp = tmp
    sl = node 

    prev, node = reverseK(node, k)

    if newHead is None:
      newHead = prev

    if pp:
      pp.next = prev

    sl.next = node 
    tmp = sl # Dummy temp is key

  return newHead


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()