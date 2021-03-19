'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
'''

#Approach 1: Priority Queues

'''
Algorithm

A) Sort the given meetings by their start time.
B) Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will
get free.
C) For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
D) If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
E) If not, then we allocate a new room and add it to the heap.
F) After processing all the meetings, the size of the heap will tell us the number of rooms allocated. 
This will be the minimum number of rooms needed to accommodate all the meetings.
'''

class Solution(object):
    def minMeetingRooms(self, intervals):
        # MIN Heap (Priority QUEUE) TC (NLOGN), SPACE (N)
        if not intervals:
            return 0
        
        intervals, res = sorted(intervals, key=lambda elem:elem[0]), []
        # Add and create room for first meeting 
        heapq.heappush(res, intervals[0][1])
        # for rest of meeting rooms
        for elem in intervals[1:]:
            # if room due to free up the earliest is free, assign room to this meeting
            if res[0] <= elem[0]:
                heapq.heappop(res)
            #if new room assign then add to heap. If old room allocated, then add to heap with updated end time
            heapq.heappush(res, elem[1])
        
        # size of heap minimum rooms required
        return len(res)

#Approach 2: Chronological Ordering

'''
Algorithm

A) Separate out the start times and the end times in their separate arrays.
B) Sort the start times and the end times separately. Note that this will mess up the original correspondence of start times and end times.
They will be treated individually now.
C) We consider two pointers: s_ptr and e_ptr which refer to start pointer and end pointer. 
The start pointer simply iterates over all the meetings and the end pointer helps us track if a meeting has ended and if we can reuse a room.
D) When considering a specific meeting pointed to by s_ptr, we check if this start timing is greater than the meeting pointed to by e_ptr. 
E) If this is the case then that would mean some meeting has ended by the time the meeting at s_ptr had to start. So we can reuse one of the rooms. Otherwise, we have to allocate a new room.
If a meeting has indeed ended i.e. if start[s_ptr] >= end[e_ptr], then we increment e_ptr.
F) Repeat this process until s_ptr processes all of the meetings.
'''

class Solution(object):
    def minMeetingRooms(self, intervals):
        # Chronocial Ordering TC (NLOGN) and Space (N)
        
        if not intervals:
            return 0
        
        res = 0
        
        #sort start and end time
        start_time = sorted([elem[0] for elem in intervals])
        end_time = sorted([elem[1] for elem in intervals])
        
        # define two pointer
        start_ptr, end_ptr = 0, 0
        
        # untill all meeting room assigned
        while start_ptr < len(intervals):
            #if there is meeting ended by time the meeting at start_ptr starts
            if start_time[start_ptr] >= end_time[end_ptr]:
                # FreeUp rooma nd increment end_ptr
                res -= 1
                end_ptr += 1
            #if room got free then res += 1 wouldn't effective. res would remains same in that case. If room will not free then increase room
            res += 1
            start_ptr += 1  
        return res

