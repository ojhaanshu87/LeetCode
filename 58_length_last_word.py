```
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word
(last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
```

class Solution(object):
    def lengthOfLastWord(self, s):
        len_s, res = len(s), 0       
        while len_s > 0:
            len_s -= 1
            # we're in the middle of the last word
            if s[len_s] != ' ':
                res += 1
            # here is the end of last word
            elif res > 0:
                return res

        return res
