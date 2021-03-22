'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates). 
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order. 

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]
'''

class Solution(object):
    def commonChars(self, A):
        res = set(A[0])
        if len(A) < 2:
            return res
        for token in A:
            res = res.intersection(set(token))
        temp = {}
        for elem in res:
            temp[elem] = min([token.count(elem) for token in A])
            
        final = []
        for key, value in temp.iteritems():
            final += [key] * value
        return final
