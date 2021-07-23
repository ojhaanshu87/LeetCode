'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
'''

#TC O(N), Space O(N)

'''
Algorithm

Initialize a stack to use for DFS, as well as a variable numGoodNodes that keeps track of how many good nodes are in the tree. The stack should initially contain the root and a very small value (like INT_MIN).

Execute DFS: while the stack is not empty, pop from the stack.

At each node, first check if node.val is greater than or equal to the number associated with it maxSoFar. If it is, then increment numGoodNodes. Next, push the children onto the stack, along with the greater value between maxSoFar and node.val.

Return numGoodNodes
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        stack = [(root, float("-inf"))]
        res = 0
        while stack:
            node, max_so_far = stack.pop()
            if max_so_far <= node.val:
                res += 1
            if node.left:
                stack.append((node.left, max(node.val, max_so_far)))
            if node.right:
                stack.append((node.right, max(node.val, max_so_far)))
        return res
        
