"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [0]
Output: [0]

Example 4:
Input: head = [1,3]
Output: [3,1]

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-10^5 <= Node.val <= 10^5
"""

#RECURSION -> TC (O(NLOGN) Space (O(LOGN)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def middle_elem(self, head):
        prev, slow_ptr, fast_ptr = None, head, head
        while fast_ptr and fast_ptr.next:
            prev = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        #if slow_ptr equals to head
        if prev:
            prev.next = None
        return slow_ptr
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        mid_elem = self.middle_elem(head)
        mid_val = TreeNode(mid_elem.val)
        if head == mid_elem:
            return mid_val
        mid_val.left = self.sortedListToBST(head)
        mid_val.right = self.sortedListToBST(mid_elem.next)
        return mid_val
        
        
#RECURSION + CONVERT TO ARRAY   _> TC (O(N) Space (O(N))
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def ll_to_array(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        all_elems = self.ll_to_array(head)
        def conver_list_to_bst(left, right):
            if left > right:
                return None
            middle = (left + right) // 2
            node = TreeNode(all_elems[middle])
            if left == right:
                return node
            node.left = conver_list_to_bst(left, middle - 1)
            node.right = conver_list_to_bst(middle + 1, right)
            return node
        return conver_list_to_bst(0, len(all_elems) - 1)
        if not head:
            return None
        mid_elem = self.middle_elem(head)
        mid_val = TreeNode(mid_elem.val)
        if head == mid_elem:
            return mid_val
        mid_val.left = self.sortedListToBST(head)
        mid_val.right = self.sortedListToBST(mid_elem.next)
        return mid_val

#INORDER SIMULATION -> O(N) TC and O(LOG(N)) SPACE

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def findSize(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # Get the size of the linked list first
        size = self.findSize(head)

        # Recursively form a BST out of linked list from l --> r
        def convert(l, r):
            nonlocal head

            # Invalid case
            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal. Recursively form
            # the left half
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node
            node = TreeNode(head.val)   
            node.left = left

            # Maintain the invariance mentioned in the algorithm
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node
        return convert(0, size - 1)
