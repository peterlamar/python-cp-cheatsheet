# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        values = collections.defaultdict(list)
        
        def dfs(node, lvl):
            if node is None:
                return
            
            values[lvl].append(node.val)
            dfs(node.left, lvl+1)
            dfs(node.right, lvl +1)
        
        rtn = []
        
        dfs(root, 0)
        
        for k in values:
            rtn.append(max(values[k]))
        
        return rtn

    def largestValues(self, root: TreeNode) -> List[int]:
        self.curLevel = 0
        self.curMax = float('-inf')
        self.rtn = []
        
        if root is None:
            return
        
        d = deque([(root, 0)])            
        while d:
            node, lvl = d.popleft()
            if node:
                if lvl > self.curLevel:
                    self.rtn.append(self.curMax)
                    self.curMax = float('-inf')
                    self.curLevel = lvl
                self.curMax = max(self.curMax, node.val)
                d.append((node.left, lvl+1))
                d.append((node.right, lvl+1))
        
        self.rtn.append(self.curMax)

        return self.rtn