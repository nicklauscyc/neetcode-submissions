class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Create array of max from (i, n-1]
        maxAfter = -1
        after = [0 for j in range(len(prices))]
        for i in range(len(prices)-1, -1, -1):
            after[i] = maxAfter
            if prices[i] > maxAfter:
                maxAfter = prices[i]
        print(after)

        maxProfit = 0
        for i in range(len(prices)):
            profit = after[i] - prices[i]
            maxProfit = max(profit, maxProfit)
        return maxProfit
        