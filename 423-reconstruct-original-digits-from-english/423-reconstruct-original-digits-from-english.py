class Solution:
    def originalDigits(self, s: str) -> str:
        result=''
        fre=[0]*10
        cnt=Counter(s)
        
        fre[0]=cnt['z']
        fre[2]=cnt['w']
        fre[4]=cnt['u']
        fre[6]=cnt['x']
        fre[8]=cnt['g']
        fre[7]=cnt['s']-fre[6]
        fre[5]=cnt['v']-fre[7]
        fre[3]=cnt['h']-fre[8]
        fre[1]=cnt['o']-fre[2]-fre[4]-fre[0]
        fre[9]=cnt['i']-fre[6]-fre[5]-fre[8]
        
        for i in range(10):
            result+=str(i)*fre[i]
        
        return result