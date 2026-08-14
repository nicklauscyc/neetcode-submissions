class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        r = len(intervals) - 1
        l = 0 
        m = 0
        while l <= r:
            m = (l + r) // 2
            #print(l, m, r)
            if newInterval[0] < intervals[m][0]:
                r = m - 1
            else:
                l = m + 1
        intervals.insert(l, newInterval)


        # merge operation
        merged = []
        res = [] # this is the current interval being built
        #print(intervals)
        for i in range(len(intervals)):
            #print(i, res)
            if res: # If there is an interval being built
                if res[1] >= intervals[i][0]:
                    res[1] = max(res[1], intervals[i][1])
                else:
                    # no merging, start a new interval
                    merged.append(res)
                    res = intervals[i]
            else:
                # start a new interval
                res = intervals[i]

        # If there was still an interval pending after the last run, add it
        if res:
            merged.append(res)

  
        return merged
        '''
        r l 
          m
          *

        r l
        m
          * '''  