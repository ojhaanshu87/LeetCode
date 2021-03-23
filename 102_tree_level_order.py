'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

#RECURSION

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
            
    def levelOrder(self, root):
        res = []
        self.driver(root, res, 0)
        return res
        
# BFS 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        from collections import deque
        res = []
        if not root:
            return res
        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            res.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                res[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return res
        
        
