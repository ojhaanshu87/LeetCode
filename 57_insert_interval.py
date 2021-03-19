'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
'''

class Solution(object):
    def insert(self, intervals, newInterval):  
        # Append new interval to intervals and sort based on first element
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x:x[0])
        
        # if length less than 0 then return newInterval
        if len(intervals) < 0:
            return newInterval
        
        # Else we are checking for the condtion for merging the intervals.
        #So here we have taken 0 and 1. Where 0 means the starting index and 1 means the ending index and after this condition is True 
        #and the intervals are merged we are just poping out the current i else we will continue till the end.
        
        curr = 1
        while curr < len(intervals):
            if intervals[curr][0] <= intervals[curr-1][1]:
                intervals[curr-1][0] = min(intervals[curr-1][0], intervals[curr][0])

                intervals[curr-1][1] = max(intervals[curr-1][1], intervals[curr][1])

                intervals.pop(curr)
            else:
                curr += 1
                continue

        return intervals
