```
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.

```

class Solution(object):
    def reverse(self, s, start, end):
        while(start < end):
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
    
    def reverse_word_driver(self, s):
        start, end = 0, 0
        while start < len(s):
            while end < len(s) and s[end] != ' ':
                end += 1
            self.reverse(s, start, end -1)
            start = end + 1
            end += 1
            
    def remove_spaces(self, s):
        start, end, result = 0, len(s) - 1, []
        #remove leading space
        while start <= end and s[start] == ' ':
            start += 1
        #remove trainling space
        while start <= end and s[end] == ' ':
            end -= 1
        
        #reduce multiple spaces
        while start <= end:
            if s[start] != ' ':
                result.append(s[start])
            elif result[-1] != ' ':
                result.append(s[start])
            start += 1
        return result
        
    def reverseWords(self, s):
        after_remove_space = self.remove_spaces(s)
        self.reverse(after_remove_space, 0, len(after_remove_space) - 1)
        self.reverse_word_driver(after_remove_space)
        return ''.join(after_remove_space)
