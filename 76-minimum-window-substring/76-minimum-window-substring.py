class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        dic={}
        l=0
        meet=0
        min_l,min_r,min_len=0,0,999999
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
                    print(cur_len)
                    if cur_len<min_len:
                        min_len=cur_len
                        min_l,min_r=l,r
        if min_len==999999:
            print("here3")
            return ""
        return s[min_l:min_r+1]