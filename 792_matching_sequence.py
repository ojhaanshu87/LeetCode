'''
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order
of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 
Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
'''

# ALGORITHM (O(N)) TC and (O(N)) Space
  #We first count the occurences of a word in words array and store in a final_count dictionary.
  #Then we iterate throught the set(words).
  #In the for loop we use iter which creates an iterator and will give us whether a letter of a word is present or not.
  #If it is present we increment the value of i by the number of its occurences that we have stored in the final_count dictionary.

class Solution(object):
    def numMatchingSubseq(self, s, words):
        res = 0
        final_words = collections.Counter(words)
        for word in set(words):
            iter_var = iter(s)
            if all(letter in iter_var for letter in word):
                res += final_words[word]
        return res

# Method 2 

class Solution(object):
    def numMatchingSubseq(self, s, words):
        count = 0
        map_temp = collections.defaultdict(list)
        for word in words:
            map_temp[word[0]].append(word)
        for char in s:
            temp = map_temp[char]
            del map_temp[char]
            for word in temp:
                if len(word) == 1:
                    count += 1
                    continue
                map_temp[word[1]].append(word[1:])
        return count
