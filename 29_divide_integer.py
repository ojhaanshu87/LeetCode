'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For this problem, assume that your function returns 231 − 1 when the division result overflows.
 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
'''

#TC O(log(N)) Space O(1)

LIMIT = 2 ** 31
class Solution(object):
    def divide(self, dividend, divisor):
        check_negative = True if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else False
        dividend, divisor = abs(dividend), abs(divisor) # Space O(1)
        res, pivot = 0, 1
        def limit_check(count, check_negative):
            if not check_negative and count >= LIMIT:
                count = LIMIT - 1
            return count if not check_negative else -count
        # Init pivot and divisor by left shifting (X 2) till dividend <= divisor
        while dividend > divisor: # Time O(logN)
            divisor <<= 1
            pivot <<= 1        
        if dividend == divisor:
            # If dividend == divisor, just return pivot
            return limit_check(pivot, check_negative)
        while pivot > 0: # till pivot > 0 Time O(logN)
            while dividend < divisor:
                pivot >>= 1
                divisor >>= 1
            dividend -= divisor
            res += pivot
        return limit_check(res, check_negative)
        
