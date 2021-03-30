'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
'''

class Solution(object):
    def maxSubArray(self, nums):
        # DP, Kadence O(N) Time and O(1) Space
        curr_subarr, max_subarr = nums[0], nums[0]
        for elem in nums[1:]:
            curr_subarr = max(elem, elem + curr_subarr)
            max_subarr = max(max_subarr, curr_subarr)
        return max_subarr

# Divide and Conquor O(N LOG N) TC and O(LOG N) Space where N is len(nums)

class Solution(object):
    def driver_divide_and_conquor(self, nums, mid):
        max_l_sum, max_r_sum = float('-inf'), float('-inf')
        sum_elem = 0
        for i in range(mid-1, -1, -1):
            sum_elem += nums[i]
            max_l_sum = max( max_l_sum , sum_elem)
        sum_elem = 0
        for i in xrange(mid,len(nums), 1):
            sum_elem += nums[i]
            max_r_sum = max( max_r_sum , sum_elem)
        return max_l_sum + max_r_sum
    
    def maxSubArray(self, nums):
        if len(nums) ==  1:
            return nums[0]
        elif not nums:
            return 0
        else :
            mid = len(nums) // 2
            l_sum = self.maxSubArray(nums[:mid])
            r_sum = self.maxSubArray(nums[mid:])
            c_sum = self.driver_divide_and_conquor(nums, mid)
            return max(l_sum, r_sum, c_sum)
        
