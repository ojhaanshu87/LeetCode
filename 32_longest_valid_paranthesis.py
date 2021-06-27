'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring. 

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
'''

# O(N) TC and O(1) space

class Solution(object):
    def longestValidParentheses(self, s):
        temp = [-1]
        res  = 0
        for idx, elem in enumerate(s):
            if temp[-1] != -1 and s[temp[-1]] == "(" and elem == ")":
                temp.pop()
                res = max(res, idx - temp[-1])
            else:
                temp.append(idx)

        return res
