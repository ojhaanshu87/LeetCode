"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

"""
APPROACH  The time complexity is O(n^2) and the space complexity is O(2^n) (n is the size of nums)

The idea is as we examine the numbers in nums one by one, we keep all the sums that can be formed using the previous numbers in a Set.
At each step we can either take the current number or not (like 0/1 knapsack problem). 
So if the target ( target = sum(nums) / 2) minus the current number is already in the Set, then we return True.
Otherwise, the new sums that are formed using the current number is simply all the old sums in Set plus the current number.
We add these new sums to Set if they are smaller than target (remember, all the numbers are positive so if the sum exceeds target, it's not useful anymore).

One small thing to notice is that we need to copy the Set to Set_old before we add new sums to Set,
because we don't want the size of the Set to be changed during the iteration.
"""
class Solution(object):
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        Set = set([0])
        for i in nums:
            if target - i in Set:
                return True
            Set_old = Set.copy()
            for Sum in Set_old:
                if Sum + i < target:
                    Set.add(Sum + i)
        return False
                
        
