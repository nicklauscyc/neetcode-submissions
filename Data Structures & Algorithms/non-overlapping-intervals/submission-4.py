class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        print(intervals)
        
        cs = intervals[0][0]
        ce = intervals[0][1]
        remove = 0
        for i in range(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if ce > s:
                remove += 1
            ce = min(e, ce)
            if ce <= s:
                ce = e

        return remove
