```
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
```


class Solution(object):
    def generate_hash_key(self, string):
        bit_map = [0] * 26
        for char in string:
            bit_map[ord(char) - ord('a')] += 1
        return str(bit_map)
    
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        #METHOD 3 O(1->26) space complexity 
        return self.generate_hash_key(s) == self.generate_hash_key(t)
        
        #METHOD 2
        # return sorted(s) == sorted(t)
    
        #METHOD 1
        # if len(s) != len(t):
        #     return False
        # dict_s, dict_t = {}, {}
        # for elem in s:
        #     if elem in dict_s:
        #         dict_s[elem] += 1
        #     else:
        #         dict_s[elem] = 1
        # for elem in t:
        #     if elem in dict_t:
        #         dict_t[elem] += 1
        #     else:
        #         dict_t[elem] = 1
        # if dict_s == dict_t:
        #     return True
        # else:
        #     return False
        
