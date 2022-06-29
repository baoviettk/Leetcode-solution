class Solution(object):
    def permute(self, nums):
        result=[]
        if len(nums)==1:
            return [list(nums)]
        for num in nums:
            n=nums.pop(0)
            perms=self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            
            result.extend(perms)
            nums.append(n)
        
        return result
        