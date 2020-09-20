```
Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?

```

class Solution(object):
    def reverse(self, s, start, end):
        while(start < end):
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
    def reverse_words_driver(self, s):
        start, end = 0, 0
        while(start < len(s)):
            #go for end of word
            while end < len(s) and s[end] != ' ':
                end += 1
            #reverse word
            self.reverse(s, start, end - 1)
            #move to next word
            start = end + 1
            end += 1
            
    def reverseWords(self, s):
        self.reverse(s, 0, len(s) - 1)
        self.reverse_words_driver(s)
        
