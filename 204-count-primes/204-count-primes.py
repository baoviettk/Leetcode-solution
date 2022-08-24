class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        is_prime=[1]*n
        is_prime[0], is_prime[1]=0,0
        m=2
        while m*m<n:
            if is_prime[m]==1:
                is_prime[m*m:n:m]=[0]*((n-1-m*m)//m+1)
            m+=1 if m ==2 else 2
                
        return sum(is_prime)