class Solution:
    def knightDialer(self, n: int) -> int:
        def revert(num):
            if num==0:
                return 1
            return 0
        if n ==0:
            return n
        if n==1: return 10
        else:
            neighbors = {
                0:(4,6),
                1:(6,8),
                2:(7,9),
                3:(4,8),
                4:(0,3,9),
                5:(),
                6:(0,1,7),
                7:(2,6),
                8:(1,3),
                9:(2,4)
            }
            index=1
            dp=[[1]*10 for i in range(2)]
            for j in range(n-1):
                for i in range(10):
                    temp=0
                    for nei in neighbors[i]:
                        temp+=dp[revert(index)][nei]
                    dp[index][i]=temp
                index=revert(index)
        return sum(dp[revert(index)])%(10**9+7)
        