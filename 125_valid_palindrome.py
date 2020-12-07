"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
"""

#ALGORITHM TC (O(N)) Space O(1)

"""
Set two pointers, one at each end of the input string
  If the input is palindromic, both the pointers should point to equivalent characters, at all times. [1]
    If this condition is not met at any point of time, we break and return early. [2]
  We can simply ignore non-alphanumeric characters by continuing to traverse further.
  Continue traversing inwards until the pointers meet in the middle.
"""

class Solution(object):
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
        
