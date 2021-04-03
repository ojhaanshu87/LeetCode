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
    
    
# MEthod 2 O(NLOGN) TC sorting and Constant Space (O(1))

class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        nums1.sort()
        nums2.sort()
        print nums1, nums2
        ptr_n1, ptr_n2 = 0, 0
        while ptr_n1 < len(nums1) and ptr_n2 < len(nums2):
            if nums1[ptr_n1] < nums2[ptr_n2]:
                ptr_n1 += 1
            elif nums1[ptr_n1] > nums2[ptr_n2]:
                ptr_n2 += 1
            else:
                if nums1[ptr_n1] not in res:
                    res.append(nums1[ptr_n1])
                ptr_n1 += 1
                ptr_n2 += 1
        return res

# What if Duplicates allowed in result
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        ptr1, ptr2, res = 0, 0, []
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1
            else:
                res.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
        return res
