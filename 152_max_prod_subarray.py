'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

# Dynamic Programming O(N) TC and O(1) Space 

class Solution(object):
    def maxProduct(self, nums):
        # DP TC O(N) Space O(1)
        if len(nums) == 0:
            return 0
        max_so_far, min_so_far = nums[0], nums[0]
        res = max_so_far
        for idx in range(1, len(nums)):
            curr = nums[idx]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = temp_max
            res = max(max_so_far, res)
        return res
