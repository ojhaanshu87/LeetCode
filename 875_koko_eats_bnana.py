'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 
Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

'''

# low, high = 1, max(piles)
# mid = low + high / 2 that is 6 in given example
# 1 + 1 + 2 + 2 = 6 hours to finish but we need to optimise
# low = 1, high = 6 + 1 =
# mid = 4 now
# 

class Solution(object):
    def count_time_eat_all_speed(self, mid, piles):
        count_hours = 0
        for pile in piles:
            count_hours += pile / mid
            if pile % mid != 0:
                count_hours += 1
        return count_hours
    
    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        while low <= high:
            mid = low + ((high - low) >> 1)
            if self.count_time_eat_all_speed(mid, piles) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
