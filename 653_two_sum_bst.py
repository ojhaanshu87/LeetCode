'''
Given the root of a Binary Search Tree and a target number k,
return true if there exist two elements in the BST such that their sum is equal to the given target.
'''

# O(N) TC O(N) Space

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder_traversal(self, root, inorder):
        if root:
            self.inorder_traversal(root.left, inorder)
            inorder.append(root.val)
            self.inorder_traversal(root.right, inorder)
        
    def findTarget(self, root, k):
        res = []
        self.inorder_traversal(root, res)
        low, high = 0, len(res) - 1
        while low < high:
            temp = res[low] + res[high]
            if temp == k:
                return True
            elif temp < k:
                low += 1
            else:
                high -= 1
        return False
