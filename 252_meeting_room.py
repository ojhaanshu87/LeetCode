'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
'''

'''
The idea here is to sort the meetings by starting time. Then, go through the meetings one by one and make sure that each meeting ends before the next one starts.
'''

class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key=lambda elem:elem[0])
        for elem in range(len(intervals) - 1):
            if intervals[elem][1] > intervals[elem + 1][0]:
                return False
        return True
