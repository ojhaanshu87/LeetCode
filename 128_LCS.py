'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
'''

'''
Algorithm

This optimized algorithm contains only two changes from the brute force approach: 
the numbers are stored in a HashSet (or Set, in Python) to allow O(1)O(1) lookups, and we only attempt to build sequences
from numbers that are not already part of a longer sequence. This is accomplished by first ensuring that the number that would
immediately precede the current number in a sequence is not present, as that number would necessarily be part of a longer sequence.
'''

# # hash set method TC(O(N)) and space (O(N))
class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        result = 0
        for num in num_set:
            if num-1 in num_set:
                continue
            temp = 1
            while num + temp in num_set:
                temp += 1
            result = max(temp, result)
        return result
