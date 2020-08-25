class Solution:
    """
    https://leetcode.com/problems/fruit-into-baskets/discuss/170740/JavaC%2B%2BPython-Sliding-Window-for-K-Elements
    https://leetcode.com/problems/minimum-size-subarray-sum/
    https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
    https://leetcode.com/problems/max-consecutive-ones-iii/

1. Have a counter or hash-map to count specific array input 
and keep on increasing the window toward right using 
outer loop.
1. Have a while loop inside to reduce the window side by 
sliding toward right. Movement will be based on constraints 
of problem. 
1. Store the current maximum window size or minimum window
size or number of windows based on problem requirement.

    """
    def totalFruit(self, tree: List[int]) -> int:
      maxCount, j = 0, 0
      ht = {}

      # counter with hashmap to move right
      for i, c in enumerate(tree):
        ht[c] = ht.get(c, 0) + 1

        # reduce window right with if or while loop
        if len(ht) <= 2:
          maxCount = max(maxCount, i-j+1) # Store max
        else:
          jc = tree[j]
          ht[jc] -= 1
          if ht[jc] <= 0:
            del ht[jc]
          j += 1  

      return maxCount