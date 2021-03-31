'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original. 

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"
'''

class Solution(object):
    def reverse(self, list_elem, start, end):
        while start < end:
            list_elem[start], list_elem[end] = list_elem[end], list_elem[start]
            start, end = start + 1, end - 1
        return
    
    def reverseStr(self, s, k):
        idx = 0
        list_elem = [x for x in s]
        while idx < len(list_elem):
            if idx + k - 1 < len(list_elem):
                self.reverse(list_elem, idx, idx + k - 1)
            else:
                self.reverse(list_elem, idx, len(list_elem) - 1)
            idx = idx + 2 * k
        return "".join(list_elem)
        
