"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Sort the intervals  

        # Go over the intervals, and if they don't overlap, merge them together greedily

        # Once we merged the max number of intervals, count the distinct intervals to get the number of meeting rooms
        starts = sorted(intervals, key=lambda x: x.start)
        ends = sorted(intervals, key=lambda x: x.end)

        s = 0 
        e = 0 
        n = len(intervals)
        ongoing_meetings = 0
        max_meetings = 0
        while s < n and e < n:
            start_time = starts[s].start
            end_time = ends[e].end
            print("start", start_time)
            print("end", end_time)
            print("xxxxxxx")

            if start_time < end_time:
                print("starting", start_time)
                ongoing_meetings += 1
                s += 1
            else: # start_time >= end_time:
                print("ending", end_time)
                ongoing_meetings -= 1
                e += 1
            print("ongoing", ongoing_meetings)
            if ongoing_meetings > max_meetings: 
                max_meetings = ongoing_meetings
        
        return max_meetings

            

