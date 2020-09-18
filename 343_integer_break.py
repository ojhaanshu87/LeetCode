```
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
```

class Solution(object):
    def integerBreak(self, n):
        defined_val = {2: 1, 3: 2, 4: 4}
        if n in defined_val:
            return defined_val[n]
        
        div = n/3
        if n%3 == 1:
            div -= 1
            
        leftover = n - (div * 3)
        if leftover:
            return pow(3, div)*leftover
        else:
            pow(3,div) 

#DP APPROACH

# class Solution(object):
#     def integerBreak(self, n):
#         dp_table = [0]*59
#         dp_table[0] = 1
#         for i in range(0,59):
#             for j in range(1,10):
#                 if i+j < 59:
#                     dp_table[i+j] = max(dp_table[i]*j, dp_table[i+j])
#                 else:
#                     break
#         dp_table[2], dp_table[3] = 1, 2
#         return dp_table[n]
