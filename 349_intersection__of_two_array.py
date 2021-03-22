'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]


Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        if n < m:
            nums1, nums2 = nums2, nums1
            n, m = m, n
        nums1.sort()
        ans = []
        for num,freq in collections.Counter(nums2).items():
            first = bisect_left(nums1, num)
            second = bisect_right(nums1, num)
            if first != -1:
                for _ in range(min(second-first,freq)):
                    ans.append(num)
        # if remove set from below then return all elem irrespective of duplications 
        return set(ans)
