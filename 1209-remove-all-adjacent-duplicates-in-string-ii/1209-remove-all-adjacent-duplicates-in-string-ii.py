class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        arr, result=[],""
        cur_char=0
        
        for c in s:
            if arr and cur_char==c:
                arr[-1][1]+=1
                if arr[-1][1]==k:
                    arr.pop()
                    if arr:
                        cur_char=arr[-1][0]
            else:
                arr.append([c,1])
                cur_char=c
        for c, cnt in arr:
            result+=c*cnt
            
        return result
                