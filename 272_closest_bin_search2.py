"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""

#ALGORITHM - BFS
# Time Complexity:O(N)+O(K)* O(log(N)) where N is Number of Nodes
# Auxilary Space: O(N) for queue and heap

#Traverse the tree to get all the nodes and store the absolute difference value. Using a heap , pop the lowest /nearest to target values from the heap in O(log(n)) time.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestKValues(self, root, target, k):
        heap = []
        queue = [root]
        # bfs tree traversal
        while queue:
            temp = queue.pop(0)
            heapq.heappush(heap,(abs(target-temp.val),temp.val))
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res

