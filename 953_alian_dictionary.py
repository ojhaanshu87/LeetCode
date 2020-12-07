"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

#ALGORITHM TC (O(length of Words)) Space O(1)

"""
Let's check whether all adjacent words a and b have a <= b.

To check whether a <= b for two adjacent words a and b, we can find their first difference.
For example, "applying" and "apples" have a first difference of y vs e. After, we compare these characters to the index in order.

Care must be taken to deal with the blank character effectively. If for example, we are comparing "app" to "apply", this is a first difference of (null) vs "l".
"""

class Solution(object):
    def isAlienSorted(self, words, order):
        store_data = {char:idx for idx, char in enumerate(order)}
        for elem in range(len(words) - 1):
            w1 = words[elem]
            w2 = words[elem + 1]
            for elem1 in range(min(len(w1), len(w2))):
                if store_data[w1[elem1]] < store_data[w2[elem1]]: break
                elif w1[elem1] == w2[elem1]: continue
                else: return False
            else:
                if len(w1) > len(w2): return False
        return True
                
        
