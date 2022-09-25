class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        cnt={}
        fre=[[] for i in range(len(arr)+1)]
        
        for n in arr:
            cnt[n]=cnt.get(n,0)+1
        result=len(cnt)
        for n, c in cnt.items():
            fre[c].append(n)
        for i in range(len(arr)+1):
            for num in fre[i]:
                k-=i
                if k==0:
                    return result-1
                if k<0:
                    return result
                result-=1
                
        return result