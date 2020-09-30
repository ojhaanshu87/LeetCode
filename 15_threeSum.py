```
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
```

# The algorithm is similar to the hashset approach above. We just need to add few optimizations so that it works efficiently for repeated values:

# Use another hashset dups to skip duplicates in the outer loop.
# Without this optimization, the submission will time out for the test case with 3,000 zeroes. This case is handled naturally when the array is sorted.
# Instead of re-populating a hashset every time in the inner loop, we can use a hashmap and populate it once.
#Values in the hashmap will indicate whether we have encountered that element in the current iteration.
#When we process nums[j] in the inner loop, we set its hashmap value to i. This indicates that we can now use nums[j] as a complement for nums[i].
# This is more like a trick to compensate for container overheads.
#The effect varies by language, e.g. for C++ it cuts the runtime in half. Without this trick the submission may time out.

# Time Complexity: O(n 
# 2
#  ). We have outer and inner loops, each going through nn elements.

# While the asymptotic complexity is the same, this algorithm is noticeably slower than the previous approach. Lookups in a hashset, though requiring a constant time, are expensive compared to the direct memory access.

# Space Complexity: \mathcal{O}(n)O(n) for the hashset/hashmap.

# For the purpose of complexity analysis, we ignore the memory required for the output. However, in this approach we also store output in the hashset for deduplication. In the worst case, there could be \mathcal{O}(n^2)O(n 
# 2
#  ) triplets in the output, like for this example: [-k, -k + 1, ..., -1, 0, 1, ... k - 1, k]. Adding a new number to this sequence will produce n / 3 new triplets.


class Solution(object):
    def threeSum(self, nums):
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res
       
        
