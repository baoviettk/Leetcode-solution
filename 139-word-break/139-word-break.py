class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        LEN_S=len(s)
        dp=[False]*(LEN_S+1)
        dp[-1]=True
        for i in range(LEN_S-1,-1,-1):
            for w in wordDict:
                LEN_W=len(w)
                if i+LEN_W<=LEN_S and s[i:i+LEN_W]==w and dp[i+LEN_W]:
                    dp[i]=True
                    break
        
        return dp[0]