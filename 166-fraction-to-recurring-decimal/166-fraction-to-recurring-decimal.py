class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        pos={}
        if numerator==0:
            return '0'
        if numerator*denominator>0:
            sign=''
        else:
            sign='-'
        numerator,denominator=abs(numerator),abs(denominator)
        result=sign+str(numerator//denominator)
        numerator%=denominator
        if numerator>0:
            result+='.'
        while numerator>0:
            if numerator in pos:
                p=pos[numerator]
                return result[:p]+'('+result[p:]+')'
            pos[numerator]=len(result)
            numerator*=10
            result+=str(numerator//denominator)
            numerator%=denominator
        return result