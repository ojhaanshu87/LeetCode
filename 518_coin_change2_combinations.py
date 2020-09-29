```
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1
```

#Initiate number of combinations array with the base case "no coins": dp[0] = 1, and all the rest = 0.
#Loop over all coins:
                    #For each coin, loop over all amounts from 0 to amount:
                            #For each amount x, compute the number of combinations: dp[x] += dp[x - coin].
#Return dp[amount]

class Solution(object):
    def change(self, amount, coins):
        dp_table = [0] * (amount + 1)
        dp_table[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp_table[x] += dp_table[x - coin]
        return dp_table[amount]
        
