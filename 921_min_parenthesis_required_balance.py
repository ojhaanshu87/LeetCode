'''
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Example 1:
Input: "())"
Output: 1


Example 2:
Input: "((("
Output: 3

Example 3:
Input: "()"
Output: 0

Example 4:
Input: "()))(("
Output: 4
'''

# O(N) TC and O(1) Space

'''
loop through the input string and use a variable balance to store the number of encountered (-characters which have not been closed yet, 
thus it will be increased every time this character occurs. If the given character is ),
it will be checked if balance > 0 such that this ) can be matched with an open (. If this is the case, 
balance will be reduced by one. In any other case, we need to insert ( right left to it so the number of insertions gets increased by one which is ultimately returned.
'''

class Solution(object):
    def minAddToMakeValid(self, S):
        balance, res = 0, 0 
        for character in S:
            if character == "(":
                balance += 1
            elif character == ")":
                if balance != 0:
                    balance -= 1
                else:
                    res += 1
            else:
                pass
                    
        return res + balance
                
