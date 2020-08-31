[Language Mechanics](#language-mechanics)

1. [Loops](#loops)
1. [Strings](#strings)
1. [Sort](#sort)
1. [Hash](#hash)
1. [Set](#set)
1. [List](#list)
1. [Deque](#deque)
1. [Binary Tree](#binarytree)
1. [heapq](#heapq)
1. [Search](#search)
1. [Random](#random)
1. [Constants](#Constants)

[Algorithms](#algorithms)

1. [Binary Search](#binary-search)
1. [Sliding Window](#sliding-window)
1. [Dynamic Programming](#dynamic-programming)
1. [Cyclic Search](#cyclic-search)
1. [Linked List](#linked-list)
1. [Greedy])(#greedy)

[Algorithm Tips](#algo-tips)

# Language Mechanics

## Loops

Go through all elements
```python
i = 0
while i < len(str):
  i += 1
```

equivalent
```python
for i in range(len(message)):
  print(i)
```

Get largest number index from right
```python
while i > 0 and nums [i-1] >= nums[i]:
  i -= 1
```

Manually reversing
```python
l, r = i, len(nums) - 1
while l < r:
  nums[l], nums[r] = nums[r], nums[l]
  l += 1
  r -= 1
```

Go past the loop if we are clever with our boundry
```python
for i in range(len(message) + 1):
  if i == len(message) or message[i] == ' ':
```

Fun with Ranges
```python
for a in range(0,3): # 0,1,2
for a in reversed(range(0,3)) # 2,1,0
for i in range(len(A)//2): # A = [0,1,2,3,4,5]
  print(i) # 0,1,2 
  print(A[i]) # 0,1,2
  print(~i) # -1,-2,-3
  print(A[~i]) # 5,4,3
```

## Strings

Reverse works with built in split, [::-1] and " ".join()
```python
# s = "the sky  is blue"
def reverseWords(self, s: str) -> str:  
  wordsWithoutWhitespace = s.split() # ['the', 'sky', 'is', 'blue']
  reversedWords = wordsWithoutWhitespace[::-1] # ['blue', 'is', 'sky', 'the']        
  final = " ".join(reversedWords) # blue is sky the
```

Manual split based on isalpha()
```python
def splitWords(input_string) -> list: 
  words = [] # 
  start = length = 0
  for i, c in enumerate(input_string):
    if c.isalpha():
      if length == 0:
        start = i                    
        length += 1
      else:
        words.append(input_string[start:start+length])
        length = 0
  if length > 0:
    words.append(input_string[start:start+length])
  return words
```

Test type of char
```python
def rotationalCipher(input, rotation_factor):
  rtn = []
  for c in input:
    if c.isupper():
      ci = ord(c) - ord('A')
      ci = (ci + rotation_factor) % 26
      rtn.append(chr(ord('A') + ci))
    elif c.islower():
      ci = ord(c) - ord('a')
      ci = (ci + rotation_factor) % 26
      rtn.append(chr(ord('a') + ci))
    elif c.isnumeric():
      ci = ord(c) - ord('0')
      ci = (ci + rotation_factor) % 10
      rtn.append(chr(ord('0') + ci))
    else:
      rtn.append(c)
  return "".join(rtn)  
```

AlphaNumberic
```python
isalnum()
```

Get charactor index
```python
print(ord('A')) # 65
print(ord('B')-ord('A')+1) # 2
print(chr(ord('a') + 2)) # c
```

## Sort

```python
  def merge_sorted_lists(arr1, arr2): # built in sorted does Timsort optimized for subsection sorted lists
    return sorted(arr1 + arr2)
```

## Hash

```python
for c in s1: # Adds counter for c
  ht[c] = ht.get(c, 0) + 1 # ht[a] = 1, ht[a]=2, etc
```

## Set

```python
st = set()
st.add(a) # Add to st
st.remove(a) # Remove from st
```

## List

```python
test = [0] * 100 # initialize list with 100 0's
```

## Deque

```python
>>> from collections import deque
>>> deq = deque([1, 2, 3])
>>> deq.appendleft(5)
>>> deq.append(6)
>>> deq
deque([5, 1, 2, 3, 6])
>>> deq.popleft()
5
>>> deq.pop()
6
>>> deq
deque([1, 2, 3])
```
## BinaryTree

Pre, In Order, and Post order Traversal
```python
def preorder_print(self, start, traversal):
  """Root->Left->Right"""
  if start:
    traversal += (str(start.value) + "-") # Pre Order
    traversal = self.preorder_print(start.left, traversal)
    traversal = self.preorder_print(start.right, traversal)
  return traversal
```

## Heapq

[Priority Queue](https://realpython.com/python-heapq-module/#data-structures-heaps-and-priority-queues) 
1. Implemented as complete binary tree, which has all levels as full excepted deepest
1. In a heap tree the node is smaller than its children

```python
def maximumProduct(self, nums: List[int]) -> int:
  l = heapq.nlargest(3, nums)
  s = heapq.nsmallest(3, nums)
  return max(l[0]*l[1]*l[2],s[0]*s[1]*l[0])
```
## Search

[Binary Search Tree](https://en.wikipedia.org/wiki/Binary_search_tree) - left node is smaller than value of its parent

## Random

```Python
for i, l in enumerate(shuffle):
  r = random.randrange(0+i, len(shuffle))
  shuffle[i], shuffle[r] = shuffle[r], shuffle[i]
return shuffle
```

## Constants

```Python
max = float('-inf')
min = float('inf')
```

# Algorithms

## Binary Search

```python
class Solution:
"""
12345678 
FFTTTTTT
"""
def mySqrt(self, x: int) -> int:
  def condition(value, x) -> bool:
    return value * value > x

  if x == 1:
    return 1

  left, right = 1, x
  while left < right:
    mid = left + (right-left) // 2
    if condition(mid, x):
      right = mid
    else:
      left = mid + 1

  return left - 1
```
[binary search](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)

## Sliding Window

1. Have a counter or hash-map to count specific array input and keep on increasing the window toward right using outer loop.
1. Have a while loop inside to reduce the window side by sliding toward right. Movement will be based on constraints of problem.
1. Store the current maximum window size or minimum window size or number of windows based on problem requirement.

### Typical Problem Clues:
1. Get min/max/number of satisfied sub arrays
1. Return length of the subarray with max sum/product
1. Return max/min length/number of subarrays whose sum/product equals K

Can require [2 or 3 pointers to solve](https://medium.com/algorithms-and-leetcode/magic-solution-to-leetcode-problems-sliding-window-algorithm-891e3d60bf89)

```python
def fruits_into_baskets(fruits):
  maxCount, j = 0, 0
  ht = {}

  for i, c in enumerate(fruits):
    if c in ht:
      ht[c] += 1
    else:
      ht[c] = 1

    if len(ht) <= 2:
      maxCount = max(maxCount, i-j+1)
    else:
      jc = fruits[j]
      ht[jc] -= 1
      if ht[jc] <= 0:
        del ht[jc]
      j += 1  

  return maxCount
```

1. [sliding window template](https://leetcode.com/discuss/general-discussion/657507/Sliding-Window-for-Beginners-Problems-or-Template-or-Sample-Solutions)
1. [sliding window example](https://leetcode.com/problems/fruit-into-baskets/discuss/170740/JavaC%2B%2BPython-Sliding-Window-for-K-Elements)

## Dynamic Programming

[dynamic programming](https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns)
[dp notes](https://leetcode.com/discuss/general-discussion/475924/my-experience-and-notes-for-learning-dp)

[facebook interviewquestions](https://leetcode.com/discuss/interview-question/675445/facebook-interview-experiences-all-combined-from-lc-till-date-07-jun-2020)

## Cyclic Search

1. Useful algo when sorting in place

```python
# if my number is equal to my index, i+1 
# if my number is equal to this other number, i+1 (dups)
# else swap
def cyclic_sort(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  
    else:
      i += 1
  return nums
```

## Linked List

1. Lots of linked list operations require 3 pointers (reverse/merge)

Reverse:
```python
def reverseLinkedList(head):
	prev, node  = None, head
    while node:
		node.next, prev, node = prev, node, node.next
	return prev
```

Reversing is easier if you can modify the values of the list
```python
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
```
Merge:
```python
def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
	p2 = headTwo
	prev = None
	
	while p1 and p2:
		if p1.value < p2.value:
			prev = p1
			p1 = p1.next
		else:
			if prev:
				prev.next = p2
			prev = p2
			p2 = p2.next
			prev.next = p1
	
	if p1 is None:
		prev.next = p2
	
	return headOne if headOne.value < headTwo.value else headTwo
```

## Greedy

Greedy algorithm chooses the option that looks best at every step and solves by keeping the best answer so far. I.e. giving change by giving the largest coin possible at every step. Look to solve choices incrementally until optimal solution.

1. Divide problem into subproblems, including one small problem and the remaining subproblem
2. Determine the optimal substructure of the problems (formulating a recurrance function)
3. Show if we make the greedy choice, then only one subproblem remains

### Typical Problem Clues:
Greedy/Dynamic Programming [hints](https://medium.com/algorithms-and-leetcode/greedy-algorithm-explained-using-leetcode-problems-80d6fee071c4):
1. True/False
1. Max/Min numer

## Algo tips

Store knowledge in the data structure by sorting it. For example, merging [meeting times](https://www.interviewcake.com/question/python/merging-ranges?course=fc1&section=array-and-string-manipulation) by sorting and merging

```
[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
```

into

```
[(0, 1), (3, 8), (9, 12)]
```
