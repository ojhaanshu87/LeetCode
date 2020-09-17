```
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

```

class Solution(object):
    def decodeString(self, s):
        result = []
        for elem in s:
            if elem == ']':
				# go back until the opening and remember the string
                substring = []
                while (result[-1] != '['):
                    substring.append(result.pop())
                result.pop()
                
				# figure out how many times to add it
                n = 0
                decimal = 0
                while(len(result) > 0 and result[-1].isnumeric()):
                    n = n + 10 ** decimal * int(result.pop())
                    decimal = decimal + 1
                    
				# add the string n times; remember that substring is in the reverse order
                for i in range(0, n):
                    for j in range(0, len(substring)):
                        result.append(substring[len(substring)-1-j])
            else:
                result.append(elem)
        return ''.join(result)
