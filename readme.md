# Algorithms

1. [Binary Search](#binary-search)
1. [Sliding Window](#sliding-window)
1. [Dynamic Programming](#dynamic-programming)
1. [Cyclic Search](#cyclic-search)
1. [Linked List](#linked-list)



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
