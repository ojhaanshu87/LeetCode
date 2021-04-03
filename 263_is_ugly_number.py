'''
Given an integer n, return true if n is an ugly number.

Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.

Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 8
Output: true
Explanation: 8 = 2 × 2 × 2

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.

Example 4:
Input: n = 1
Output: true
Explanation: 1 is typically treated as an ugly number.
'''
class Solution(object):
    def  all_prime_factors(self, number):
        elem = 2
        factors = []
        while elem * elem <= number:
            if number % elem:
                elem += 1
            else:
                number //= elem # divide with integral result (discard remainder)
                factors.append(elem)
        if number > 1:
            factors.append(number)
        return factors
    
    def isUgly(self, n):
        if n == 0:
            return False
        if n < 0:
            return False
        
        static_val = [2, 3, 5]
        all_factors = self.all_prime_factors(n)
        for elem in all_factors:
            if elem not in static_val:
                return False
        return True
        
