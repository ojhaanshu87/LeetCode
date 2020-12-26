'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
'''

#TC O(N) & Space (O(1))

'''
Algorithm

Initialize left pointer to 0 and right pointer to size-1
While left<right, do:
        If height[left] is smaller than height[right]
                If height[left] >=left_max, update left_max
                Else add left_max−height[left] to ans
                Add 1 to left.
       
       else
            If height[right] >=right_max, update right_max
            Else add right_max−height[right] to ans
            Add 1 to right.    
'''

class Solution(object):
    def trap(self, height):
        ans = 0
        low, high, left_max, right_max = 0, len(height) - 1, 0, 0
        if len(height) <= 2:
            return 0
        while low <= high:
            left_max = max(left_max, height[low])
            right_max = max(right_max, height[high])
            if left_max < right_max:
                ans += left_max - height[low]
                low += 1
            else:
                ans += right_max - height[high]
                high -= 1
        return ans
                    
                    
