class Solution:
    def calculate(self, s: str) -> int:
        stack,cur_num,ope=[],0,"+"
        all_oper={"+","-","*", "/"}
        for i in range(len(s)):
            char=s[i]
            if char.isnumeric():
                cur_num=cur_num*10+int(char)
            if char in all_oper or i ==len(s)-1:
                if ope=="+":
                    stack.append(cur_num)
                elif ope=="-":
                    stack.append(-cur_num)
                elif ope=="*":
                    stack[-1]*=cur_num
                else:
                    stack[-1]=int(stack[-1]/cur_num)
                
                ope=char
                cur_num=0
        return sum(stack)