class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        result=0
        cur=1
        dic={}
        dic[s[0]]=1
        most_char=s[0]
        for i in range(1,len(s)):
            print("char:"+str(s[i]))
            print(most_char)
            cur+=1
            if s[i] not in dic.keys():
                dic[s[i]]=0
                print(i)
            dic[s[i]]+=1
            print(dic)
            if most_char!=s[i]:
                if dic[most_char]<dic[s[i]]:
                    most_char=s[i]
            if cur-dic[most_char]>k:
                dic[s[l]]-=1
                l+=1
                cur-=1
                print("cur:"+str(cur))
            result=max(result,cur)
        
        return result
                        
        