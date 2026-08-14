class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # Sorting guarantees the invariant that we can find the remaining
        # with a linear approach for the n^2 approach 
        # all pairs and then binary search is an n^2 log n approach so we don't think 
        # about doing that.
        print(nums)
        n = len(nums)

        res = set()
        for i in range(n-2):
            l = i+1
            r = n-1
            target = - nums[i] # find when L + R == -I
   
            while l < r: 
                print(nums[i], nums[l], nums[r])
                p = nums[l] + nums[r]
                if p == target: 
                    t = [nums[i], nums[l], nums[r]]
                    t.sort() # sorting a constant length list is constant time 
                    tup = tuple(t)
                    res.add(tup)
                    l += 1
                    r -= 1
                elif p < target:
                    l += 1
                else: # p > target
                    r -= 1
        return list(res)


        




        