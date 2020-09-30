```
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
```

#Non-Optimal -> TC : O(N) and SC : O(1)

class Solution(object):
    def trailingZeroes(self, n):
        count_zero = 0
        for elem in range(5, n+1, 5):
            curr = elem
            while curr % 5 == 0:
                count_zero += 1
                curr //= 5
        return count_zero

#Optimal -> TC : O(logn) return n/5 + n/25 + n/125 + n/625 + n/3125+...;
class Solution(object):
    def trailingZeroes(self, n):
        count_zero = 0
        while n > 0:
            n //= 5
            count_zero += n
        return count_zero
        
       

        
       

