"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

#ALGORITHM -> TC (O(N + M)) & SpaceComplexity (O(max(N, M))) where N and M are length of input

"""
Convert a and b into integers x and y, x will be used to keep an answer, and y for the carry.

  While carry is nonzero: y != 0:

  Current answer without carry is XOR of x and y: answer = x^y.

  Current carry is left-shifted AND of x and y: carry = (x & y) << 1.

  Job is done, prepare the next loop: x = answer, y = carry.

Return x in the binary form.
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        temp1, temp2 = int(a, 2), int(b, 2)
        while temp2:
            ans = temp1 ^ temp2
            carry = (temp1 & temp2) << 1
            temp1, temp2 = ans, carry
        return bin(temp1)[2:]
