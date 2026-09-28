class Solution:
    def __init__(self):
        self.dp = {}
        
    def count1(self, n):
        if n in self.dp:
            return dp[n]
        count = 0
        l = n
        while l > 0:
            if l % 2 == 1:
                count += 1
            l >>= 1
        print("count", count)

        self.dp[n] = count
        return count

    def countBits(self, n: int) -> List[int]:
        res = [0 for i in range(n+1)]
        for i in range(n+1):
            res[i] = self.count1(i)

        return res

        