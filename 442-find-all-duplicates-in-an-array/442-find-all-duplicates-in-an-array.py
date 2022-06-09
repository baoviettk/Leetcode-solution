class Solution(object):
    def findDuplicates(self, nums):
        i=0
        return_arr=[]
        while i< len(nums):
            j=nums[i]-1
            if nums[i]!=nums[j]:
                nums[i],nums[j]= nums[j],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return_arr.append(nums[i])
        return return_arr
        