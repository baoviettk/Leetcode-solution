class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        mi=999999999
        coins.sort()
        def bfs(remain):
            if remain in dp:
                return dp[remain]
            if remain==0:
                return 0
            mi=999999999
            for coin in coins:
                if coin> remain:
                    break
                mi=min(mi,1+bfs(remain-coin))
            dp[remain]=mi
            return mi
        
        result= bfs(amount)
        if result >= 999999999:
            return -1
        return result