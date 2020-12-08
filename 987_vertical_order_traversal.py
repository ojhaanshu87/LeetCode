"""
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order
from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

Example 1:

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We can do a tree pre-order traversal, and assign (x,y) position at the same time. Since both x, y coordinates and node value are recorded in a dict, x as key, a list of (y, node val) as value, we can sort the output finally according to the confusing discription.

class Solution(object):
    def DFS(self, root, x, y, res):
        if x in res:
            res[x].append((y, root.val))
        else:
            res[x] = [(y, root.val)]
        if root.left:
            self.DFS(root.left, x-1, y-1, res)
        if root.right:
            self.DFS(root.right, x+1, y-1, res)
    
    def verticalTraversal(self, root):
        # key is x coordinate, value is a list of tuple (y coordinate, node value)
        res = {}
        self.DFS(root, 0, 0, res)
        res2 = sorted(res.items(), key=lambda x: x[0])
        res2 = [v for k, v in res2]
        
        # now res2 is a list of list of tuples
        final_res = []
        for r in res2:
			# First sort by y value in decreasing order, then sort tree node value in increasing order
            val = sorted(r, key=lambda x: (-x[0], x[1]))
            val = [y for x, y in val]
            final_res.append(val)
        
        return final_res
        
        
        
        
        
