class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp={}
        
        def find(i, remain_zero, remain_one):
            if i==len(strs) or remain_zero + remain_one==0:
                return 0
            if (i,remain_zero, remain_one) in dp:
                return dp[(i,remain_zero, remain_one)]
            zeroes,ones= self.findZeroesOnes(strs[i])
            
            skip=find(i+1, remain_zero, remain_one)
            consider=0
            if remain_zero-zeroes>=0 and remain_one-ones>=0:
                consider= 1 + find(i+1,remain_zero-zeroes, remain_one-ones)
            dp[(i,remain_zero, remain_one)]= max(skip, consider)
            return dp[(i,remain_zero, remain_one)]
        
        return find(0,m,n)
        
    def findZeroesOnes(self, str):
        zeroes,ones=0,0
        for char in str:
            if char =='0':
                zeroes+=1
            else:
                ones+=1
        return zeroes, ones
        