'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''

# O(N) TC and O(1) Space

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def ll_length(self, head):
        temp = head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count
    
    def reverseKGroup(self, head, k):
        list_length = self.ll_length(head)
        if list_length == 1 or k == 1 or list_length < k:
            return head
        reverses = list_length / k
        remainders = list_length % k
        dummy = ListNode()
        prev_head = dummy
        prev_tail = None
        temp = head
        while reverses > 0:
            tempHead = temp
            for i in range(k):
                temp1 = temp.next
                temp.next = prev_tail
                prev_tail = temp
                temp = temp1
            prev_head.next = prev_tail
            prev_tail = None
            prev_head = tempHead
            reverses -= 1
        if remainders > 0:
            prev_head.next = temp
        return dummy.next
