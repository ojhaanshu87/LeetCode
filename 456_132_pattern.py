'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''

# Stack Solution O(N) TC and O(N) Space
#we try to find 2-3-1 pattern in reversed nums.

class Solution(object):
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False
        stack = [] # mono stack (decreasing)
        min_val = float('-inf')
        # reversed 2-3-1 pattern
        for elem in reversed(nums):
            if elem < min_val:
                return True 
            while stack and stack[-1] < elem:
                min_val = stack.pop()
            stack.append(elem)
        return False
