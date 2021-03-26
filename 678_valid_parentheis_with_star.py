'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true
'''

#using two stacks to record the index of ( and * -> TC and Space O(N)

#we push the index to s1 if ( occurent and push the index to s2 if * occurent
#if ) occurent, we try to pop the last ( first, if s1 is empty which mean there are no ( anymore. we try to use * replace (. we return False when both of s1 and s2 are empty
#After go throught the string, we need to analyse the position of rest of (, we need one * with larger index for each (.

class Solution(object):
    def checkValidString(self, s):
        if not s:
            return True
        s_brackets, s_star = [], []
        for i in range(len(s)):
            if s[i] == "(":
                s_brackets.append(i)
            elif s[i] == "*":
                s_star.append(i)
            elif s[i] == ")":
                if s_brackets:
                    s_brackets.pop(-1)
                else:
                    if s_star:
                        s_star.pop(-1)
                    else:
                        return False
        while s_brackets:
            if not s_star:
                return False
            else:
                if s_brackets.pop(-1) > s_star.pop(-1):
                    return False
        return True
      
# Greedy O(N) Time and O(1) Space

class Solution(object):
    def checkValidString(self, s):
        left_bal, right_bal = 0, 0
        for i in range(len(s)):
            left_bal += 1 if s[i] in '(*' else -1
            right_bal += 1 if s[~i] in ')*' else -1
            if left_bal < 0 or right_bal < 0:
                return False
        
        return True
