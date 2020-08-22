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

"""
# time: 14 M
Error: ommitted subNode = node 

"""
def reverse_sub_list(head, p, q):
  node = head

  OrigPrev = None 
  while node and node.value != p:
    OrigPrev = node 
    node = node.next

  subListHead = node 
  subNode = node 

  prev = None
  while subNode and subNode.value != q:
    subNode.next, prev, subNode = prev, subNode, subNode.next 

  OrigPrev.next = subNode # 1->4 
  subListHead.next = subNode.next # 2->5
  subNode.next = prev # 3->4
  
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
