```
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
 

Constraints:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

```

#ALGORITHM
#Let's keep a count {card: number of copies of card} as a TreeMap (or dict).
#Then, repeatedly we will do the following steps: find the lowest value card that has 1 or more copies (say with value x), and try to remove x, x+1, x+2, ..., x+W-1
# from our count. If we can't, then the task is impossible.

class Solution(object):
    def isNStraightHand(self, hand, W):
        count = collections.Counter(hand)
        while count:
            count_min = min(count)
            for k in xrange(count_min, count_min+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1

        return True
        
