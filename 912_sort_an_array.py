'''
Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
'''

#  # Counting Sort: Time Complexity O(n+k), Space Complexity O(k)

class Solution(object):
    def sortArray(self, nums):
        _max, _min = max(nums), min(nums)
        if _min >= 0:
            count = [0 for elem in range(_max + 1)]
            for elem in range(len(nums)):
                count[nums[elem]] += 1
            i, j = 0, 0
            while i < _max + 1:
                if count[i] > 0:
                    nums[j] = i
                    j += 1
                    count[i] -= 1
                else:
                    i += 1
        else:
            count = [0 for i in range(_max + 1 -_min)]
            for i in range(len(nums)):
                count[nums[i]-_min] += 1
            i, j = 0, 0
            while i < _max + 1 -_min:
                if count[i] > 0:
                    nums[j] = i +_min
                    j += 1
                    count[i] -= 1
                else:
                    i += 1
        return nums
