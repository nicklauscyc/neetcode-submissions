class MedianFinder:

    def __init__(self):
        self.nums = []

        

    def addNum(self, num: int) -> None:
        # Perform a binary search to insert the num into self.nums
        n = len(self.nums)
        l = 0 
        r = n # We may have to insert this element at the end

        print("addNum start", self.nums)

        while l < r: 
            m = l + (r-l) // 2
            if num < self.nums[m]:
                r = m
            else: 
                l = m + 1
        
        # TODO optimize the insertion rule later
        self.nums.insert(l, num)
        print("addNum end, inserted at ", l, self.nums)
        


    def findMedian(self) -> float: 
        if len(self.nums) & 1: 
            return self.nums[len(self.nums)//2]
        return self.nums[len(self.nums)//2] / 2 + self.nums[len(self.nums)//2 - 1] / 2        
        