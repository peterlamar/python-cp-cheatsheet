"""
sort coins
11, greatest to least (Greedy)
11 - 5
6 - 5
1 - 2
1 - 1

1,3,4 (Greedy)
4, 1, 1 = 6

(Optimal)
3, 3 = 6

1,3,4

6 = b(5) + 1
6 = b(3) + 3

0 1 2 3 4 5 6 7 8 9 10 11 a: amount
1 3 4                     c: coins

0 1 2 1 1 2 2               dp

# if total can be reached
if c == amount:
    dp[a] = 1
    
# if amount == coin, set dp[a]=1
# if amount == dp[a-coin] + coin:
    
# solution is equal to prior plus coin or previous plus coin
    
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp =  [MAX] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for a in range(c, amount+1):    
                dp[a] =  min(dp[a], dp[a-c]+1)      
        return dp[amount] if dp[amount] != MAX else -1