class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len=len(nums)
        result=[1]*nums_len
        for i in range(1,nums_len):
            result[i]=result[i-1]*nums[i-1]
        current=1
        for i in range(nums_len-1,-1,-1):
            result[i]*=current
            current*=nums[i]
                    
        return result
    
    
            
        