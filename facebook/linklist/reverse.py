import math
# Add any extra import statements you may need here


class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

# Add any helper functions you may need here
"""
Go in and reverse k elements

Time: 15+

Error:
missed oddHead, connecting edge cases


"""

"""
def reverse(head):
  # Write your code here
  def reverseKElements(myHead, k):
    node, prev = myHead, None
    count = 0
    while node and count < k:
      node.next, prev, node = prev, node, node.next
      count += 1
    return (prev, node)
  
  node = head
  evenHead = None
  evenTail = None
  oddHead = None
  newHead = None
  evenCount = 0
  while node:
    if node.data%2 == 0 and evenCount == 0:
      evenHead = node
      evenCount += 1
    elif node.data%2 == 0:
      evenCount += 1
      evenTail = node
    elif node.data %2 == 1 and evenCount > 0:
      prev, curr = reverseKElements(evenHead, evenCount)
      if oddHead:
        oddHead.next = evenTail
        newHead = oddHead
      else:
        newHead = prev
      evenHead.next = curr
      oddHead = curr
      evenHead = None
      evenTail = None
      evenCount = 0
    elif node.data % 2 == 1 and evenCount == 0:
      oddHead = node
    
    node = node.next
  
  if evenCount > 0:
    prev, curr = reverseKElements(evenHead, evenCount)
    oddHead.next = evenTail
  
  return newHead

"""

"""
5 min
no errors
"""
def reverse(head):
  node = head
  stk = []
  while node:
    if node.data % 2 == 0:
      stk.append(node)
    if node.data % 2 == 1 or node.next is None:
      while len(stk) > 1:
        stk[-1].data, stk[0].data = stk[0].data, stk[-1].data
        stk.pop(0)
        stk.pop(-1)
      stk.clear()
    node = node.next
  return head

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printLinkedList(head):
  print('[', end='')
  while head != None:
    print(head.data, end='')
    head = head.next
    if head != None:
      print(' ', end='')
  print(']', end='')

test_case_number = 1

def check(expectedHead, outputHead):
  global test_case_number
  tempExpectedHead = expectedHead
  tempOutputHead = outputHead
  result = True
  while expectedHead != None and outputHead != None:
    result &= (expectedHead.data == outputHead.data)
    expectedHead = expectedHead.next
    outputHead = outputHead.next

  if not(outputHead == None and expectedHead == None):
    result = False

  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printLinkedList(tempExpectedHead)
    print(' Your output: ', end='')
    printLinkedList(tempOutputHead)
    print()
  test_case_number += 1

def createLinkedList(arr):
  head = None
  tempHead = head
  for v in arr:
    if head == None:
      head = Node(v)
      tempHead = head
    else:
      head.next = Node(v)
      head = head.next
  return tempHead

if __name__ == "__main__":
  head_1 = createLinkedList([1, 2, 4, 6, 8, 9, 12, 16])
  expected_1 = createLinkedList([1, 8, 6, 4, 2, 9, 16, 12])
  output_1 = reverse(head_1)
  check(expected_1, output_1)
  
  head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
  expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6])
  output_2 = reverse(head_2)
  check(expected_2, output_2)
  
  # Add your own test cases here
  