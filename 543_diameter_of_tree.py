```
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
```

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.diameter = 0
        
    def height (self, root):
        if root is None:
            return 0
        if root and root.left is None and root.right is None:
            return 1
        left = self.height(root.left)
        right = self.height(root.right)
        if left+right > self.diameter:
            self.diameter = left+right
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        self.height(root)
        return self.diameter
        
