``` 
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1
 

Constraints:

2 <= n <= 3 * 104
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

```

#ALGORITHM -> O(N) time and O(1) Space

#In phase 1, fast = nums[nums[fast]] is twice as fast as slow = nums[slow].
#Since the hare goes fast, it would be the first one who enters the cycle and starts to run around the cycle. 
#At some point, the tortoise enters the cycle as well, and since it's moving slower the hare catches the tortoise up at some intersection point. 
#Now phase 1 is over, and the tortoise has lost.

#In phase 2, we give the tortoise a second chance by slowing down the hare, so that it now moves with the speed of tortoise: tortoise = nums[tortoise], hare = nums[hare]. 
#The tortoise is back at the starting position, and the hare starts from the intersection point.


class Solution(object):
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
        

