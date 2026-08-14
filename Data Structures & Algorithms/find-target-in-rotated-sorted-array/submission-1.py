class Solution:
    # Always use lo < hi so that the return statement is lo == mid == hi
    # To consider lower mid or upper mid, consider the case of 2 elements
    # Always try to exclude mid, reason about where the target CANNOT be
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target

        pos = self.binSearch(self.smallestFn)
        if self.nums[0] < self.nums[pos]:
            pos = 0
        print("index", pos, "val", nums[pos])
        self.shift = pos
        return self.shiftedBinSearch(self.findTarget)

    def shiftedBinSearch(self, targetFn):
        lo = 0
        hi = len(self.nums) - 1
        while lo < hi:
           
            m = lo + (hi - lo + 1) // 2 
            
            mshift = (m + self.shift) % len(self.nums)
            print("shifted", lo, m, hi, "mshift", mshift, "mshiftval", self.nums[mshift])
            if targetFn(self.nums[mshift], self.target):
                lo = m
            else:
                hi = m - 1
        
        print("exit", lo, hi)
        res = (lo + self.shift) % len(self.nums)
        if self.nums[res] == self.target:
            return res
        return -1


    
    def findTarget(self, x, target):
        return x <= target

    def smallestFn(self, x):
        return x < self.nums[0]


    # First find the index of the smallest element
    def binSearch(self, targetFn):
        l = 0
        r = len(self.nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if targetFn(self.nums[m]):
                r = m
            else:
                l = m + 1
        return l
    
        