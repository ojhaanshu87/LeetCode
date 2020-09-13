#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].

#Input: nums = [3,3], target = 6
#Output: [0,1]

class Solution(object):
    def twoSum(self, nums, target):
        res = {}
        for elem in range (0, len(nums)):
            if nums[elem] in res:
                return [res[nums[elem]], elem]
            else:
                res[target - nums[elem]] = elem
