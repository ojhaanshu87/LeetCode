'''
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
'''

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0 or len(s) == 0:
            return 0
        temp = {}
        fast, slow, res = 0, 0, 0
        while fast < len(s):
            fast_char = s[fast]
            temp[fast_char] = temp.get(fast_char, 0) + 1

            while (len(temp) > k):
                slow_char = s[slow]
                if temp[slow_char] == 1:
                    del temp[slow_char]
                elif temp[slow_char] >1:
                    temp[slow_char] = temp[slow_char]-1
                slow += 1
			
			# when we get here we can be sure that we have atmost k chars in the temp
            res = max(res, fast - slow + 1)
            fast += 1
        return res
        
        
