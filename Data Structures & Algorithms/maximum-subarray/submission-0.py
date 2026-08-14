class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        most = nums[0]
        for l in range(len(nums)):
            val = nums[l]
            if val > most:
                most = val
            for r in range(l+1, len(nums)): 
                val += nums[r]
                if val > most:
                    most = val
        return most        