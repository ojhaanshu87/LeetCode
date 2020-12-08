"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""

#Algorithm

#Initiate three pointers p1, p2, p3, and place them at the beginning of arr1, arr2, arr3 by initializing them to 0;
#while they are within the boundaries:
  #if arr1[p1] == arr2[p2] && arr2[p2] == arr3[p3], we should store it because it appears three times in arr1, arr2, and arr3;
  #else
    #if arr1[p1] < arr2[p2], move the smaller one, i.e., p1;
    #else if arr2[p2] < arr3[p3], move the smaller one, i.e., p2;
    #if neither of the above conditions is met, it means arr1[p1] >= arr2[p2] && arr2[p2] >= arr3[p3], therefore move p3.

class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        res = []
        ptr1, ptr2, ptr3 = 0, 0, 0
        while ptr1 < len(arr1) and ptr2 < len(arr2) and ptr3 < len(arr3):
            if arr1[ptr1] == arr2[ptr2] == arr3[ptr3]:
                res.append(arr1[ptr1])
                ptr1 += 1
                ptr2 += 1
                ptr3 += 1
            else:
                if arr1[ptr1] < arr2[ptr2]:
                    ptr1 += 1
                elif arr2[ptr2] < arr3[ptr3]:
                    ptr2 += 1
                else:
                    ptr3 += 1
        return res
