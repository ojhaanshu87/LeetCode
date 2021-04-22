'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
'''

class Solution(object):
    def multiply(self, num1, num2):
        num_1, num_2 = 0, 0
        for elem in num1:
            num_1 = num_1 * 10 + ord(elem) - ord('0')
        for elem in num2:
            num_2 = num_2 * 10 + ord(elem) - ord('0')
        return str(num_1 * num_2)
