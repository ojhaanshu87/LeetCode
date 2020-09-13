#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.

#Input: nums = [-1]
#Output: -1

#Input: nums = [-2147483647]
#Output: -2147483647

class Solution(object):
    def maxSubArray(self, nums):
        max_so_far , curr_max = float('-inf'), float('-inf')
        for elem in nums:
            curr_max = max(elem, curr_max + elem)
            max_so_far = max(max_so_far,curr_max) 
        
        return max_so_far
