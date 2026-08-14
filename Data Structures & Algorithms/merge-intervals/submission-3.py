class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = -1 
        r = -1
        res = []
        for i in sorted(intervals): 
            if l == -1:
                l = i[0]
                r = i[1]
            else:
                if r >= i[0]:
                    # merge the interval
                    r = max(r, i[1])
                else: 
                    res.append([l, r])
                    l = i[0]
                    r = i[1]
        if not res or [l, r] != res[-1]:
            res.append([l, r])
        return res



        