'''
Given an integer n, return the nth ugly number.

Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 is typically treated as an ugly number.
'''

# Dynamic Programming Approach - O(1) TC and O(1) Space

class Solution(object):
    def nthUglyNumber(self, n):
        # DP Approach, O(1) TC and O(1) Space
        i2, i3, i5, res = 0, 0, 0, [1]
        while len(res) < n:
            temp = min(res[i2] * 2, res[i3] * 3, res[i5] * 5)
            res.append(temp)
            if temp == res[i2] * 2:
                i2 += 1
            if temp == res[i3] * 3:
                i3 += 1
            if temp == res[i5] * 5:
                i5 += 1
        return res[-1]
