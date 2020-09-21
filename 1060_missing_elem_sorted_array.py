```
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
```

#Linear Search O(N)  Space complexity O(1)

          #Implement missing(idx) function that returns how many numbers are missing until array element with index idx. Function returns nums[idx] - nums[0] - idx.

          #Find an index such that missing(idx - 1) < k <= missing(idx) by a linear search.

          #Return kth smallest nums[idx - 1] + k - missing(idx - 1).

#[4,7,9,10]
# 7 - 4 - 1 = 2
# 9 - 4 - 2 = 3
# nums_missing count between 0 & i is (nums[i] - nums[0] - i)

class Solution(object):    
    def missingElement(self, nums, k):
        missing_count = lambda idx : nums[idx] - nums[0] - idx
        #If kth missing number is larger than the last element of the array
        if missing_count(len(nums) - 1) < k:
            return nums[-1] + k - missing_count(len(nums) - 1)
        idx = 1
        #find idx such that missing(idx - 1) < k <= missing(idx)
        while missing_count(idx) < k:
            idx += 1
        #kth missing number is GT nums[idx - 1] and LT nums[idx]
        return nums[idx - 1] + k - missing_count(idx - 1)
 
 #Binary Search O(log N) Space complexity O(1)
 
 ```
 Algorithm
            Implement missing(idx) function that returns how many numbers are missing until array element with index idx. Function returns nums[idx] - nums[0] - idx.
            Find an index such that missing(idx - 1) < k <= missing(idx) by a binary search.
            return kth smallest nums[idx - 1] + k - missing(idx - 1). ```
 
 class Solution(object):    
    def missingElement(self, nums, k):
        missing_count = lambda idx : nums[idx] - nums[0] - idx
        #If kth missing number is larger than the last element of the array
        if missing_count(len(nums) - 1) < k:
            return nums[-1] + k - missing_count(len(nums) - 1)
        
        start, end = 0, len(nums) - 1
        #find left = right index such that missing(left - 1) < k <= missing(left)
        while start != end:
            mid = start + (end - start) // 2
            if missing_count(mid) < k:
                start = mid + 1
            else:
                end = mid
        #kth missing number is greater than nums[left - 1] and less than nums[left]
        return nums[start - 1] + k - missing_count(start - 1)


