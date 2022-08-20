class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        if s[0] =='0' and (len(s)==1 or int(s[-2:])>27):
            return 0
                            
        dp=[0]*(len(s)+1)
        dp[-1]=1
        if s[-1]!='0':
            dp[-2]=1
        else:
            dp[-2]=0
        for i in range(len(s)-2,-1,-1):
            if s[i]=='0':
                print("here")
                if i>0 and s[i-1]>'2':
                    return 0
                else:
                    dp[i]=0
                    continue
            if int(s[i:i+2])<27 and s[i] !='0':
                dp[i]=dp[i+1]+dp[i+2]
            else:
                dp[i]=dp[i+1]
        print(dp)
        return dp[0]