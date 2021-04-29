'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up:

Could you come up with the O(n2) solution?
Could you improve it to O(n log(n)) time complexity?
'''

# Bin Search Approach -> Time: O(NlogN), Space: O(n)

class Solution(object):
    def binarySearch(self, temp_arr, low, high, target):
        while low <= high:
            mid = low + (high - low) // 2
            if temp_arr[mid] == target:
                return mid
            if temp_arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low # low is always ending at the right position 
    
    def lengthOfLIS(self, nums):
        if not nums or len(nums) == 0:
            return 0
        temp_arr = []
        len_point = 1 # len_point put on temp_arr
        temp_arr.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > temp_arr[-1]:
                temp_arr.append(nums[i])
                len_point += 1
            else:
                bs_idx = self.binarySearch(temp_arr, 0, len(temp_arr)- 1, nums[i])
                temp_arr[bs_idx] = nums[i]      
        return len_point



# DP Approach -> Time: O(n^2), Space: O(n)

class Solution(object):
    def lengthOfLIS(self, nums):
        res = 0
        dp_table = [1] * len(nums)
        for elem in range (1, len(nums)):
            for elem1 in range (0, elem):
                if (nums[elem] > nums[elem1] and dp_table[elem] < dp_table[elem1] + 1):
                    dp_table[elem] = dp_table[elem1] + 1
        for elem in range (0, len(nums)):
            res = max(res, dp_table[elem])
        return res
