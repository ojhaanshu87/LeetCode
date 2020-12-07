"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.
Example 2:

Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
"""

#ITERATIVE SOLUTION (DFS)

class Solution(object):
    def depthSum(self, nestedList):
        if not nestedList:
            return 0
        res = 0
        stack = [(elem, 1) for elem in nestedList]
        while stack:
            elem, depth = stack.pop()
            if not elem.isInteger():
                for nested in elem.getList():
                    stack.append((nested, depth + 1))
            else:
                 res += depth * elem.getInteger()
        return res
 
 #RECURSIVE SOLUTION

class Solution(object):
    
    def driver_depthSum(self, nestedInt, depth = 1):
        if nestedInt.isInteger():
            return depth * nestedInt.getInteger()
        else:
            accum_sum = 0
            for elem in nestedInt.getList():
                accum_sum += self.driver_depthSum(elem, depth + 1)
            return accum_sum
    
    def depthSum(self, nestedList):
        res = 0
        for elem in nestedList:
            res += self.driver_depthSum(elem)
        return res
