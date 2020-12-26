'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

'''
Specifically, the steps we need to do are:

Find the middle.
Reverse the second half.
Determine whether or not there is a palindrome.
Restore the list.
Return the result.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middle_elem(self, head):
        slow_ptr, fast_ptr = head, head
        while fast_ptr.next and fast_ptr.next.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        return slow_ptr
    
    def reverse_ll(self, head):
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def isPalindrome(self, head):
        if head is None:
            return True
        
        middle_elem = self.middle_elem(head)
        reverse_ll = self.reverse_ll(middle_elem.next)
        
        result, first, second = True, head, reverse_ll
        
        while result and second:
            if first.val != second.val:
                result = False
            first = first.next
            second = second.next
        
        middle_elem.next = self.reverse_ll(reverse_ll)
        return result
        
