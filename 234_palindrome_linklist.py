'''
Given the head of a singly linked list, return true if it is a palindrome.
'''


#TC O(N) and Space O(1)

# Find the end of the first half.
# Reverse the second half.
# Determine whether or not there is a palindrome.
# Restore the list.
# Return the result.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def end_of_first_half (self, head):
        fast_ptr, slow_ptr = head, head
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
        
        # find end of first half and reverse second half
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_ll(first_half_end.next)
        
        # check whether or not there is palindrome
        res, first_pos, second_pos = True, head, second_half_start
        while res and second_pos:
            if first_pos.val != second_pos.val:
                res = False
            first_pos = first_pos.next
            second_pos = second_pos.next
        
        # Restore the list and return res
        first_half_end.next = self.reverse_ll(second_half_start)
        return res
        
        
        
