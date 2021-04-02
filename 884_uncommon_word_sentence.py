'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order

Example 1:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: A = "apple apple", B = "banana"
Output: ["banana"]
'''

# Join to sentence with space. Create map with word and frequency, if frequency == 1 append to result array and finally return array. 

class Solution(object):
    def uncommonFromSentences(self, A, B):
        res = []
        temp = A + " " + B
        count_temp = collections.Counter(temp.split(" "))
        for word, freq in count_temp.iteritems():
            if freq == 1:
                res.append(word)
        return res
