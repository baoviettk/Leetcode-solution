class Solution(object):
    def squareSum(self, n):
        sum=0
        while n>9:
            digit= n%10
            sum+=digit*digit
            n=n/10
        return sum+n*n
    
    def isHappy(self, n):
        fast=n
        slow=n
        
        while fast!= 1 and self.squareSum(fast) !=1:
            fast= self.squareSum(self.squareSum(fast))
            slow= self.squareSum(slow)
            
            if fast==slow:
                return False
        
        return True
    
