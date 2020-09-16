```
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
```

class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = 0
        self.is_leaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        head = self.root
        for i in range(len(word)):
            if word[i] in head.child:
                head = head.child[word[i]]
                head.count += 1
            else:
                head.child[word[i]] = TrieNode()
                head = head.child[word[i]]
                head.count = 1
        
        head.is_leaf = True


class Solution(object):
    def longestCommonPrefix(self, strs):
        global ans
        trie = Trie()
        count = 0
        for word in strs:
            trie.insert(word)
        for word in strs:
            head = trie.root
            tmp = ""
            for elem in word:
                if head.child[elem].count == len(strs):
                    tmp += elem
                head = head.child[elem]
            ans = tmp
                    
        return ans
        
