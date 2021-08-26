"""
time: n + e
space: n
Paint
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = {}
        for n in range(len(graph)):
            if n not in seen:
                seen[n] = 0
                stk = [n]
                while stk:
                    node = stk.pop()
                    for nei in graph[node]:
                        if nei not in seen:
                            seen[nei] = seen[node] ^ 1
                            stk.append(nei)
                        elif seen[nei] == seen[node]:
                            return False
        return True
    