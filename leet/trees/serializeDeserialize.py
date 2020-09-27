# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        rtn = []
        def dfs(node):
            if node:
                rtn.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                rtn.append('#')
                
        dfs(root)
        
        return ' '.join(rtn)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            val = next(vals)
            if val == '#':
                return None
            else:
                node = TreeNode(int(val))
                node.left = dfs()
                node.right = dfs()
                return node

        vals = iter(data.split())
        return dfs()
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
['1', '3', '5', '#', '6', '#', '#', '2', '#', '4', '#', '#']
['1', '3', '5', '#', '6', '#', '#', '2', '#', '4', '#', '#']
