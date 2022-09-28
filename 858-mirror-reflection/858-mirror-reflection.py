class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
#         (reflex+1)*q=square*p
#         (ref)*q=square*p
        ref,square=p,q
        while ref%2==0 and square%2==0:
            ref//=2
            square//=2
        if ref%2==0:
            return 2
        if square%2==1:
            return 1
        return 0