```
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]

```

class Solution(object):
    def wiggleSort(self, nums):
        for elem in range(1, len(nums), 2):
            if nums[elem] < nums[elem-1]:
                nums[elem], nums[elem-1] =  nums[elem-1], nums[elem]
            if elem + 1 <= len(nums) - 1 and nums[elem] < nums[elem+1]:
                nums[elem], nums[elem+1]  = nums[elem+1], nums[elem]
        return nums
