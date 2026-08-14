class Solution:
    def findMin(self, nums):

        # Since our array, if sorted, is increasing in order, 
        # f() is a monotonically increasing function over nums
        # it goes from 0 (false) to 1 (true) when it finds the 
        # smallest element
        def f(x): 
            return x < nums[0]
        
        l = 0
        r = len(nums) 
        m = (l + r) // 2
        while l < r: 
            if f(nums[m]):
                r = m
            else:
                l = m + 1
            m = (l + r) // 2

        return m

    def search(self, nums: List[int], target: int) -> int:
        # First find the minimum
        mo = self.findMin(nums)
        print("min at index", mo)

        # So now every index will be i + mo % len(nums)

        # Then have some function that translates the index from 
        # a non rotated array to a rotated array to find the target
        l = 0
        r = len(nums)
        while l < r:
            m = (l + r) // 2 
            i = (m + mo) % len(nums)
            print("actual index", l, m, r, i)
            res = nums[i]
            if res == target: 
                return i
            elif res < target:
                l = m + 1
            else:
                # res > target
                r = m

        return -1



