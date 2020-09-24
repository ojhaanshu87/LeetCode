```
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]

```

class Solution(object):
    def sumZero(self, n):
        res = [-1,1] if n % 2 == 0 else [0]
        num = 2
        while len(res) < n:
            res.append(num)
            res.append(-num)
            num +=1
        return res
