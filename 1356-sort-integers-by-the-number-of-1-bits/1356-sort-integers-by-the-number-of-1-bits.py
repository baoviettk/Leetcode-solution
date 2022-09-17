class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (self.count1(x),x))
    
    def count1(self,num):
        count=0
        while num>0:
            count+=num&1
            num>>=1
        return count