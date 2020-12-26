'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

'''
First, we sort the list as described. Then, we insert the first interval into our merged list and continue considering each interval in turn as follows:
If the current interval begins after the previous interval ends, then they do not overlap and we can append the current interval to merged.
Otherwise, they do overlap, and we merge them by updating the end of the previous interval if it is less than the end of the current interval.

Time complexity : O(nlogn)
Space complexity : O(log N) or O(N)
If we can sort intervals in place, we do not need more than constant additional space, 
although the sorting itself takes O(\log n)O(logn) space. Otherwise, we must allocate linear space to store a copy of intervals and sort that.
'''

class Solution(object):
    def merge(self, intervals):
        sorted_by_lower_bound = sorted(intervals, key = lambda tup:tup[0])
        merged =[]
        for higher in sorted_by_lower_bound:
            if not merged:
                merged.append(higher)
            else:
                lower = merged[-1]
                if higher[0] <= lower[1]:
                    upper_bound = max (lower[1], higher[1])
                    merged[-1] = (lower[0], upper_bound)
                else:
                    merged.append(higher)
        return merged
        
