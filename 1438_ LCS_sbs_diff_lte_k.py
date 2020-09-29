```
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any
two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9

```

#O(N) Solution using Deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        min_q = deque()
        max_q = deque()
        i = 0
        for item in nums:
            while(len(min_q)>0 and min_q[-1]>item):
                min_q.pop()

            while(len(max_q)>0 and max_q[-1]<item):
                max_q.pop()

            min_q.append(item)
            max_q.append(item)


            if max_q[0] - min_q[0] > limit:
                if min_q[0] == nums[i]:
                    min_q.popleft()

                if max_q[0] == nums[i]:
                    max_q.popleft()

                i+=1


        return len(nums)-i
        
