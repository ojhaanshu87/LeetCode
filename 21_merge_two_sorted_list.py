'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
'''

# O(N + M) TC and Space O(1)
# Iteration
'''
First, we set up a false "prehead" node that allows us to easily return the head of the merged list later.
We also maintain a prev pointer, which points to the current node for which we are considering adjusting its next pointer. 
Then, we do the following until at least one of l1 and l2 points to null: if the value at l1 is less than or equal to the value at l2, then we connect l1 to the previous node
and increment l1. Otherwise, we do the same, but for l2. Then, regardless of which list we connected, we increment prev to keep it one step behind one of our list heads.

After the loop terminates, at most one of l1 and l2 is non-null. Therefore (because the input lists were in sorted order), 
if either list is non-null, it contains only elements greater than all of the previously-merged elements. This means that we can simply connect the non-null list to the merged list
and return it.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        pre_head = ListNode(-1)
        prev = pre_head
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
                
            else:
                prev.next = l2
                l2 = l2.next
            
            prev = prev.next
        
        # atleast one of l1 and l2 can still have node so connect the non-null list to end of list
        prev.next = l1 if l1 else l2
        
        return pre_head.next
        
