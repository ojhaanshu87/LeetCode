```
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
 

Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
 

Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

```

class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        houses.sort()
        left, right, i, j = -float('inf'), heaters[0], 0, 0
        max_radius = float('-inf')
        
        while i < len(houses):
            
            if(houses[i] >= left and houses[i] <= right):
                if(left == float('-inf')):
                    max_radius = max(max_radius, min(float('inf'), right - houses[i]))
                else:
                    max_radius = max(max_radius, min(houses[i]-left, right - houses[i]))     
                i+=1 
            else:
                left = right
                j+=1
                
                if(j == len(heaters)):
                    right = float('inf')
                else:
                    right = heaters[j]
        return max_radius
        
