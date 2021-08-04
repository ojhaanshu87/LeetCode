'''
Given the root of a binary tree,
return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
'''

# level order + 2 lines

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
       #whatever code you use to solve the level order traversal
        if root is None:
            return 
        
        queue, res_list = [], []
        queue.append(root)
        
        while len(queue) > 0:
            res = []
            for l in range(len(queue)):
                node = queue.pop(0)
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res_list.append(res)
        #you only need to add this part to check the nature of level and reverse the nodes
        for elem in range(len(res_list)):
            if elem % 2 == 1:
                res_list[elem] = res_list[elem][::-1]
                
        return res_list
        
