# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        self.res = []
        self.n = len(nestedList)
        self.currentIndex = 0

        def flatList(givenList):
            for item in givenList:
                if item.isInteger():
                    self.res.append(item.getInteger())
                else:
                    flatList(item.getList())
        
        flatList(self.nestedList)

    def next(self):
        """
        :rtype: int
        """
        number = self.res[self.currentIndex]
        self.currentIndex += 1
        return number


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.currentIndex < len(self.res)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())