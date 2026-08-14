class Solution:
    # 14 mins
    def dp(self, nums, i):
        print('index', i)
        if i in self.memo:
            return self.memo[i]

        if i >= len(nums) - 1:
            self.memo[i] = True
            return True
        
        # To jump or not to jump
        maxJump = nums[i]
        if not maxJump: 
            self.memo[i] = False
            return False
        
        for j in range(1, maxJump+1):
            success = self.dp(nums, i+j)
            if success: 
                self.memo[i] = True
                return True

        self.memo[i] = False
        return False
       
    def canJump(self, nums: List[int]) -> bool: 
        self.memo = {}
        res = self.dp(nums, 0)
        print(self.memo)
        return res