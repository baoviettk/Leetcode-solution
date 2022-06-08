class Solution(object):
    def findDisappearedNumbers(self, nums):
        i = 0
        return_arr=[]
        while i < len(nums):
            swap_index=nums[i]-1
            if nums[i] != nums[swap_index]:
                nums[i], nums[swap_index] = nums[swap_index], nums[i]
            else:
                i += 1
            
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return_arr.append(i+1)
        
        return return_arr