class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        right=len(nums)
        result=[]
        nums.sort()
        
        def twoSum(left,target):
            l,r=left, right-1
            while l<r:
                cur_sum=nums[l]+nums[r]+target
                if cur_sum==0:
                    result.append([target,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while r>l and nums[r]==nums[r+1]:
                        r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1

                elif cur_sum>0:
                    r-=1
                else:
                    l+=1
                
                
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue      
            twoSum(i+1,nums[i])
        
        return result
        
            
    
                               
                    
                