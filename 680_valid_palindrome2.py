"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000
"""

#ALGORITHM TC (O(N)) Space O(1)

"""
Suppose we want to know whether s[i], s[i+1], ..., s[j] form a palindrome. 
If i >= j then we are done. If s[i] == s[j] then we may take i++; j--. Otherwise, the palindrome must be either s[i+1], s[i+2], ..., s[j] or s[i], s[i+1], ..., s[j-1], 
and we should check both cases.
"""

class Solution(object):
    def validPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                tmp1 = s[:start] + s[start + 1:]
                tmp2 = s[:end] + s[end + 1:]
                return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
        return True
        


