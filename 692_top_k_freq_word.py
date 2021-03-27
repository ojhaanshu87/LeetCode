'''
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
    
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
    
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
'''

# Sorting Time (O(NLOGN)) Space O(N) where N is len(word)

class Solution(object):
    def topKFrequent(self, words, k):
        res = {}
        for elem in words:
            if elem in res:
                res[elem] += 1
            else:
                res[elem] = 1
        candidates = res.keys()
        candidates.sort(key = lambda w: (-res[w], w))
        return candidates[:k]

# Heap using heapq.heapify time O(N + kLOGN))  and space is O(N)

class Solution(object):
    def topKFrequent(self, words, k):
        temp, res = {}, []
        for elem in words:
            if elem in temp:
                temp[elem] += 1
            else:
                temp[elem] = 1
        max_heap = [(-freq, word) for word, freq in temp.items()]
        heapq.heapify(max_heap)
        for elem in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res
