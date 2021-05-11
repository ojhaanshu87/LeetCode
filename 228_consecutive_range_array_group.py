'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Example 3:
Input: nums = []
Output: []

Example 4:
Input: nums = [-1]
Output: ["-1"]

Example 5:
Input: nums = [0]
Output: ["0"]
'''

# O(N) Binary Search

class Solution(object):
    def summaryRanges(self, nums):
        # What if the array is long and most of the elements are identical.
        start = 0
        res = []
        while start < len(nums):
            low, high = start, len(nums)
            while low < high:
                mid = (low + high) >> 1
                if nums[mid] - mid == nums[start] - start:
                    low = mid + 1
                else:
                    high = mid
            if start == low - 1:
                res.append(str(nums[start]))
            else:
                res.append(str(nums[start]) + '->' + str(nums[low-1]))
            start = low  
        return res
        
        
