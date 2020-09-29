```
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
 
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
   
Given tree t:
   4
  / \
 1   2
Return false.
```
```
#Algorithm -> Time complexity : O(m*n)O(m∗n). In worst case(skewed tree) traverse function takes O(m*n)O(m∗n) time.

              Space complexity : O(n)O(n). The depth of the recursion tree can go upto nn. nn refers to the number of nodes in ss.

Instead of creating an inorder traversal, we can treat every node of the given tree tt as the root, 
treat it as a subtree and compare the corresponding subtree with the given subtree ss for equality.
For checking the equality, we can compare the all the nodes of the two subtrees.


For doing this, we make use a function traverse(s,t) which traverses over the given tree ss and treats every node as the root of the subtree currently being considered. 
It also checks the two subtrees currently being considered for their equality.
In order to check the equality of the two subtrees, we make use of equals(x,y) function, which takes xx and yy,
which are the roots of the two subtrees to be compared as the inputs and returns True or False depending on whether the two are equal or not.
It compares all the nodes of the two subtrees for equality. Firstly, it checks whether the roots of the two trees for equality and then calls itself recursively for the left
subtree and the right subtree. ```

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def traverse(self, root):
        if root == None:
            return 'Null'
        left_list = self.traverse(root.left)
        right_list = self.traverse(root.right)
        return '.'+str(root.val)+'.' + str(left_list) + str(right_list) 
    
    
    def isSubtree(self, s, t):
        if s is None or t is None:
            return False
		    #convert the two trees into two strings
        root_s = self.traverse(s)
        root_t = self.traverse(t)
        if root_s is None or root_t is None:
            return False
		    #check if the child is a substring of parent
        if root_t in root_s:
            return True
        return False
            
        
        
