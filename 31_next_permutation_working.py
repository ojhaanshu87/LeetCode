"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.
 
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:
Input: nums = [1]
Output: [1]
 
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

# Start from the back of the numbers and look for the first time the number decreases.
#At this point you know you need to swap a number. The number you need to swap is the number greater than the decremented number
#(ex: 1235764 would mean 6 should swap with 5).
#Then, simply sort the remaining tail of the number because now you know that you've increased a leading number which
#guarantees the number is larger than the previous number.


class Solution(object):
    def nextPermutation(self, nums):
        nums = [int(elem) for elem in nums]
        test_list1 = nums[:] 
        test_list1.sort(reverse = True) 
        if (test_list1 == nums): 
            return "Not Possible"
        else:
            num_count = len(nums) - 1
            dec = False
            while num_count > 0 and not dec:
                if nums[num_count - 1] < nums[num_count]:
                    swap_i = num_count
                    for j in range(num_count, len(nums)):
                        if nums[j] < nums[swap_i] and nums[j] > nums[num_count - 1]:
                            swap_i = j
                    nums[num_count - 1], nums[swap_i] = nums[swap_i], nums[num_count - 1]
                    dec = True
                else:
                    num_count -= 1
            nums[num_count:] = sorted(nums[num_count:])
            return ''.join(str(elem) for elem in nums)
        
print Solution().nextPermutation("218765")
