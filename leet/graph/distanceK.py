# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
time: O(n + k)
space: n
"""
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        adj = collections.defaultdict(list)
        
        def dfsa(node):
            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)
                dfsa(node.left)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
                dfsa(node.right)
                
        dfsa(root)
        
        def dfs(node, prev, d):
            if node:
                if d == K:
                    rtn.append(node.val)
                else:
                    for nei in adj[node]:
                        if nei != prev:
                            dfs(nei, node, d+1)
                    
        rtn = []
        dfs(target, None, 0)
        return rtn