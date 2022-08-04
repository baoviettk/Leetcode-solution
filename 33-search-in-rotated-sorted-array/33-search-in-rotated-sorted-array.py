class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=(r+l)//2
            if nums[m]== target:
                return m
            if nums[m]>=nums[l]:
                if target<=nums[m] and target>=nums[l]:
                    r=m-1
                else:
                    l=m+1
            else:
                if target>=nums[m] and target<nums[l]:
                    l=m+1
                else:
                    r=m-1
        return -1