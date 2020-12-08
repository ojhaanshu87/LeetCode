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
        
