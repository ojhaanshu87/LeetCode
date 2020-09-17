```
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

```

#Time Complexity: O(n)
# Space Complexity: 0(n+m+k)

class Solution(object):
    def isIsomorphic(self, s, t):
        if len(set(s)) != len(set(t)):
            return False
        res = {}
        for elem in range(0, len(s)):
            if s[elem] not in res:
                res[s[elem]] = t[elem]
            elif res[s[elem]] != t[elem]:
                return False
        return True
