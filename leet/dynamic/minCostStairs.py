[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

[1, 100, 2, 3, 3, 103, 4, 5, 104, 6]


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0]*(len(cost))
        dp[0], dp[1] = cost[0], cost[1]
        
        for d in range(2, len(cost)):
            dp[d] = min((dp[d-1] + cost[d]), (dp[d-2] + cost[d]))
            
        return min(dp[-2], dp[-1])