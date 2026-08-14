class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums))]

        def help(i):
            if i >= len(nums):
                return 0

            if dp[i] > -1:
                return dp[i]

            # Rob this house
            toRob = help(i+2) + nums[i]

            # Don't rob this house
            notToRob = help(i+1)

            res = max(toRob, notToRob)
            if res == toRob:
                print("rob", i, toRob)
            else: 
                print("pass", i, notToRob)
            dp[i] = res

            return res

        return help(0)
        