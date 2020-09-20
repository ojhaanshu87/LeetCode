```
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

```

class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        start, end = 0, len(nums) - 1
        
        #if rightmost elem GT left most means no rotation happen
        if nums[end] > nums[0]:
            return nums[0]
        
        while start <= end:
            mid = start = (end - start) // 2
            #if mid elem greater than next then mid + 1 is smallest
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            #if mid is less than previous then mid is smallest
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            #if mid elem GT 0th elem then smallest at somewhere in right else somewhere in left
            if nums[mid] > nums[0]:
                start = mid + 1
            else:
                end = mid - 1
        
