'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeSorted(self, left, right):
        head = temp = ListNode()
        while left and right:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next 
        temp.next = left if left else right
        return head.next
    
    def sortList(self, head):
        # divide and conquer
        # divide into 2 halves
        # sort each half
        # merge 2 havles
        if head == None or head.next == None:
            return head
        slow, fast = head, head
        while fast and fast.next:
            tail = slow
            fast = fast.next.next
            slow = slow.next  
        tail.next = None
        # sort each half
        left = self.sortList(head)
        right = self.sortList(slow)
        # merge 2 halves
        return self.mergeSorted(left, right)
