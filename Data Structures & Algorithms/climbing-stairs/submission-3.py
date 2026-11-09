class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        if n == 0:
            return 1
        if n == 1:
            return 1
        else:
            one = self.climbStairs(n-1)
            two = self.climbStairs(n-2)
            self.memo[n] = one + two
            return one + two
        