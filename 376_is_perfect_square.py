'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false
'''
# Binary Search O(logN) TC and Space O(1)
class Solution(object):
    def isPerfectSquare(self, num):
        if num < 2:
            return True
        left_boundary, right_boundary = 2, num // 2
        while left_boundary <= right_boundary:
            mid = left_boundary + (right_boundary - left_boundary) // 2
            square = mid * mid
            if square == num:
                return True
            if square > num:
                right_boundary = mid - 1
            else:
                left_boundary = mid + 1
        return False
      
 
# Substraction Method 
class Solution(object):
    def isPerfectSquare(self, num):
        subtract = 1
        while num > 0:
            num -= subtract
            subtract += 2
        if num == 0:
            return True
        else:
            return False
