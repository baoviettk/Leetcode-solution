class Solution(object):
    def subsetsWithDup(self, nums):
        cur, arr=[],[]
        n=len(nums)
        nums.sort()
        
        def dfs(i):
            if i==n:
                arr.append(list(cur))
                return
            
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            
            while i+1<n and nums[i]==nums[i+1]:
                i+=1
            
            dfs(i+1)
        
        dfs(0)
        return arr
        