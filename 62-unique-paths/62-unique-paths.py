class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1]*n
        for i in range(1,m):
            for j in range(n):
                if j>0:
                    dp[j]+=dp[j-1]
        return dp[-1]