'''
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''

# BINARY SEARCH
class Solution(object):
    def intersect(self, nums1, nums2):
        #Binary Search
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
        return ans
      
# 2 Pointers and Sorting
class Solution(object):
    def intersect(self, nums1, nums2):
        # 2 Pointers Sorting
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0 
        n, m = len(nums1), len(nums2)
        ans = list()
        while p1 < n and p2 < m:
            if nums1[p1]==nums2[p2]:
                ans.append(nums1[p1])
                p1+=1
                p2+=1
            elif nums1[p1]<nums2[p2]: p1+=1
            else: p2+=1
        return ans
    
# Hash Map
class Solution(object):
    def intersect(self, nums1, nums2):
        res, temp = [], collections.Counter(nums1)
        for elem in range(len(nums2)):
            if nums2[elem] in temp:
                res.append(nums2[elem])
                temp[nums2[elem]] -= 1
                if temp[nums2[elem]] == 0:
                    del temp[nums2[elem]]
        return res
