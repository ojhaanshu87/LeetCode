'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
 
'''

class Solution(object):
    def findWords(self, words):
        res = []
        for elem in words:
            first_row, second_row, third_row = 0, 0, 0
            for token in elem:
                if token.lower() in "qwertyuiop":
                    first_row += 1
                if token.lower() in "asdfghjkl":
                    second_row += 1
                if token.lower() in "zxcvbnm":
                    third_row += 1
            if first_row == len(elem) or second_row == len(elem) or third_row == len(elem):
                res.append(elem)
        return res
