'''
Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

Example 1:
Input: preorder = [5,2,1,3,6]
Output: true

Example 2:
Input: preorder = [5,2,6,1,3]
Output: false
'''

# Convert to Inorder and check if sorted or not 
# TC O(N) and Space O(N)

class Solution(object):
    def to_inorder(self, preorder):
        # O(N) TC and O(N) Space
        stack = deque()
        inorder = []
        for pre in preorder:
            while stack and pre > stack[-1]:
                inorder.append(stack.pop())
            stack.append(pre)
        while stack:
            inorder.append(stack.pop())
        return inorder
    
    def verifyPreorder(self, preorder):
        inorder = self.to_inorder(preorder)
        for elem in range(1, len(inorder)):
            if inorder[elem - 1] > inorder[elem]:
                return False
        return True
        

