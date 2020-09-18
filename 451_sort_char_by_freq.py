```
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```
 
#HASH MAP and SORT -> Time Complexity : O(nlogn) OR O(n+klogk).

class Solution(object):
    def frequencySort(self, s):
        res = collections.Counter(s)
        temp = [(k,v) for k,v in sorted(res.items(), key=lambda x: (-x[1], x))]
        res = [i*j for i, j in temp]
        return ''.join(res)


#Multiset and Bucket Sort -> Time Complexity : O(n)

```
Firstly, observe that because all of the characters came out of a String of length nn, the maximum frequency for any one character is nn.
This means that once we've determined all the letter frequencies using a HashMap, we can sort them in O(n)O(n) time using Bucket Sort.
Recall that for our previous approaches, we used comparison-based sorts, which have a cost of O(nlogn).

Recall that Bucket Sort is the sorting algorithm where items are placed at Array indexes based on their values (the indexes are called "buckets"). 
For this problem, we'll need to have a List of characters at each index. For example, here is how our String from before goes into the buckets.

While we could simply make our bucket Array length nn, we're best to just look for the maximum value (frequency) in the HashMap.
That way, we only use as much space as we need, and won't need to iterate over heaps of empty buckets during the next phase.

Finally, we need to iterate over the buckets, starting with the largest and ending with the smallest, building up the string in much the same way as we did before.
```

class Solution(object):
    def frequencySort(self, s):
        if not s: return s
    
        # Determine the frequency of each character.
        to_dict = collections.Counter(s)
        max_freqency = max(to_dict.values())

        # Bucket sort the characters by frequency.
        buckets = [[] for _ in range(max_freqency + 1)]
        for key, value in to_dict.items():
            buckets[value].append(key)

        # Build up the string.
        string_builder = []
        for i in range(len(buckets) - 1, 0, -1):
            for elem in buckets[i]:
                string_builder.append(elem * i)

        return "".join(string_builder)



