# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
t: 2n
s: n
"""

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        #Build adjecency graph
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
    
        rtn = []
        visited = set()
        def dfs2(node, d):
            if d < K:
                visited.add(node)
                for nei in adj[node]:
                    if nei not in visited:
                        dfs2(nei, d+1)
            else:
                rtn.append(node.val)
        
        dfs2(target, 0)
        
        return rtn
                
            
        