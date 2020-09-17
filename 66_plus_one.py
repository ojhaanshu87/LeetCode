```
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]

Input: digits = [1, 2, 9]
Output: [1, 3, 0]

Input: digits = [9, 9, 9]
Output: [1, 0, 0, 0]
```

class Solution(object):
    def plusOne(self, digits):
        for elem in range(0, len(digits)):
            idx = len(digits) -1 - elem
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
        #if all digits are 9
        return [1] + digits

