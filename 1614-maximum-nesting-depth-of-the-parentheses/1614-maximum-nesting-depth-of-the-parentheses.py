class Solution:
    def maxDepth(self, s: str) -> int:
        cur,res=0,0
        stk=[]
        for ch in s:
            if ch=="(":
                cur+=1
            elif ch==")":
                res=max(cur,res)
                cur-=1
        return res