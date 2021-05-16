'''
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. 
If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1. 

Example 1:
Input: n = 12
Output: 21

Example 2:
Input: n = 21
Output: -1
'''

# Valid Solution 
class Solution(object):
    def nextGreaterElement(self, n):
        s = str(n)
        index = -1
        for i in range(len(s)-2, -1, -1):#iterate from second last element to see if there is a number smaller than previous
            if s[i] < s[i+1]:
                index = i
                break
        i = index
        if i >= 0:
            prev = i + 1
            for j in range(i+1, len(s)):
                if s[prev]>s[j]>s[i]:
                    prev = j     
            val = int(s[:i]+s[prev]+"".join(sorted(s[i]+s[i+1:prev] + s[prev+1:])))
            return val if val< 2**31 else -1
        return i
        


# Another Method, Step By Step
class Solution(object):
    def nextGreaterElement(self, n):
        # getting each digit
        nums = list(map(int, str(n)))
        
        # step 1 --> Check to see if nums are in descending order then return -1
        # from highest digit to lowest
        indx = len(nums) - 2
        while indx >= 0 and nums[indx] >= nums[indx + 1]:
            indx -= 1
        
        if indx == -1:
            return -1
        
        # step 2 --> index of the value after indx which is less than indx's value
        indx2 = len(nums) - 1
        while nums[indx2] <= nums[indx]:
            indx2 -= 1
        
        # step 3 --> swapping and reversing
        nums[indx], nums[indx2] = nums[indx2], nums[indx]
        nums[indx + 1:] = reversed(nums[indx + 1:])
        
        #return the value
        res = ""
        for num in nums:
            res += str(num)
        res = int(res)
        
        return res if res <= 2 ** 31 else -1


# Run Time Error but valid for many problems (ALL Permutation Method)
from itertools import permutations

class Solution(object):
    def nextGreaterElement(self, n):
        all_nums_of_same_digits = [int(''.join(i)) for i in set(permutations(str(n)))]
        all_nums_of_same_digits.sort()
        num_idx = all_nums_of_same_digits.index(n)
        if all_nums_of_same_digits[num_idx + 1] <= 2**31:
            return all_nums_of_same_digits[num_idx + 1]
        else:
            -1
 


