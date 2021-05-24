'''
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares
while 3 and 11 are not.

 

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

 #O(root(N)) TC and Space O(1)

class Solution(object):
    def is_square(self, num):
        return int(num ** 0.5) ** 2 == num
    
    def is_two_squares(self, num):
        #Use the Sum of 2 Squares Theorem
        for p in range(3, num + 1, 4):
            #Count the Number of Times p Divides n (mod 2) 
            k = 0
            while num % p == 0:
                num //= p
                k ^= 1

            #Check the Count
            if k:
                #The Test Failed
                return False
            elif num < p:
                #There's No Point Searching Anymore Because p is Only Getting Bigger
                break
        #The Test Succeeded
        return True
    
    def is_three_squares(self, num):
        if num % 8 not in (0, 4, 7):
            return True
        
        #Divide by 4^a
        while num % 4 == 0:
            num //= 4

        #Test if n is a Sum of 3 Squares
        return num % 8 != 7
    
    def numSquares(self, n):
        if self.is_square(n):
            return 1
        elif self.is_two_squares(n):
            #Sum of 2 Squares Theorem
            return 2
        elif self.is_three_squares(n):
            #Lagrange's Three-Square Theorem
            return 3
        else:
            #Lagrange's Four-Square Theorem
            return 4
        
