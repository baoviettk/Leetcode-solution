class Solution(object):
    def searchRange(self, nums, target):
        
        def findIndex(first,last):
            if first>last:
                return None
            middle = (first+last)/2
            if nums[middle]==target:
                return middle
            if target<nums[middle]:
                return findIndex(first, middle-1)
            return findIndex(middle+1, last)
        left= findIndex(0, len(nums)-1)
        if left==None:
            return [-1,-1]
        right=left
        while left-1>-1 and nums[left-1]==nums[left]:
            left-=1
        while right+1<len(nums) and nums[right+1]==nums[right]:
            right+=1
            
        return [left,right]