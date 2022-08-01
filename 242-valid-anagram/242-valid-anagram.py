class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        if len(s)!=len(t):
            return False
        for char in s:
            if char not in dic:
                dic[char]=0
            dic[char]+=1
        for char in t:
            if char not in dic:
                return False
            if dic[char]>1:
                dic[char]-=1
            else:
                del dic[char]
        
        return True
            