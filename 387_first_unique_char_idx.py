```
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
```

class Solution(object):
    def firstUniqChar(self, s):
        res = {}
        for elem in s:
            if elem in res:
                res[elem] += 1
            else:
                res[elem] = 1
        
        for idx, char in enumerate(s):
            if res[char] == 1:
                return idx
        return -1
