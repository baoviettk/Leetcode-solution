class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        dic={}
        l=0
        meet=0
        min_len=999999
        for char in t:
            dic[char]=dic.get(char,0)+1
        require=len(dic)
        for r in range(len(s)):
            if s[r] in dic:
                dic[s[r]]-=1
                if dic[s[r]]==0:
                    meet+=1
                if meet==require:
                    while meet==require:
                        if s[l] in dic:
                            dic[s[l]]+=1
                            if dic[s[l]]==1:
                                meet-=1
                        l+=1
                    l-=1
                    dic[s[l]]-=1
                    meet+=1
                    cur_len=r-l+1
                    if r-l+1<min_len:
                        min_len=r-l+1
                        result=s[l:r+1]
        if min_len==999999:
            return ""
        return result