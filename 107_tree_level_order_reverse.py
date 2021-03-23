'''
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
'''

# RECURSION

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def driver(self, node, res, level):
        if not node:
            return res
        if len(res) == level:
            res.append([])
        res[level].append(node.val)
        if node.left:
            self.driver(node.left, res, level + 1)
        if node.right:
            self.driver(node.right, res, level + 1)
    
    def levelOrderBottom(self, root):
        res = []
        self.driver(root, res, 0)
        return res[::-1]
      
# ITERATIVE (BFS)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        res = []
        next_level = deque([root])
        while root and next_level:
            curr_level = next_level
            next_level = deque()
            res.append([])
            
            for node in curr_level:
                # append the current node value
                res[-1].append(node.val)
                # process child nodes for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
        return res[::-1]
        
