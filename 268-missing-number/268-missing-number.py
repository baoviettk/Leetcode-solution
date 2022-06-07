class Solution(object):
    def missingNumber(self, nums):
        i=0
        nums.append(-1)
        while i<len(nums):
            if nums[i]==i or nums[i]==-1:
                i+=1
            else:
                swap_index=nums[i]
                nums[i], nums[swap_index] = nums[swap_index], nums[i]
            
        return nums.index(-1)

        