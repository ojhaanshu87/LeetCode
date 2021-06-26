'''
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        #edge case
        if not head or not head.next:   
            return head                 
        #get pre_node and dummy point to node 0          
        pre_node = dummy = ListNode(0)   
        #link dummy to head
        dummy.next = head
        while head and head.next:   
            #set next_node node after head each time 
            next_node = head.next        
            #swapping
            head.next = next_node.next    
            next_node.next = head         
            pre_node.next = next_node  
            #after swapping
            #move head to one node next becasue head is at node 1 
            head = head.next  
            #move pre_node to one node before head which is next_node.next node
            pre_node = next_node.next          
        return dummy.next
        
