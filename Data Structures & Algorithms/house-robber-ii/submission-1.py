class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def rob(nums, i, first_robbed):
            if (i, first_robbed) in dp:
                return dp[(i, first_robbed)]
            if i > len(nums) - 1:
                dp[(i, first_robbed)] = 0
                return 0 
            # To rob
            if i == len(nums) - 1:
                if first_robbed:
                    dp[(i, first_robbed)] = 0
                    return 0 # can't rob this since the first was robbed
                dp[(i, first_robbed)] = nums[i]
                return nums[i]
            
            is_rob = 0
            if i == 0:
                is_rob = nums[i] + rob(nums, i+2, True)
            else:
                is_rob = nums[i] + rob(nums, i+2, first_robbed)

            # Not to rob
            no_rob = rob(nums, i+1, first_robbed)

            dp[(i, first_robbed)] = max(is_rob, no_rob)
            return max(is_rob, no_rob)
        
        return rob(nums, 0, False)
        