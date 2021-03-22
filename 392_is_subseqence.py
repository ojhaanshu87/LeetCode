'''
Given two strings s and t, check if s is a subsequence of t.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing
the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''

# Two Pointers (left for source, right for target)
# If source[left] == target[right] found a match & move both pointers one step forward.
# source[left] != target[right] no match and move only right pointer on target string
# TC O(T) where T is Target string length, Space O(1) 

class Solution(object):
    def isSubsequence(self, s, t):
        ptr_left, ptr_right = 0, 0
        while ptr_left < len(s) and ptr_right < len(t):
            if s[ptr_left] == t[ptr_right]:
                ptr_left += 1
            ptr_right += 1
        return ptr_left == len(s)
