'''
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums, return the minimum number of elements to remove to make nums a mountain array.

 

Example 1:
Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.

Example 2:
Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].

Example 3:
Input: nums = [4,3,2,1,1,2,3,1]
Output: 4

Example 4:
Input: nums = [1,2,3,4,4,3,2,1]
Output: 1
 

Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.
'''

# DP Approach O(N^2) TC and O(N) Space

'''
let dp1[i] be maximum length of LIS, ending with element index i and dp2[i] be maximum length of Mountain array.
Then, update of dp1 is straightforward: iterate over all previous elements and update it.
For dp2[i] we again need to iterate over all previous elements and if nums[j] < nums[i], we can update dp2[i], using dp2[j] + 1 or dp1[j] + 1.
'''

class Solution(object):
    # TC O(N^2) Space O(N)
    def minimumMountainRemovals(self, nums):
        max_len_of_lis, max_len_mountain_array = [1] * len(nums), [1] * len(nums)
        for elem in range(1, len(nums)):
            for elem1 in range(elem):
                if nums[elem1] < nums[elem]: max_len_of_lis[elem] = max(max_len_of_lis[elem], 1+max_len_of_lis[elem1])
                if nums[elem1] > nums[elem]: 
                    if max_len_of_lis[elem1] > 1:
                        max_len_mountain_array[elem] = max(max_len_mountain_array[elem], 1 + max_len_of_lis[elem1])
                    if max_len_mountain_array[elem1] > 1:
                        max_len_mountain_array[elem] = max(max_len_mountain_array[elem], 1 + max_len_mountain_array[elem1])
        return len(nums) - max(max_len_mountain_array)
