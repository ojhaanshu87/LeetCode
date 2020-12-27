'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
'''
'''
Simplify problem down to two cases: sum or subtraction of two positive integers: x \pm yx±y, where x > yx>y. Save down the sign of the result.

If one has to compute the sum:

     While carry is nonzero: y != 0:

          Current answer without carry is XOR of x and y: answer = x^y.

          Current carry is left-shifted AND of x and y: carry = (x & y) << 1.

          Job is done, prepare the next loop: x = answer, y = carry.

     Return x * sign.

If one has to compute the difference:

     While borrow is nonzero: y != 0:

        Current answer without borrow is XOR of x and y: answer = x^y.

        Current borrow is left-shifted AND of NOT x and y: borrow = ((~x) & y) << 1.

        Job is done, prepare the next loop: x = answer, y = borrow.

    Return x * sign.
'''
class Solution(object):
    def getSum(self, a, b):
        num1, num2 = abs(a), abs(b)
        if num1 < num2:
            return self.getSum(b, a)
        sign = 1 if a > 0 else -1
        if a * b >= 0:
            while num2:
                answer = num1 ^ num2
                carry = (num1 & num2) << 1
                num1, num2 = answer, carry
                
        else:
            while num2:
                answer = num1 ^ num2
                borrow = ((~num1) & num2) << 1
                x, y = answer, borrow
        return num1 * sign
