class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        cur=0
        for i in range(1,n+1):
            cur=(cur+k)%i
        
        return cur+1