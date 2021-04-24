'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.

Example 1:
Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Example 2:
Input: nums = [4,14,4]
Output: 4
'''

class Solution(object):
    def totalHammingDistance(self, nums):
        count, result = collections.defaultdict(int), 0
        
        for elem in nums:
            for position in range(31):
                if elem & 1:
                    count[position] += 1
                elem >>= 1
                if not elem:
                    break
                    
        for position in range(31):
            result += count[position] * (len(nums) - count[position])
        return result