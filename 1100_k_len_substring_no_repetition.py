```
Given a string S, return the number of substrings of length K with no repeated characters.

 

Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. In this case is not possible to find any substring.
```

##################################

```
The general approach here is to slide a window of length K across S. Whenever window contains only unique letters then add one to res signifying a unique string was found.

Below this is implemented using a dictionary to count the number of times each letter occurs in window. This means we do not need to check if a substring contains only unique letters at every iteration (which would be very time consuming). Instead, when a letter is added to the window we increase its count by 1, when a letter leaves the window we decrease its count by 1. If the count reaches 0, then we delete that letter from the window.

So, at each step we only need to:

add the new letter to window
remove the left most letter from the window
check if len(window) == K
If the substring contains only unique characters, then len(window) will be K. If there are any duplicate characters then len(window) will be less than K.

Example of how the code works:
i.e: S = 'aabcgfleetcode' ; K = 5

	'[aabcg]fleetcode'
	window = {'a': 2, 'b': 1, 'c':1, 'g': 1}  < -- window spans 5 letters but len(window) = 4 so substring is not unique
	
	'a[abcgf]leetcode'
	window = {'a': 1, 'b': 1, 'c': 1, 'g': 1, 'f': 1} <-- window spans 5 letters and len(window) = 5 so substring is unique
	
	'aa[bcgfl]eetcode'
	window = {'b': 1, 'c': 1, 'g': 1, 'f': 1, 'l': 1} <-- window spans 5 letters and len(window) = 5 so substring is unique
```

class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        #Initialize window by counting how many times each letter
        #occurs in the first K letters of S
        window = {}
        for letter in S[:K]:
            window[letter] = window.get(letter,0) + 1 #window.get(letter,0) is window[letter] if letter is in window otherwise  it is 0
        
        i = K 
        res = 0 #count substrings with no repeated characters
        while i < len(S):
            #At each step check if len(window) == K, this can only happen if each
            #letter's count is equal to 1 which means there are no repeated characters
            if len(window) == K:
                res += 1
            
            #Insert letter to the right of the window into the window (and update the letter count)
            window[S[i]] = window.get(S[i],0) + 1
            
            #Remove the letter from the left of the window, if it was there was only 1 of that letter
            #then delete it from the window, otherwise decrease its count by 1
            if window[S[i-K]] == 1:
                del window[S[i-K]]
            else:
                window[S[i-K]] -= 1
        
            i += 1
        else:
            #Once the while loop terminates check if the last K letters formed a unique substring
            #Note: while-else activates the else statement after the while loop terminates if the 
            #      while loop did not terminate due to a break command
            if len(window) == K:
                res += 1
        
        return res
