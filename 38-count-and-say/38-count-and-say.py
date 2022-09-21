class Solution:
    def countAndSay(self, n: int) -> str:
        cur,nxt='1',''
        for i in range(1,n):
            cur_ch,fre=cur[0],1
            for j in range(1,len(cur)):
                if cur_ch==cur[j]:
                    fre+=1
                else:
                    nxt+=str(fre)+str(cur_ch)
                    cur_ch=cur[j]
                    fre=1
            nxt+=str(fre)+str(cur_ch)
            cur,nxt=nxt,""
        return cur
            
        