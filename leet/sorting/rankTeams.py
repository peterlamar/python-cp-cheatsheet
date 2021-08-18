class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # Create 2D data structure A : 0, 0, 0, 'A', C: 0, 0, 0, 'B'
        rnk = {v:[0] * len(votes[0]) + [v] for v in votes[0]}

        # Tally votes in reverse because sort defaults ascending
        for v in votes:
            for i, c in enumerate(v):
                rnk[c][i] -= 1
                  
        # Sort
        return "".join(sorted(rnk, key = lambda x: rnk[x]))