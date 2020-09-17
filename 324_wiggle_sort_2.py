```
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

```

#USE SORTING (direct mechansim) O(nlogn)

# class Solution(object):
#     def wiggleSort(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         N=len(nums)
#         if N<2: return nums
        
#         nums.sort(reverse=True)        
#         nums[::2],nums[1::2]=nums[N/2:],nums[:N/2]

#ALGORITHM AND SOLUTION O(N) 

```
Basic idea: we find median value, put numbers bigger than median into odd index, smaller than median into even index.
Naive solution:

Sort the array to find median in O(nlgn) time + O(1) space
Move odd and even index numbers into temp array and move them back to the original array with new index. Taking O(n) time + O(n) space.
Total: O(nlgn) time + O(n) space
In order to achieve O(n) time + O(1) space, we need to answer two questions:

How to find median in O(n)+O(1)
How to re-order the odd-even indexes "in-place" using O(1) memory.
Three knowledge pre-requisitions:

Quick select to find median in O(n) time on average, O(n^2) in worst case. Taking O(1) memory.
"Median of medians" alogrithm to improve quick select, making the time complexity "deterministic O(n)" rather than "average O(n)".
Virtual indexing technology to achieve in-place wiggle sort based on median value found above.
There is "median of medians + quick select" methods provided out of the box in all languages. You have to write it yourself.
This problem deserve to be of "Hard" difficulty rather than "Medium" for the O(n)+O(1) solution, considering so many technologies involved.

Virtual index:
This is actually a "Three color Sort" problem. Imagine scanning the nums this way: "1,3,5,7,9, ... 0,2,4,6,8,10...". During the scan, when you see a big number, put it to "left", a small number, put it to "right", in the end, you will see all big numbers on left, all small numbers on right, and all median numbers in the middle.
But wait, here "left" and "right" are actually the left and right of "1,3,5,7...0,2,4,6,8,..." indexes, not the left and right of "0,1,2,3,4,5...", because you are scanning in "1,3,5,7...0,2,4,6,8,..." order. So what you actually see is all big numbers on odd index, all small numbers on even index, all median numbers distributed on the left and right side of the array. And this kind of distribution is guaranteed to be wiggled sorted.

Code:
I use random pivot for quick select rather than "median of medians", which is much easier to implement and has average O(n) for all kind of input pattern.
Please be noted that you cannot use recursion in the fast select part, otherwise the space complexity won't be real O(1).
```

import random
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        def nsmallest(nums,n):            
            start,end=0,len(nums)-1
            while True:
                pivot=nums[random.randint(start,end)]
                i,j,k=start,end,start
                while k<=j:
                    if nums[k]<pivot:
                        nums[i],nums[k]=nums[k],nums[i]
                        i+=1
                        k+=1
                    elif nums[k]>pivot:
                        nums[j],nums[k]=nums[k],nums[j]
                        j-=1
                    else:
                        k+=1
                if i<=n-1<=j:
                    return pivot
                elif n-1<i:
                    end=i-1
                else:
                    start=i+1
        n=len(nums)
        mid=nsmallest(nums,(n+1)//2)
        mapIdx=lambda i:(1+2*i)%(n|1)
        i,j,k=0,n-1,0
        while k<=j:
            if nums[mapIdx(k)]>mid:
                nums[mapIdx(k)],nums[mapIdx(i)]=nums[mapIdx(i)],nums[mapIdx(k)]
                i+=1
                k+=1
            elif nums[mapIdx(k)]<mid:
                nums[mapIdx(k)],nums[mapIdx(j)]=nums[mapIdx(j)],nums[mapIdx(k)]
                j-=1
            else:
                k+=1
