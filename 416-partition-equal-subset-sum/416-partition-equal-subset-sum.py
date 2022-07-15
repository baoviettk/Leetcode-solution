class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
    
        n=len(nums)
        dp=[[-1 for x in range(sum(nums)//2+1)] for y in range(n)]
        
        def subSetSum(nums, index, n, target):
            if index==n or target<0:
                return False
            if nums[index]==target:
                dp[index][target]=True
                return True
            if dp[index][target]!=-1:
                return dp[index][target]
            dp[index][target]=subSetSum(nums, index+1, n, target) or subSetSum(nums, index+1, n, target-nums[index])
            return dp[index][target]
        
        target1=sum(nums)//2
        return subSetSum(nums, 0, n, target1)
