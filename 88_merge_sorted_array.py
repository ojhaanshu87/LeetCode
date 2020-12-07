"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""

#ALGORITHM -> TC (O(N+M)) Space (O(1))

"""
Two pointers / Start from the end:
 if we start to overwrite nums1 from the end, where there is no information yet? Then no additional space is needed.
 The set pointer here is used to track the position of an added element.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ptr_num1, ptr_num2, set_ptr_to_track_pos_added_elem = m - 1, n - 1, m + n - 1
        while ptr_num1 >= 0 and ptr_num2 >= 0:
            if nums1[ptr_num1] < nums2[ptr_num2]:
                nums1[set_ptr_to_track_pos_added_elem] = nums2[ptr_num2]
                ptr_num2 -= 1
            else:
                nums1[set_ptr_to_track_pos_added_elem] = nums1[ptr_num1]
                ptr_num1 -= 1
            set_ptr_to_track_pos_added_elem -= 1
        #add missing elems
        nums1[:ptr_num2 + 1] = nums2[:ptr_num2 + 1]
