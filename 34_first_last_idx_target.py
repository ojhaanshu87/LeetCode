'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''

class Solution(object):       
    def extreme_insertion_index(self, nums, target, left):
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                high = mid
            else:
                low = mid + 1
        return low
    
    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]
    

#LOGIC but incorrect

class Solution(object):
    def first_occour(self, nums, target): 
        idx = -1
        low, high = 0, len(nums)
        while low < high:
            mid = (high + low) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid +1
            if nums[mid] == target:
                idx = mid
        return idx
    
    def last_occour(self, nums, target):
        idx = -1
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (high + low) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
            if nums[mid] == target:
                idx = mid
        return idx
            
    def searchRange(self, nums, target):
        if nums.count(target) == 1:
            return [0, 0]
        res = []
        res.append(self.first_occour(nums, target))
        res.append(self.last_occour(nums, target))
        return res
    
        
