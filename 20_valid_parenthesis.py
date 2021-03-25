'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
'''

class Solution(object):
    def __init__(self):
        self.stack = list()
        self.open = set("({[")
        self.close = set(")}]")
        
    def isValid(self, s):
        for ch in s:
            if ch in self.open:
                self.stack.append(ch)
            elif ch in self.close :
                if not len(self.stack):
                    return False
                end = self.stack.pop(-1)
                if (ch == ")" and end == "(") or (ch == "}" and end =="{") or (ch == "]" and end == "["):
                    continue
                else:
                    return False
        return False if len(self.stack) else True
