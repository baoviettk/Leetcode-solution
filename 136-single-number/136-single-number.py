class Solution(object):
    def singleNumber(self, nums):
        result=nums[0]
        for i in range(1,len(nums)):
            result^=nums[i]
            
        return result
        