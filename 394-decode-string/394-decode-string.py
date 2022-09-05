class Solution:
    def decodeString(self, s: str) -> str:
        stk=[]
        cur=''
        cur_num=0
        for c in s:
            if c=="[":
                stk.append(cur)
                stk.append(cur_num)
                cur,cur_num='',0
            elif c=="]":
                num=stk.pop()
                prev=stk.pop()
                cur=prev+cur*num
            elif c.isdigit():
                cur_num=cur_num*10+int(c)
            else:
                cur+=c
            
        return cur
                
                