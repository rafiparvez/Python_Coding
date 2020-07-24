# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
# Solution: https://leetcode.com/articles/flatten-nested-iterator/
# APPROACH 1: RECURSIVE
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self._integers = list()
        self.curr = 0
        self._flatten_list(self.nestedList)
        
    def _flatten_list(self, nestedList: [NestedInteger]):
        for nested_int in nestedList:
            if nested_int.isInteger():
                self._integers.append(nested_int.getInteger())
            else:
                self._flatten_list(nested_int.getList())
                
    def next(self) -> int:
        if self.hasNext():
            num = self._integers[self.curr]
            self.curr +=1
            return num
        
    def hasNext(self) -> bool:
        if self.curr < len(self._integers):
            return True
        else:
            return False
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


# APPROACH 2: DFS Using STACKs
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))
        
    def next(self) -> int:
        self._make_top_an_integer()
        return self.stack.pop().getInteger()
        
    def _make_top_an_integer(self):
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(reversed(self.stack.pop().getList()))
    
    def hasNext(self) -> bool:
        self._make_top_an_integer()
        return len(self.stack) > 0
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
