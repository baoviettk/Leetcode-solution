class Solution(object):
    def findTargetSumWays(self, nums, target):
        dp={}
        
        def backtracking(i,total):
            if i==len(nums):
                if total==target:
                    return 1
                return 0
            if (i,total) in dp:
                return dp[(i,total)]
            
            dp[(i,total)]= backtracking(i+1,total+nums[i])+backtracking(i+1,total-nums[i])
            
            return dp[(i,total)]
        
        return backtracking(0,0)
        