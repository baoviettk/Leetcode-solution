class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=nums[0]
        cur_min,cur_max=1,1
        
        for num in nums:
            temp_max=cur_max
            cur_max=max(cur_max*num,cur_min*num,num)
            cur_min=min(temp_max*num,cur_min*num,num)
            
            result=max(cur_max, result)
        return result
        