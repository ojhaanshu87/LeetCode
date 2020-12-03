"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

#Always Choose Left Middle Node as a Root
#Algorithm
"""
Implement helper function helper(left, right), which constructs BST from nums elements between indexes left and right:

  If left > right, then there is no elements available for that subtree. Return None.

  Pick left middle element: p = (left + right) // 2.

  Initiate the root: root = TreeNode(nums[p]).

  Compute recursively left and right subtrees: root.left = helper(left, p - 1), root.right = helper(p + 1, right).

Return helper(0, len(nums) - 1).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
     
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def driver(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = driver(left, p - 1)
            root.right = driver(p + 1, right)
            return root
        
        return driver(0, len(nums) - 1)
        
        
