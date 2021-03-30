```
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
```

#Categorize by Sorted String

class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

#Categorize by Count

class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

# Hashmap and Sorting 

'''
We create a dictionary and for each word in the input array, we add a key to the dictionary if the sorted version of the word doesn't already exist in the list of keys.
The key then becomes the sorted version of the word, and the value for the key is an array that stores each anagram of the key.
i.e. for every next word that is an anagram, we would sort the word, find the key that is equal to the sorted form,
and add the original word to the list of values for the key.
At the end of it, we just add every value in the dictionary to the final array.
'''

class Solution(object):
    def groupAnagrams(self, strs):
        temp, res = {}, []
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in temp:
                temp[sortedWord] = [word]
            else:
                temp[sortedWord].append(word)       
        for value in temp.values():
            res.append(value)
        return res
