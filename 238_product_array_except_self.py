```
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
```
#LOG APPROACH O(n) and O(1)
#x = a * b * c * d
#log(x) = log(a * b * c * d)
#log(x) = log(a) + log(b) + log(c) + log(d)
#x = antilog(log(a) + log(b) + log(c) + log(d))

class Solution(object):
    def productExceptSelf(self, nums):
        EPS = 1e-9
        total, res = 0 , []
        for elem in range(0, len(nums)):
            total += math.log10(nums[elem])
        for elem in range(0, len(nums)):
            res.append(int((EPS + pow(10.00, total - math.log10(nums[elem])))))
        return res
        
# pow() Approach
#Traverse the array and find the product of all the elements in the array. Store the product in a variable.
#Then again traverse the array and find the product of all the elements except that number by using the formula (product * pow(a[i], -1))

class Solution(object):
    def productExceptSelf(self, nums):
        total, res = 1 , []
        if all(v == 0 for v in nums):
            for elem in range(0, len(nums)):
                res.append(0) 
            return res
        
        else:
            for elem in range(0, len(nums)):
                total *= nums[elem]
            for elem in range(0, len(nums)):
                res.append(int(total*(nums[elem]**-1)))
            return res

# Another Approach Algorithm

#Initialize the empty answer array where for a given index i, answer[i] would contain the product of all the numbers to the left of i.
# Construct the answer array the same way we constructed the L array in the previous approach. 
# These two algorithms are exactly the same except that we are trying to save up on space
# The only change in this approach is that we don't explicitly build the R array from before.
# Instead, we simply use a variable to keep track of the running product of elements to the right and we keep updating the answer
#array by doing answer[i] = answer[i] * Ranswer[i]=answer[i]∗R. For a given index i, answer[i] contains the product of all the elements to the left and R would contain
#product of all the elements to the right. We then update R as R = R * nums[i]R=R∗nums[i]


class Solution(object):
    def productExceptSelf(self, nums):
        # The answer array to be returned
        answer = [0]*len(nums)
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, len(nums)):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(len(nums))):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
        
        
