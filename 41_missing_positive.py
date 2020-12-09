"""
Given an unsorted integer array nums, find the smallest missing positive integer.

Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?

Input: nums = [1,2,0]
Output: 3

Input: nums = [3,4,-1,1]
Output: 2

Input: nums = [7,8,9,11,12]
Output: 1
"""

#ALGORITHM O(N) TC and O(1) Space

"""
Now everything is ready to write down the algorithm.

  Check if 1 is present in the array. If not, you're done and 1 is the answer.
  If nums = [1], the answer is 2.
  Replace negative numbers, zeros, and numbers larger than n by 1s.
  Walk along the array. Change the sign of a-th element if you meet number a. Be careful with duplicates : do sign change only once. Use index 0 to save an information about presence of number n since index n is not available.
  Walk again along the array. Return the index of the first positive element.
  If nums[0] > 0 return n.
  If on the previous step you didn't find the positive element in nums, that means that the answer is n + 1.
"""

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Base case.
        if 1 not in nums:
            return 1
        
        # nums = [1]
        if n == 1:
            return 2
        
        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain 
        # only positive numbers.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array. 
        # If nums[2] is positive - number 2 is missing.
        for i in range(n): 
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
            
        # Now the index of the first positive number 
        # is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
            
        return n + 1
