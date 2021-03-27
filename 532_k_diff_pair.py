'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

Example 1:
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Example 4:
Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
Output: 2

Example 5:
Input: nums = [-1,-2,-3], k = 1
Output: 2
'''

# Sorting and Binary Search TC (O(NLOGN)) Space O(N)

class Solution(object):
    def findPairs(self, nums, k):
        # Binary Search after Sort
        nums.sort()
        res = 0
        for elem in range(len(nums)):
            if elem > 0:
                if nums[elem] == nums[elem - 1]:
                    continue
            low, high = elem + 1, len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == nums[elem] + k:
                    res += 1
                    break
                elif nums[mid] < nums[elem] + k:
                    low = mid + 1
                else:
                    high = mid - 1
        return res
      
# Hash Map O(N) time and space

# Approach 
  # A) create map with key as num[idx] and value as count
  # B) iterate over key and search k > 0 and k + num[idx] in map.keys() if found increment counter
  # C) check for k == 0 and map[value] > 1 and increment the count (for if k is negative or zero)
 
class Solution(object):
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        res = 0
        temp_map = collections.Counter(nums)
        for key in temp_map.iterkeys():
            if k > 0 and key + k in temp_map:
                res += 1
            elif k == 0 and temp_map[key] > 1:
                res += 1
        return res
