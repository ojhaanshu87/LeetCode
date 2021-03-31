'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"
'''

# O(N) time and O(1) space

class Solution(object):
    def reverseWords(self, s):
        # O(N) Time and O(1) space
        current_word = ''
        start = 0
        for x in range(len(s)):
            index = s[x]
            if index == ' ':
                beginning = s[:start]
                end = s[x:]
                s = beginning + current_word + end
                start = x + 1
                current_word = ''
            else:
                current_word = index + current_word
        s = s[:start] + current_word
        return s
        
