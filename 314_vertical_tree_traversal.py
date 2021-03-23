'''
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
'''

# Pre-order traversal
# need a col and level variable to indicate which column and level is it
# left, right and res lists to store, and combine three together for final result

#Complexity Analysis

'''
Time Complexity: (W⋅HlogH)) where WW is the width of the binary tree (i.e. the number of columns in the result) and HH is the height of the tree.
In the first part of the algorithm, we traverse the tree in DFS, which results in \mathcal{O}(N)O(N) time complexity.
Space Complexity: \mathcal{O}(N)O(N) where NN is the number of nodes in the tree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def driver_dfs(self, root, left, right, res, col, level):
        if not root:
            return
        if col < 0:
            if len(left) < -col:
                left.append([(root.val, level)])
            else:
                left[-col - 1].append((root.val, level))
        elif col > 0:
            if len(right) < col:
                right.append([(root.val, level)])
            else:
                right[col - 1].append((root.val, level))
        else:
            res[0].append((root.val, level))
        self.driver_dfs(root.left, left, right, res, col - 1, level + 1)
        self.driver_dfs(root.right, left, right, res, col + 1, level + 1)
            
    def verticalOrder(self, root):
        if not root:
            return []
        left, right, res = [], [], [[]]
        self.driver_dfs(root, left, right, res, 0, 0)
        left = left[::-1]
        for ls in [left, res, right]:
            for i in range(len(ls)):
                ls[i].sort(key=lambda x: x[1])
                ls[i] = [val for val, _ in ls[i]]
        return left + res + right
            
        
