class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        cur_c, cur_dup='',0
        arr,result=[],''
        for c in s:
            if arr and cur_c==c:
                arr[-1][1]+=1
                if arr[-1][1] == k:
                    arr.pop()
                    if arr:
                        cur_c = arr[-1][0]
            else:
                arr.append([c,1])
                cur_c=c
        for [c,cnt] in arr:
            result+=c*cnt
        return result