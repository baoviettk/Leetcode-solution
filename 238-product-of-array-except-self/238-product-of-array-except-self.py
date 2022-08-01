class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product, postfix_product=[1]*len(nums),[1]*len(nums)
        result=[]
        nums_len=len(nums)-1
        for i in range(1,nums_len+1):
            prefix_product[i]=prefix_product[i-1]*nums[i-1]
        current=1
        for i in range(nums_len-1,-1,-1):
            postfix_product[i]=postfix_product[i+1]*nums[i+1]
        
        for i in range(nums_len+1):
            result.append(prefix_product[i]* postfix_product[i])
            
        return result
            
        