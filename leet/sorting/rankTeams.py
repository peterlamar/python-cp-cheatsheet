class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        sumTally = { v:[0]* len(votes[0]) + [v] for v in votes[0]}
        
        for v in votes:
            for i, c in enumerate(v):
                sumTally[c][i] -= 1
        
        return "".join(sorted(sumTally, key = lambda x: sumTally[x]))