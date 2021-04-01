'''
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:
Input: num = "69"
Output: true

Example 2:
Input: num = "88"
Output: true

Example 3:
Input: num = "962"
Output: false

Example 4:
Input: num = "1"
Output: true
'''

# String Builder Approach O(N) TC and O(1) Space

class Solution(object):
    def isStrobogrammatic(self, num):
        res = []
        for char in reversed(num):
            if char in ['0', '1', '8']:
                res.append(char)
            elif char == '6':
                res.append('9')
            elif char == '9':
                res.append('6')
            else:
                return False
        temp = ''.join(res)
        return temp == num
      
# Hash Map O(N) TC and O(N) Space

class Solution(object):
    def isStrobogrammatic(self, num):
        res, map_is_true = [], {'0':'0', '1': '1', '8': '8', '6': '9', '9': '6'}
        for char in reversed(num):
            if char not in map_is_true:
                return False
            res.append(map_is_true[char])
        temp = ''.join(res)
        print temp
        print num
        return temp == num
