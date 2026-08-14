class Solution:

    def climbStairs(self, n: int) -> int:
        self.dp = {}
        return self._climbStairs(n)

    def _climbStairs(self, n):
    
        
        if n in self.dp: 
            return self.dp[n]
        if n == 0: 
            self.dp[n] = 0
            return 1
        if n == 1: 
            self.dp[n] = 1
            return 1
        else:
            res = self._climbStairs(n-1) + self._climbStairs(n-2)
            self.dp[n] = res
            return res
        