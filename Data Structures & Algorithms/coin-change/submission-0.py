class Solution:
    def help(self, amount):
        if amount in self.dp:
            return self.dp[amount]

        if amount == 0: 
            return 0
        if amount < 0:
            return self.impossible

        min_num = self.impossible
        for coin in self.coins: 
            num = 1 + self.help(amount - coin)
            if num < min_num: 
                min_num = num
        self.dp[amount] = min_num
        return min_num

        
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        # it is impossible to use more than amount // smallestCoin + 1 number of coins to 
        # make up the amount
        smallestCoin = coins[0]
        for coin in coins: 
            if coin < smallestCoin:
                smallestCoin = coin
        self.impossible = amount // smallestCoin + 1
        
        self.dp = {}
        res = self.help(amount)
        if res == self.impossible: 
            return -1
        return res
        
        