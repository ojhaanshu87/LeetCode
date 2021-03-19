'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
'''

class Solution(object):
    def reverseVowels(self, s):
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            if s[p1] in vowel and s[p2] in vowel:
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1
            elif s[p2] in vowel:
                p1 += 1
            elif s[p1] in vowel:
                p2 -= 1
            else:
                p1 += 1
                p2 -= 1
        return ''.join(s)
