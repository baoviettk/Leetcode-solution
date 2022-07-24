class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        
        for current in range(1,amount+1):
            
            for coin in coins:
                if current-coin>-1:
                    dp[current]= min(dp[current], 1+dp[current-coin])
        return dp[amount] if dp[amount]<amount+1 else -1 