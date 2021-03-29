'''
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A.
Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
'''

# O(N) time O(N) Space

class Solution(object):
    def rotateString(self, A, B):
        if len(A) == 0 and len(B) == 0:
            return True
         # pick the first char of b 
        first_char = B[0]
        # search for the first_char in a
        for i in range(len(A)):
            if A[i] == first_char:
                if (A[i:] + A[:i] == B):
                    return True
        return False
