class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def rob(l,r) -> int:
            if r-l<1:
                return nums[l]
            one,two=nums[r],0
        
            for i in range(r-1,l-1,-1):
                one,two=max(two+nums[i],one),one
        
            return max(two,one)
        
        return max(rob(0,len(nums)-2), rob(1,len(nums)-1))
