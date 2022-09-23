class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dif=[0]*26
        result=0
        for i in range(len(s)):
            dif[ord(s[i])-ord('a')]+=1
            dif[ord(t[i])-ord('a')]-=1
        for num in dif:
            if num>0:
                result+=num
        
        return result