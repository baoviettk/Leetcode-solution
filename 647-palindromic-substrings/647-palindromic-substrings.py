class Solution:
    def countSubstrings(self, s: str) -> int:
        result=0
        for i in range(len(s)):
            l,r=i,i
            while l>-1 and r<len(s):
                if s[l]==s[r]:
                    result+=1
                    l-=1
                    r+=1
                else:
                    break
            
        for i in range(len(s)-1):
            l,r=i,i+1
            while l>-1 and r<len(s):
                if s[l]==s[r]:
                    result+=1
                    l-=1
                    r+=1
                else:
                    break
                    
        return result