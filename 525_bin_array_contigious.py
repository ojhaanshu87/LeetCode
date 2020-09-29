```
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

```

#ALGORITHM

#WE INITIALISE A DICTIONARY WHICH KEEPS TRACK OF ALL 0'S AND 1'S ENCOUNTERED USING count VARIABLE, WHICH INCREMENTS IF 1 IS ENCOUNTERED AND DECREMENTS IF 0 IS ENCOUNTERED.
#WE STORE (COUNT VALUE: INDEX) PAIRS IN A DICTIONARY.
#IF A SAME VALUE IS FOUND IN DICTIONARY AGAIN, IT SIMPLY MEANS THAT BETWEEN THOSE TWO INDICES, THE NUMBER OF 0'S AND 1'S ARE SAME.

class Solution(object):
    def findMaxLength(self, nums):
        if not nums or len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[0]==nums[1]:
                return 0
            return 2
        
        if nums.count(1)==nums.count(0):
            return len(nums)
        
        dic = {0:-1}
        maxlen = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count in dic:
                maxlen = max(maxlen,i-dic[count])
            else:
                dic[count] = i
        return maxlen
                
        
