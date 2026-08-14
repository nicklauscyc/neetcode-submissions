class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        run = 0 
        most = nums[0]
        for num in nums:
            print(run)
            if run < 0:
                run = 0
            run += num
            if most < run: 
                most = run
        return max(run,most)

   