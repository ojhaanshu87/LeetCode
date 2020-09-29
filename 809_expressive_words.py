```
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo",
we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the
following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.
Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two
extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 

Constraints:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters

```

#ALGORITHM


For some word, write the head character of every group, and the count of that group. For example, for "abbcccddddaaaaa", we'll write the "key" of "abcda", 
and the "count" [1,2,3,4,5].

Let's see if a word is stretchy. Evidently, it needs to have the same key as S.

Now, let's say we have individual counts c1 = S.count[i] and c2 = word.count[i].

If c1 < c2, then we can't make the ith group of word equal to the ith word of S by adding characters.

If c1 >= 3, then we can add letters to the ith group of word to match the ith group of S, as the latter is extended.

Else, if c1 < 3, then we must have c2 == c1 for the ith groups of word and S to match.

class Solution(object):
    def expressiveWords(self, S, words):
        res = 0
        string_groups = [[char, len(list(grp))] for char, grp in itertools.groupby(S)]
        for word in words:
            word_groups = [[char, len(list(grp))] for char, grp in itertools.groupby(word)]
            if (len(string_groups) == len(word_groups) and 
                all(gs[0] == gw[0] and (gs[1] == gw[1] or gs[1] > gw[1] and gs[1] >= 3)
                    for gs, gw in zip(string_groups, word_groups))):
                res += 1
        return res
            
