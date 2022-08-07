class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        result=0
        cur=1
        dic={}
        dic[s[0]]=1
        for i in range(1,len(s)):
            cur+=1
            if s[i] not in dic.keys():
                dic[s[i]]=0
            dic[s[i]]+=1
            while cur-max(dic.values())>k:
                dic[s[l]]-=1
                l+=1
                cur-=1
            result=max(result,cur)
        
        return result
                        
        