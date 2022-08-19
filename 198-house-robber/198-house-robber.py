class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        one,two=nums[-1],0
        
        for i in range(len(nums)-2,-1,-1):
            one,two=max(two+nums[i],one),one
        
        return max(two,one)