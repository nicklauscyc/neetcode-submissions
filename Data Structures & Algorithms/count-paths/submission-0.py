class Solution:
    def rec(self, r, c, m, n, dp):
        if (r, c) in dp: 
            return dp[(r,c)]

        if r >= m or r < 0:
            return 0
        if c >= n or c < 0:
            return 0

        # returns the number of paths to the (m-1, n-1)
        if r == m - 1 and c == n - 1:
            return 1
        
        right = self.rec(r, c+1, m, n, dp)
        down = self.rec(r+1, c, m, n, dp)
        dp[(r,c)] = right + down
        return right + down 

    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        return self.rec(0, 0, m, n, dp)
        