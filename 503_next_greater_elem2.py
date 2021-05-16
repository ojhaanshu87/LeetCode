'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number
. If it doesn't exist, return -1 for this number.
Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
Constraints:
1 <= nums.length <= 104
-109 <= nums[i] <= 109
'''

from collections import deque

class Solution(object):
    def nextGreaterElements(self, nums):
        # Monotonic Stack O(N) time and O(N) space
        # https://labuladong.gitbook.io/algo-en/ii.-data-structure/monotonicstack#:~:text=Monotonic%20stack%20is%20actually%20a,element%20putting%20into%20the%20stack.
        result = [-1] * len(nums)
        stack = deque()
        for elem in range(2 * len(nums) -1, -1, -1):
            while stack and stack[-1] <= nums[elem % len(nums)]:
                stack.pop()
            result[elem % len(nums)] = stack[-1] if stack else -1
            stack.append(nums[elem % len(nums)])  
        return result
