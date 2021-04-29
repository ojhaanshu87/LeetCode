'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
'''

class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False
        left_ptr, right_ptr = 0, len(arr) - 1
        while (left_ptr < right_ptr):
            if arr[left_ptr] < arr[left_ptr + 1]:
                left_ptr += 1
            elif arr[right_ptr - 1] > arr[right_ptr]:
                right_ptr -= 1
            else:
                break
        if left_ptr == right_ptr and left_ptr !=0 and right_ptr != len(arr) - 1:
            return True
        else:
            return False
