'''
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''

class Solution(object):
    def groupStrings(self, strings):
        res = collections.defaultdict(list)
        for s in strings:
            code = ''
            for i in range(1, len(s)):
                x = ord(s[i]) - ord(s[i-1])
                if x < 0:
                    x += 26
                code += str(x) 
            res[code] += [s]
        return res.values()
        
