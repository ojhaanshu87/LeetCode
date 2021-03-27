"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

# TC and Space (O(N))
# Since the array A is sorted, loosely speaking it has some negative elements with squares in decreasing order, 
# then some non-negative elements with squares in increasing order.
# For example, with [-3, -2, -1, 4, 5, 6], we have the negative part [-3, -2, -1] with squares [9, 4, 1], and the positive part [4, 5, 6] with squares [16, 25, 36]. 
# Our strategy is to iterate over the negative part in reverse, and the positive part in the forward direction.
# We can use two pointers to read the positive and negative parts of the array - one pointer j in the positive direction, and another i in the negative direction.
# Now that we are reading two increasing arrays (the squares of the elements), we can merge these arrays together using a two-pointer technique.

class Solution(object):
    def sortedSquares(self, nums):
        # We first declare a list of length, len(A) then add the larger square from the back of the list, denoted by the index r - l
        res = [0] * len(nums)
        start, end = 0, len(nums) - 1
        while start <= end:
            left, right = abs(nums[start]), abs(nums[end])
            if left > right:
                res[end - start] = left * left
                start += 1
            else:
                res[end - start] = right * right
                end -= 1
        return res
        
