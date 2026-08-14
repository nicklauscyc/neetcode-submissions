class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tdp = {}
        def dp(i, status):
            if i >= len(nums):
                if status == 0:
                    # penalize not picking any element
                    return -1001
                else:
                    # at least one other element has been picked, this is 
                    # safe to terminate
                    return 0 
            if (i, status) in tdp:
                return tdp[(i, status)]

            # status == 0 : not started sub array
            # status == 1 : started sub array
            # status == 2 : ended sub array
            if status == 0:
                start_later = dp(i+1, 0)
                start_now = nums[i] + dp(i+1, 1)
                tdp[(i, status)] = max(start_later, start_now)
                return max(start_later, start_now)
            elif status == 1:
                end_later = nums[i] + dp(i+1, 1)
                end_now = dp(i+1, 2)
                tdp[(i, status)] = max(end_later, end_now)
                return max(end_later, end_now)
            elif status == 2:
                tdp[(i, status)] = 0
                return 0 # nothing to change
        
        return dp(0, 0)


        