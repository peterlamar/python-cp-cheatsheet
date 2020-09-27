# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        unweighted = 0
        weighted = 0
        while nestedList:
            nextLevel = []
            for item in nestedList:
                if item.isInteger():
                    unweighted += item.getInteger()
                else:
                    nextLevel.extend(item.getList())
            weighted += unweighted
            nestedList = nextLevel
        return weighted


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.maxDepth = 1
        def getMax(nlist, d):
            self.maxDepth = max(self.maxDepth, d)
            for n in nlist:
                if not n.isInteger():
                    getMax(n.getList(), d+1)
            
        getMax(nestedList, 1)         
        
        def dfs(nlist, d):
            res = 0
            for n in nlist:
                if n.isInteger():
                    res += n.getInteger() * (self.maxDepth - d) 
                elif n.getList():
                    res += dfs(n.getList(), d+1)
            return res
        
        return dfs(nestedList, 0)