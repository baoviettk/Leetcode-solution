class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[99999]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for c in coins:
                if i-c>-1:
                    dp[i]=min(dp[i-c]+1,dp[i])
        return dp[amount] if dp[amount]!=99999 else -1