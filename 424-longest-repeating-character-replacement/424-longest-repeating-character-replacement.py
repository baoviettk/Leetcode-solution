class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        result=0
        dic={}
        dic[s[0]]=1
        most_char=1
        for i in range(1,len(s)):
            if s[i] not in dic.keys():
                dic[s[i]]=0
            dic[s[i]]+=1
            most_char=max(most_char,dic[s[i]])
            if (i-l+1-most_char)>k:
                dic[s[l]]-=1
                l+=1
            result=max(result,i-l+1)
        
        return result
                        
        