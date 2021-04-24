'''
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
 
'''
 # # O(N) TC and O(1) Space

class Solution(object):
    def findSpecialInteger(self, arr):
        prev, curr = 0, 0
        limit = len(arr) // 4 + 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                prev = curr
                curr = i
            else:
                prev = curr

            if curr - prev >= limit:
                return arr[i - 1]

        return arr[-1]
        
