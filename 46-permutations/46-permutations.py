class Solution(object):
    def permute(self, nums):
        if len(nums)==1:
            return [list(nums)]
        result=[]
        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        
        return result
        