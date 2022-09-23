class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt=Counter(s)
        result=0
        for ch in t:
            if cnt[ch]>0:
                cnt[ch]-=1
            else:
                result+=1
        return result