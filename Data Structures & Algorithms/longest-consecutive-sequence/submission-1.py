class Solution:
    # 15 min with hint 
    # notice invariant with starts 
    # rough out the solution 
    # and high granularity find the complexity
    # notice it's not really n^2 since each start is bounded
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)

        start = set()
        for num in nums:
            if (num - 1) not in s:  
                start.add(num)
        print(start)

        max_l = 0
        for ss in start: 
            l = 1
            while (ss+1) in s: 
                print(ss+1, " in ", s)
                l += 1
                ss += 1
            if l > max_l: 
                max_l = l
        return max_l
             

        