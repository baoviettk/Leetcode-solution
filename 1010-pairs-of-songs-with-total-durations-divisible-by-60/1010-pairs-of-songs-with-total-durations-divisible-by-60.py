class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic={}
        result=0
        for t in time:
            mod= t%60
            dic[mod]= dic.get(mod,0)+1
        kys=dic.keys()
        for k in kys:
            if k>30:
                continue
            if k==30 or k==0:
                result+=int(dic[k]*(dic[k]-1)/2)
            
            else:
                result+=dic[k]*dic.get(60-k,0)
        
        return result
                