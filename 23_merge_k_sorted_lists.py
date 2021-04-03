'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
'''

# O(NLOGN) TC and O(1) Space

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def driver_merge_two_list(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        dummy = ListNode(None)
        res = dummy
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1, dummy = l1.next, dummy.next
            else:
                dummy.next = l2
                l2, dummy = l2.next, dummy.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return res.next
    
    def mergeKLists(self, lists):
        if not lists:
            return
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.driver_merge_two_list(lists[0], lists[1])
        else:
            l1 = self.mergeKLists(lists[:len(lists) //  2])
            l2 = self.mergeKLists(lists[len(lists) // 2:])
            return self.driver_merge_two_list(l1, l2)
        
