class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=(r+l)//2
            if nums[m]== target:
                return m
            if nums[m]>=nums[l]:
                if target<=nums[m] and target>=nums[l]:
                    print("take left")
                    r=m-1
                else:
                    print("take right")
                    l=m+1
            else:
                if target>=nums[m] and target<nums[l]:
                    print("take right")
                    l=m+1
                else:
                    print("take left")
                    r=m-1
        return -1