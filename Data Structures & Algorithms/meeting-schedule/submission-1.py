"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        starts = sorted(intervals, key=lambda x: x.start)
        
        if not starts:
            return True

        start = starts[0].start
        end = starts[0].end
        for i in range(1, len(starts)):
            interval = starts[i]
            if end > interval.start:
                return False
            end = interval.end
        return True
                
