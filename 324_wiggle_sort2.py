'''
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

 

Example 1:

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
Example 2:

Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 5000
It is guaranteed that there will be an answer for the given input nums.
 

Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
'''
# Brute Force O(NlogN) TC and O(N) Space
          #Just put sorted numbers in array
          # Put largest numbers in odd indexes first
          # Then put remaining numbers in even indexes
          # So even < odd > even

class Solution(object):
    def wiggleSort(self, nums):
        arr = sorted(nums)
        for i in range(1, len(nums), 2):
            nums[i] = arr.pop() 
        for i in range(0, len(nums), 2): 
            nums[i] = arr.pop() 
        return nums
      
# O(N) TC and O(1) Space
def wiggleSort(self, nums: List[int]) -> None:
	# like count sort
    count = [0] * 5001
    for i in nums:
        count[i] += 1
    
    i = 0
    c = 5000
    
	# putting the largest first at the odd site
	# and promising the final one  is smaller than the largest one or equal it
    while i * 2 + 1 < len(nums):
        while count[c] == 0:
            c -= 1
        nums[i * 2 + 1] = c
        count[c] -= 1
        i += 1
    
	# putting the largest in the remaider at the even site from largest to smallest.
	# If the last one's value at the odd site is equal the largest value in the remainder.
    # After putting, it is impossible if the value or number are adjust.
    # Because, first, the number of each value is not over len(nums)//2. If the number over len(nums)//2, that mean the output is invalid.
    # Second, if this value which is largest in the remainder has putted at the odd sites, the valid lenght becomes v = len(nums) - 2 * n if len(nums) is odd or len(nums) - 2 * n - 1 if len(nums) is even(n is the number of the value has putted) 
    # the range of the value most possibly covering is not over (len(nums)//2 - n) * 2 - 1, so the first of the value put at odd site is not adjust with the value, if the odd site is larger than r = (len(nums)//2 - n) * 2 - 1
    # It is impossible the value could adjust by the way because r < v such [2,3,1,2]
    i = 0
    while i * 2 < len(nums):
        while count[c] == 0:
            c -= 1
        nums[i * 2] = c
        count[c] -= 1
        i += 1
