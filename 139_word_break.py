"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

#METHOD1 -> DFS with Memorization TC (O(n) with memoization, O(2^n) without)

"""
The basic idea is to use DFS to remove any possible word from the word dictionary that exists in the begining of the string, 
and then the remainder of each resultant string will have the same procedure recursively applied to it.

At the end of the day, if there's one recusrion that returns True, when a input string "" is found, then there exists a possible wordBreak.

Used a memo table to store previously seen postfix strings, so we don't have to go down the route of calculating already tabulated words.
"""

class Solution(object):
    def dfs(self, string, wordDict, found):
        if string == "":
            return True
        if string in found:
            return found[string]
        found_split = False
        for word in wordDict:
            if string .startswith(word):
                found_split = found_split or self.dfs(string[len(word):], wordDict, found)
            if found_split == True:
                return True
        found[string] = found_split
        return found_split
    
    def wordBreak(self, s, wordDict):
        found = {}
        return self.dfs(s, wordDict, found)
 
#METHOD2 -> Trie With Memorization

class Solution:
    def __init__(self):
        self.trie = [{}]
		# memoization cache
        self.found = {}

    def get_prefixes(self, word):
        prefixes = []
        current_word = []

        current = self.trie[0]
        for c in word:
            if "$" in current:
                prefixes.append(''.join(current_word))
            if c in current:
                current_word.append(c)
                current = self.trie[current[c]]
            else:
                break

        if "$" in current:
            prefixes.append(''.join(current_word))      

        return prefixes

    def make_trie(self, wordDict):
        
        for word in wordDict:
            current = self.trie[0]
            for c in word + "$":
                if c in current:
                    current = self.trie[current[c]]
                else:
                    # make new node
                    self.trie.append({})
                    current[c] = len(self.trie) - 1
                    current = self.trie[current[c]]

    def dfs(self, suffix):
        if suffix in self.found:
            return False
        
        if not suffix:
            return True

        for p in self.get_prefixes(suffix):
            if self.dfs(suffix[len(p):]):
                return True
            
        self.found[suffix] = False

        return False
    
    def wordBreak(self, s, wordDict):
        self.make_trie(wordDict)

        return self.dfs(s)  
