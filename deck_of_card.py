```
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.
Example 3:

Input: deck = [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
Example 5:

Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].
```

class Solution(object):
    def hasGroupsSizeX(self, deck):
        res = {}
        if not len(deck) > 1:
            return False
        for elem in deck:
            if elem in res:
                res[elem] += 1
            else:
                res[elem] = 1
        for value in res.values():
            if not self.gcd(value, len(deck)):
                return False                
        return True
    
    def gcd(self, num1, num2):
        for elem in range(2, num1+1):
            if num1 % elem == 0 and num2 % elem == 0:
                return True
        return False
        
        
        
