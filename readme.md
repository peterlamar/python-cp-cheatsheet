[Language Mechanics](#language-mechanics)

1. [Loops](#loops)
1. [Strings](#strings)
1. [Tuples](#tuples)
1. [Sort](#sort)
1. [Hash](#hash)
1. [Set](#set)
1. [List](#list)
1. [Dict](#dict)
1. [Binary Tree](#binarytree)
1. [heapq](#heapq)
1. [lambda](#lambda)
1. [zip](#zip)
1. [Random](#random)
1. [Constants](#constants)
1. [Ternary Condition](#ternary)
1. [Bitwise operators](#bitwise)
1. [For Else](#for-else)
1. [Modulo](#modulo)
1. [any](#any)
1. [all](#all)
1. [bisect](#bisect)
1. [iter](#iter)
1. [map](#map)
1. [filter](#filter)
1. [reduce](#reduce)
1. [regular expression](#regular-expression)

[Collections](#collections)
1. [Deque](#deque)
1. [Counter](#counter)
1. [Default Dict](#default-dict)

[Algorithms](#algorithms)

1. [Binary Search](#binary-search)
1. [Topological Search](#topological-search)
1. [Sliding Window](#sliding-window)
1. [Anagrams](#anagrams)
1. [Dynamic Programming](#dynamic-programming)
1. [Cyclic Sort](#cyclic-sort)
1. [Quick Sort](#quick-sort)
1. [Merge Sort](#merge-sort)
1. [Linked List](#linked-list)
1. [Greedy](#greedy)
1. [Convert Base](#convert-base)
1. [Parenthesis](#parenthesis)
1. [Max Profit Stock](#max-profit-stock)
1. [Shift Array Right](#shift-array-right)
1. [Subarray Sum](#subarray-sum)
1. [Events](#Events)
1. [Merge Meetings](#merge-meetings)
1. [Trie](#Trie)
1. [Kadane's Algorithm - Max subarray sum](#kadane)
1. [Union Find/DSU](#union-find)
1. [Fast Power](#fast-power)
1. [Fibonacci Golden](#fibonacci-golden)

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

Replace characters or strings
```python
def isValid(self, s: str) -> bool:
  while '[]' in s or '()' in s or '{}' in s:
    s = s.replace('[]','').replace('()','').replace('{}','')
  return len(s) == 0
```

Insert values in strings
```python
txt3 = "My name is {}, I'm {}".format("John",36) # My name is John, I'm 36
```

Multiply strings/lists with *, even booleans which map to True(1) and False(0)
```python
'meh' * 2 # mehmeh
['meh'] * 2 # ['meh', 'meh']
['meh'] * True #['meh']
['meh'] * False #[]
```

Find substring in string
```python
txt = "Hello, welcome to my world."
x = txt.find("welcome")  # 7
```

## Tuple

Collection that is ordered and unchangable

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # banana
```

Can be used with Dicts

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    d = defaultdict(list)
    for w in strs:
        key = tuple(sorted(w))
        d[key].append(w)
    return d.values()
```

## Sort

Sort sorts alphabectically
```python
cars = ['Ford', 'BMW', 'Volvo']
cars.sort() # returns None type
print(cars) # ['BMW', 'Ford', 'Volvo']
cars.sort(key=lambda x: len(x) )
print(cars) # ['VW', 'BMW', 'Ford', 'Mitsubishi']
```

```python
print(sorted(['Ford', 'BMW', 'Volvo'])) # ['BMW', 'Ford', 'Volvo']
```


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

```python
s = set('abc') # {'c', 'a', 'b'}
s |= set('cdf') # {'f', 'a', 'b', 'd', 'c'} set s with elements from new set
s &= set('bd') # {'d', 'b'} only elements from new set
s -= set('b') # {'d'} remove elements from new set
s ^= set('abd') # {'a', 'b'} elements from s or new but not both
```

## List

Stacks are implemented with Lists. Stacks are good for parsing and graph traversal

```python
test = [0] * 100 # initialize list with 100 0's
```

2D
```python
rtn.append([])
rtn[0].append(1) # [[1]]               
```

List Comprehension
```python
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Reverse a list
```python
ss = [1,2,3]
ss.reverse()
print(ss) #3,2,1
```

Join list
```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2 # ['a', 'b', 'c', 1, 2, 3]
```

## Dict

Hashtables are implemented with dictionaries

Dictionary keys can be iterated through
```python
def intToRoman(self, num: int) -> str:
    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50:'L', 40: 'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    res = ''
    for i in d:
        res += num//i*d[i] # num // key * referenced character
        num %= i
    return res
```

Dict can also be initiated with comprehension
```python
nodes = {'f', 'e', 'r', 'w', 't'}
degree = {x:0 for x in nodes} # {'f': 0, 'e': 0, 'r': 0, 'w': 0, 't': 0}
```

Default can be set dict[key]=default if key is not already in dict
```python
par = {}
par.setdefault(1,1) # returns 1, makes par = { 1 : 1 } 
```

## BinaryTree


DFS Pre, In Order, and Post order Traversal

- Preorder
  - encounters roots before leaves
  - Create copy
- Inorder
  - flatten tree back to original sequence
  - Get values in non-decreasing order in BST
- Post order
  - encounter leaves before roots
  - Helpful for deleting

Recursive
```python
"""
     1
    / \
   2   3
  / \
 4   5
"""
def postOrder(node):
  if node is None:
    return
  postorder(node.left)
  postorder(node.right)
  print(node.value, end=' ')
```

Iterative PreOrder
```python
# PreOrder  1 2 4 5 3 (Root-Left-Right)
def preOrder(tree_root):
  stack = [(tree_root, False)]
  while stack:
    node, visited = stack.pop()
    if node:
      if visited:
        print(node.value, end=' ')
      else:
        stack.append((node.right, False))
        stack.append((node.left, False))
        stack.append((node, True))
```

Iterative InOrder
```python
# InOrder   4 2 5 1 3 (Left-Root-Right)
def inOrder(tree_root):
  stack = [(tree_root, False)]
  while stack:
    node, visited = stack.pop()
    if node:
      if visited:
        print(node.value, end=' ')
      else:
        stack.append((node.right, False))
        stack.append((node, True))
        stack.append((node.left, False))
```

Iterative PostOrder
```python
# PostOrder 4 5 2 3 1  (Left-Right-Root)
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
```

Iterative BFS(LevelOrder)
```python
from collections import deque

#BFS levelOrder 1 2 3 4 5 
def levelOrder(tree_root):
  queue = deque([tree_root])
  while queue:
    node = queue.popleft()
    if node:
        print(node.value, end=' ')
        queue.append(node.left)
        queue.append(node.right)

def levelOrderStack(tree_root):
    stk = [(tree_root, 0)]
    rtn = []
    while stk:
        node, depth = stk.pop()
        if node:
            if len(rtn) < depth + 1:
                rtn.append([])
            rtn[depth].append(node.value)            
            stk.append((node.right, depth+1))
            stk.append((node.left, depth+1))
    print(rtn)
    return True     

def levelOrderStackRec(tree_root):
    rtn = []
        
    def helper(node, depth):
        if len(rtn) == depth:
            rtn.append([])
        rtn[depth].append(node.value)
        if node.left:
            helper(node.left, depth + 1)
        if node.right:
            helper(node.right, depth + 1)
            
    helper(tree_root, 0)
    print(rtn)
    return rtn
```

Traversing data types as a graph, for example BFS
```python
def removeInvalidParentheses(self, s: str) -> List[str]:
    rtn = []
    v = set()
    v.add(s)
    if len(s) == 0: return [""]
    while True:
        for n in v:
            if self.isValid(n):
                rtn.append(n)
        if len(rtn) > 0: break
        level = set()
        for n in v:
            for i, c in enumerate(n):
                if c == '(' or c == ')':
                    sub = n[0:i] + n[i + 1:len(n)]
                    level.add(sub)
        v = level
    return rtn
```

## Graph

Build an [adjecency graph](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs) from edges list
```python
# N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
graph = [[] for _ in range(N)]
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
# [[1, 2], [0], [0, 3, 4, 5], [2], [2], [2]]
```

Build adjecency graph from traditional tree
```python
adj = collections.defaultdict(list)
def dfs(node):
    if node.left:
        adj[node].append(node.left)
        adj[node.left].append(node)
        dfs(node.left)
    if node.right:
        adj[node].append(node.right)
        adj[node.right].append(node)
        dfs(node.right)
dfs(root)
```

Traverse Tree in graph notation
```python
# [[1, 2], [0], [0, 3, 4, 5], [2], [2], [2]]
def dfs(node, par=-1):
    for nei in graph[node]:
        if nei != par:
            res = dfs(nei, node)
dfs(0) # 1->2->3->4->5
```

## Heapq
```
      1
     / \
    2   3
   / \ / \
  5  6 8  7
```

[Priority Queue](https://realpython.com/python-heapq-module/#data-structures-heaps-and-priority-queues) 
1. Implemented as complete binary tree, which has all levels as full excepted deepest
1. In a heap tree the node is smaller than its children

```python
def maximumProduct(self, nums: List[int]) -> int:
  l = heapq.nlargest(3, nums)
  s = heapq.nsmallest(3, nums)
  return max(l[0]*l[1]*l[2],s[0]*s[1]*l[0])
```

Heap elements can be tuples, heappop() frees the smallest element (flip sign to pop largest)
```python
def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    heap = []
    for p in points:
        distance = sqrt(p[0]* p[0] + p[1]*p[1])
        heapq.heappush(heap,(-distance, p))
        if len(heap) > K:
            heapq.heappop(heap)            
    return ([h[1] for h in heap])
```

nsmallest can take a lambda argument
```python
def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:    
    return heapq.nsmallest(K, points, lambda x: x[0]*x[0] + x[1]*x[1])
```

The key can be a function as well in nsmallest/nlargest
```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    return heapq.nlargest(k, count, count.get)
```

Tuple sort, 1st/2nd element. increasing frequency then decreasing order
```python
def topKFrequent(self, words: List[str], k: int) -> List[str]:
    freq = Counter(words)
    return heapq.nsmallest(k, freq.keys(), lambda x:(-freq[x], x))
```

## Lambda

Can be used with (list).sort(), sorted(), min(), max(), (heapq).nlargest,nsmallest(), map()

```python
# a=3,b=8,target=10
min((b,a), key=lambda x: abs(target - x)) # 8
```

```python
>>> ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
>>> print(sorted(ids)) # Lexicographic sort
['id1', 'id100', 'id2', 'id22', 'id3', 'id30']
>>> sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # Integer sort
>>> print(sorted_ids)
['id1', 'id2', 'id3', 'id22', 'id30', 'id100']
```

```python
trans = lambda x: list(al[i] for i in x) # apple, a->0..
print(trans(words[0])) # [0, 15, 15, 11, 4]
```

Lambda can sort by 1st, 2nd element in tuple
```python
sorted([('abc', 121),('bbb',23),('abc', 148),('bbb', 24)], key=lambda x: (x[0],x[1]))
# [('abc', 121), ('abc', 148), ('bbb', 23), ('bbb', 24)]
```

## Zip

Combine two dicts or lists
```python
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
list(zip(s1, s2)) # [(1, 'a'), (2, 'c'), (3, 'b')]
```

Traverse in Parallel
```python
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
  print(f'Letter: {l}') # a,b,c
  print(f'Number: {n}') # 0,1,2
```

Empty in one list is ignored
```python
letters = ['a', 'b', 'c']
numbers = []
for l, n in zip(letters, numbers):
  print(f'Letter: {l}') #
  print(f'Number: {n}') #
```

Compare characters of alternating words
```python
for a, b in zip(words, words[1:]):
    for c1, c2 in zip(a,b):
        print("c1 ", c1, end=" ")
        print("c2 ", c2, end=" ") 
```

A single argument can be passed when traversing a list of lists

```python
a = [[1,2],[3,4]]
test = zip(*a)
print(test) # (1, 3) (2, 4)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
test = zip(*matrix)
print(*test) # (1, 4, 7) (2, 5, 8) (3, 6, 9)
```

Useful when rotating a matrix
```python
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix[:] = zip(*matrix[::-1]) # [[7,4,1],[8,5,2],[9,6,3]]
```

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

## Ternary

a if condition else b
```Python
test = stk.pop() if stk else '#'
```

## Bitwise Operators
```python
'0b{:04b}'.format(0b1100 & 0b1010) # '0b1000' and
'0b{:04b}'.format(0b1100 | 0b1010) # '0b1110' or 
'0b{:04b}'.format(0b1100 ^ 0b1010) # '0b0110' exclusive or
'0b{:04b}'.format(0b1100 >> 2)     # '0b0011' shift right
'0b{:04b}'.format(0b0011 << 2)     # '0b1100' shift left
```

## For Else

Else condition on for loops if break is not called

```python
for w1, w2 in zip(words, words[1:]): #abc, ab
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            adj[c1].append(c2)
            degrees[c2] += 1
            break
    else: # nobreak
        if len(w1) > len(w2):
            return ""   # Triggers since ab should be before abc, not after
```

## Modulo

```python
for n in range(-8,8):
    print n, n//4, n%4
    
 -8 -2 0
 -7 -2 1
 -6 -2 2
 -5 -2 3

 -4 -1 0
 -3 -1 1
 -2 -1 2
 -1 -1 3

  0  0 0
  1  0 1
  2  0 2
  3  0 3

  4  1 0
  5  1 1
  6  1 2
  7  1 3
```

## Any

if any element of the iterable is True
```python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

## All
```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

## Bisect

* bisect.bisect_left returns the leftmost place in the sorted list to insert the given element
* bisect.bisect_right returns the rightmost place in the sorted list to insert the given element

```python
import bisect
bisect.bisect_left([1,2,3,4,5], 2)  # 1
bisect.bisect_right([1,2,3,4,5], 2) # 2
bisect.bisect_left([1,2,3,4,5], 7)  # 5
bisect.bisect_right([1,2,3,4,5], 7) # 5
```

Insert x in a in sorted order. This is equivalent to a.insert(bisect.bisect_left(a, x, lo, hi), x) assuming that a is already sorted. Search is binary search O(logn) and insert is O(n)

```python
import bisect
l = [1, 3, 7, 5, 6, 4, 9, 8, 2]
result = []
for e in l:
    bisect.insort(result, e)
print(result) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
li1 = [1, 3, 4, 4, 4, 6, 7] # [1, 3, 4, 4, 4, 5, 6, 7]
bisect.insort(li1, 5) # 
```

## Iter

Creates iterator from container object such as list, tuple, dictionary and set

```python
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit)) # apple
print(next(myit)) # banana
```

## Map

map(func, *iterables)

```python
my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = list(map(str.upper, my_pets)) # ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]
results = list(map(lambda x, y: (x, y), my_strings, my_numbers)) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
```

## Filter

filter(func, iterable)

```python
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
over_75 = list(filter(lambda x: x>75, scores)) # [90, 76, 88, 81]
```

```python
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def is_A_student(score):
    return score > 75
over_75 = list(filter(is_A_student, scores)) # [90, 76, 88, 81]
```

```python
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes)) # ['madam', 'anutforajaroftuna']
```

## Reduce

reduce(func, iterable[, initial]) 
where initial is optional

```python
numbers = [3, 4, 6, 9, 34, 12]
result = reduce(lambda x, y: x+y, numbers) # 68
result = reduce(lambda x, y: x+y, numbers, 10) #78
```

## Regular Expression

RE module allows regular expressions in python

```python
def removeVowels(self, S: str) -> str:
    return re.sub('a|e|i|o|u', '', S)
```

# Collections

Stack with appendleft() and popleft()

## Deque

```python
from collections import deque
deq = deque([1, 2, 3])
deq.appendleft(5)
deq.append(6)
deq
deque([5, 1, 2, 3, 6])
deq.popleft()
5
deq.pop()
6
deq
deque([1, 2, 3])
```

## Counter

```python
from collections import Counter
count = Counter("hello") # Counter({'h': 1, 'e': 1, 'l': 2, 'o': 1})
count['l'] # 2
count['l'] += 1
count['l'] # 3
```

Get counter k most common in list of tuples
```python
# [1,1,1,2,2,3]
# Counter  [(1, 3), (2, 2)]
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    if len(nums) == k:
        return nums
    return [n[0] for n in Counter(nums).most_common(k)] # [1,2]
```

elements() lets you walk through each number in the Counter
```python
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    c1 = collections.Counter(nums1) # [1,2,2,1]
    c2 = collections.Counter(nums2) # [2,2]
    dif = c1 & c2                   # {2:2}
    return list(dif.elements())     # [2,2]
```

operators work on Counter
```python
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d # {'a': 4, 'b': 3}
c - d # {'a': 2}
c & d # {'a': 1, 'b': 1}
c | d # {'a': 3, 'b': 2}
c = Counter(a=2, b=-4)
+c # {'a': 2}
-c # {'b': 4}
```

## Default Dict

```python
d={}
print(d['Grapes'])# This gives Key Error
from collections import defaultdict
d = defaultdict(int) # set default
print(d['Grapes']) # 0, no key error
d = collections.defaultdict(lambda: 1)
print(d['Grapes']) # 1, no key error
```

```python
from collections import defaultdict
dd = defaultdict(list)
dd['key'].append(1) # defaultdict(<class 'list'>, {'key': [1]})
dd['key'].append(2) # defaultdict(<class 'list'>, {'key': [1, 2]})
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

## Topological Search

[Kahn's algorithm](https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm), detects cycles through degrees and needs all the nodes represented to work 

```python
def alienOrder(self, words: List[str]) -> str:
    nodes = set("".join(words))
    adj = collections.defaultdict(list)
    degree = collections.Counter(nodes)
    
    for w1, w2 in zip(words, words[1:]):
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                adj[c1].append(c2)
                degree[c2] += 1
                break
        else:
            if len(w1) > len(w2):
                return ""
    
    stk = list(filter(lambda x: degree[x]==1, degree.keys()))
    
    ans = []
    while stk:
        node = stk.pop()
        ans.append(node)
        for nei in adj[node]:
            degree[nei] -= 1
            if degree[nei] == 1:
                stk.append(nei)
    
    return "".join(ans) * (set(ans) == nodes)
        
```

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

## Anagrams

Subsection of sliding window, solve with Counter Dict

i.e.
abc   =   bca   !=  eba
111       111       111

```python
def isAnagram(self, s: str, t: str) -> bool:
    sc = collections.Counter(s)
    st = collections.Counter(t)
    if sc != st:
        return False
    return True
```

Sliding Window version (substring)

```python
def findAnagrams(self, s: str, p: str) -> List[int]:
    cntP = collections.Counter(p)
    cntS = collections.Counter()
    P = len(p)
    S = len(s)
    if P > S:
        return []
    ans = []
    for i, c in enumerate(s):
        cntS[c] += 1
        if i >= P:
            if cntS[s[i-P]] > 1:
                cntS[s[i-P]] -= 1
            else:
                del cntS[s[i-P]]
        if cntS == cntP:
            ans.append(i-(P-1))
    return ans
```



## Dynamic Programming

```python
def coinChange(self, coins: List[int], amount: int) -> int:
  MAX = float('inf')
  dp =  [MAX] * (amount + 1)
  dp[0] = 0
  for c in coins:
    for a in range(c, amount+1):    
      dp[a] =  min(dp[a], dp[a-c]+1)      
  return dp[amount] if dp[amount] != MAX else -1
```


[dynamic programming](https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns)
[dp notes](https://leetcode.com/discuss/general-discussion/475924/my-experience-and-notes-for-learning-dp)

## Cyclic Sort

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

## Quick Sort

1. Can be modified for divide in conquer problems

```python
def quickSort(array):
	def sort(arr, l, r):
		if l < r:
			p = part(arr, l, r)
			sort(arr, l, p-1)
			sort(arr, p+1, r)

	def part(arr, l, r):
		pivot = arr[r]
		a = l
		for i in range(l,r):
			if arr[i] < pivot:
				arr[i], arr[a] = arr[a], arr[i]
				a += 1
		arr[r], arr[a] = arr[a], arr[r]
		return a

	sort(array, 0, len(array)-1)
	return array
```

## Merge Sort

```python
from collections import deque 
def mergeSort(array):
    def sortArray(nums):
        if len(nums) > 1:
            mid = len(nums)//2
            l1 = sortArray(nums[:mid])
            l2 = sortArray(nums[mid:])
            nums = sort(l1,l2)
        return nums
    
    def sort(l1,l2):
        result = []
        l1 = deque(l1)
        l2 = deque(l2)
        while l1 and l2:
            if l1[0] <= l2[0]:
                result.append(l1.popleft())
            else:
                result.append(l2.popleft())
        result.extend(l1 or l2)
        return result
	return sortArray(array)
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

## Convert Base

Base 10 to 16, or any base by changing '16' and index
```python
def toHex(self, num: int) -> str:
  rtn = []
  index = "0123456789abcdef"
  if num == 0: return '0'
  if num < 0: num += 2 ** 32
  while num > 0:
    digit = num % 16
    rtn.append(index[digit])
    num = num // 16
  return "".join(rtn[::-1])
```

## Parenthesis

Count can be used if simple case, otherwise stack. 
```python
def isValid(self, s) -> bool:
  cnt = 0
  for c in s:
    if c == '(':
      cnt += 1
    elif c == ')':
      cnt -= 1
      if cnt < 0:
        return False
  return cnt == 0
```

Stack can be used if more complex 
```python
def isValid(self, s: str) -> bool:
  stk = []
  mp = {")":"(", "}":"{", "]":"["}
    for c in s:
      if c in mp.values():
        stk.append(c)
      elif c in mp.keys():
        test = stk.pop() if stk else '#'
        if mp[c] != test:
          return False
  return len(stk) == 0
```

Or must store parenthesis index for further modification

```python
def minRemoveToMakeValid(self, s: str) -> str:
  rtn = list(s)
  stk = []
  for i, c in enumerate(s):
    if c == '(':
      stk.append(i)
    elif c == ')':
      if len(stk) > 0:
        stk.pop()
      else:
        rtn[i] = ''
  while stk:
    rtn[stk.pop()] = ''
  return "".join(rtn)
```

## Max Profit Stock

Infinite Transactions, [base formula](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75924/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems)
```python
def maxProfit(self, prices: List[int]) -> int:
    t0, t1 = 0, float('-inf')
    for p in prices:
        t0old = t0
        t0 = max(t0, t1 + p)
        t1 = max(t1, t0old - p)
    return t0
```

Single Transaction, t0 (k-1) = 0
```python
def maxProfit(self, prices: List[int]) -> int:
    t0, t1 = float('-inf')
    for p in prices:
        t0 = max(t0, t1 + p)
        t1 = max(t1, - p)
    return t0
```

K Transactions
```python
t0 = [0] * (k+1)
t1 = [float(-inf)] * (k+1)
for p in prices:
    for i in range(k, 0, -1):
        t0[i] = max(t0[i], t1[i] + p)
        t1[i] = max(t1[i], t0[i-1] - p)
return t0[k]
```

## Shift Array Right
Arrays can be shifted right by reversing the whole string, and then reversing 0,k-1 and k,len(str)
```python
def rotate(self, nums: List[int], k: int) -> None:
    def reverse(l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    if len(nums) <= 1: return
    k = k % len(nums)
    reverse(0, len(nums)-1, nums)
    reverse(0, k-1, nums)
    reverse(k, len(nums)-1, nums)
```

## Subarray Sum

The total number of continuous subarrays with sum k can be found by hashing the continuous sum per value and adding the count of continuous sum - k

```python
def subarraySum(self, nums: List[int], k: int) -> int:
    mp = {0: 1} 
    rtn, total = 0, 0
    for n in nums:
        total += n
        rtn += mp.get(total - k, 0)
        mp[total] = mp.get(total, 0) + 1
    return rtn
```

## Events

Events pattern can be applied when to many interval problems such as 'Find employee free time between meetings' and 'find peak population' when individual start/ends
are irrelavent and sum start/end times are more important

```python
def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    events = []
    for e in schedule:
        for m in e:
            events.append((m.start, 1))
            events.append((m.end, -1))
    events.sort()
    itv = []
    prev = None
    bal = 0
    for t, c in events:
        if bal == 0 and prev is not None and t != prev:
            itv.append(Interval(prev, t))
        bal += c
        prev = t
    return itv
```

## Merge Meetings

Merging a new meeting into a list

```python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    bisect.insort(intervals, newInterval)
    merged = [intervals[0]]
    for i in intervals:
        ms, me = merged[-1]
        s, e = i
        if me >= s:
            merged[-1] = (ms, max(me, e))
        else:
            merged.append(i)
    return merged
```

## Trie

Good for autocomplete, spell checker, IP routing (match longest prefix), predictive text, solving word games

```python
def __init__(self):
    self.trie = {}
def addWord(self, word: str) -> None:
    node = self.trie 
    for c in word:
        if c not in node:
            node[c] = {}
        node = node[c]
    node['$'] = True
```

Search example with . for wildcards

```python
def search(self, word: str) -> bool:
    def searchNode(word, node):
        for i,c in enumerate(word):
            if c in node:
                node = node[c]
            elif c == '.':
                return any(searchNode(word[i+1:], node[cn]) for cn in node if cn != '$' )
            else:
                return False
        return '$' in node
    return searchNode(word, self.trie)
```

## Kadane

Determine max subarray sum

```python
# input: [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(self, nums: List[int]) -> int:
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums) # max([-2,1,-2,4,3,5,6,1,5]) = 6
```

## Union Find

[Union Find](https://www.geeksforgeeks.org/union-find/) is a useful algorithm for graph

DSU for integers
```python
class DSU:
    def __init__(self, N):
        self.par = list(range(N))

    def find(self, x): # Find Parent
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: # If parents are equal, return False
            return False
        self.par[yr] = xr # Give y node parent of x
        return True # return True if union occured
```

DSU for strings
```python
class DSU:
    def __init__(self):
        self.par = {}

    def find(self, x):
        if x != self.par.setdefault(x, x):
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        self.par[yr] = xr
```

DSU with union by rank
```python
class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        return True
```

## Fast Power

Fast Power, or Exponential by [squaring](https://en.wikipedia.org/wiki/Exponentiation_by_squaring) allows calculating squares in logn time (x^n)*2 = x^(2*n)
```python
def myPow(self, x: float, n: int) -> float:
    if n < 0:
        n *= -1
        x = 1/x
    ans = 1        
    while n > 0:
        if n % 2 == 1:
            ans = ans * x
        x *= x
        n = n // 2
    return ans
```

## Fibonacci Golden

Fibonacci can be calulated with [Golden Ratio](https://demonstrations.wolfram.com/GeneralizedFibonacciSequenceAndTheGoldenRatio/)

```python
def fib(self, N: int) -> int:
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** N + 1) / 5 ** 0.5)
```