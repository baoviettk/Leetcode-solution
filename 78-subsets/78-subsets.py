class Solution(object):
    def subsets(self, nums):
        cur, arr=[],[]
        n=len(nums)
        
        def dfs(i):
            if i==n:
                arr.append(list(cur))
                return
            
            cur.append(nums[i])
            dfs(i+1)
            
            cur.pop()
            dfs(i+1)
        
        dfs(0)
        return arr
        