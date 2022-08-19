class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp={(len(nums)-1):nums[-1]}
        
        for i in range(len(nums)-2,-1,-1):
            dp[i]=max(dp.get(i+2,0)+nums[i],dp[i+1])
        print(dp)
        
        return max(dp[0],dp[1])