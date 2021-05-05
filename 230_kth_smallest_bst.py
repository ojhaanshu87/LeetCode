'''
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.
'''
# O(K) TC and O(1) Space . Morris Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):    
    def kthSmallest(self, root, k):
        # O(K) time and O(1) space where K is height. Morris Traversal
        while root:
            cur = root.left
            while cur and cur.right and cur.right != root:
                cur = cur.right    
            if cur == None or cur.right == root:
                k -= 1
                if k == 0:
                    return root.val
                root = root.right
            else:
                cur.right = root
                root = root.left
        

# Iterative Inorder -> # O(H+K) time and O(H) space where H is height


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):    
    def kthSmallest(self, root, k):
        # O(H+K) time and O(H) space where H is height
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
        
