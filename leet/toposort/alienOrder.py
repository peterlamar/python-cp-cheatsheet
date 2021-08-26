"""
Alien Dictionary
O(n) for letters in words
O(1) since constant letters (26)
"""
class Solution:
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
        