class Solution:
    def mon(self, x):
        return x < self.nums[0]

    def findMin(self, nums: List[int]) -> int: 
        self.nums = nums
        # Binary search 
        # Our monotonic function will be: 
        # let x be an element in nums:
        # def mon(x):
        #   x < nums[0]

        # Code out the binary search
        l = 0 
        r = len(nums) 
        while l <= r: 

            mid = (l + r) // 2
            print(l, mid, r)
            if mid == len(nums):
                return nums[0]
            if self.mon(nums[mid]):
                r = mid - 1
            else: 
                l = mid + 1
        return nums[l]
