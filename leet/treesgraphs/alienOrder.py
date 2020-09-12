class Solution:
    def alienOrder(self, words: List[str]) -> str:
        chars = set("".join(words))
        adj = collections.defaultdict(list)
        degrees = collections.Counter(chars)

        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    adj[c1].append(c2)
                    degrees[c2] += 1
                    break
            else:
                if len(w1) > len(w2):
                    return ""
        
        stk = list(filter(lambda x: degrees[x]==1, degrees.keys()))
        
        rtn = []
        while stk:
            node = stk.pop()
            rtn.append(node)
            for nei in adj[node]:
                degrees[nei] -= 1
                if degrees[nei] == 1:
                    stk.append(nei)
            
        return "".join(rtn) * (set(rtn) == chars)