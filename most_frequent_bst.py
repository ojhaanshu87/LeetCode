'''
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [1,null,2,2]
Output: [2]
'''

# O(N) TC and O(1) Space

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        self.res, self.maxcount, self.curcount, self.curnum = [], 0, 0, float("-Inf")
        def helper(node):
            if node: 
                helper(node.left)
                if self.curnum != node.val:
                    self.curnum = node.val
                    self.curcount = 1 
                else: 
                    self.curcount += 1
                if self.curcount == self.maxcount: 
                    self.res.append(node.val)
                elif self.curcount > self.maxcount:
                    self.maxcount = self.curcount 
                    self.res = [node.val]
                helper(node.right)
        
        helper(root)
        return self.res
