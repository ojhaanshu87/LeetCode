'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''

#space O(1) time O(N)

class Solution(object):
    def rob(self, nums):
        if len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 1:
            return nums[0]
        else:
            for elem in range(len(nums) - 3, -1, -1):
                if elem + 3 >= len(nums):
                    nums[elem] += nums[elem + 2]  #this will be only for the element 3rd from last. because we should not check the adjecent val as it raises alarm and it wont be having elem + 3 element (out of index). 
                else:
                    nums[elem] += max(nums[elem + 2], nums[elem + 3]) # check only 2 values after adjecent index.
        return max(nums[0], nums[1])
        
