class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LEN=len(nums)
        dp=[1]*LEN
        for i in range(LEN-1,-1,-1):
            for j in range(i+1,LEN):
                if nums[j]>nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        
        return max(dp)