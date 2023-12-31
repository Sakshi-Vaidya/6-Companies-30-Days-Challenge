import math
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        
        def gcd(a, b):
            if (a == 0):
                return b

            if (b == 0):
                return a

            if (a == b):
                return a

            if (a > b):
                return gcd(a-b, b)
            return gcd(a, b-a)
        
        def lcm(a,b):
            return a*b//gcd(a,b)
            
        d1=divisor1
        d2=divisor2
        u1=uniqueCnt1
        u2=uniqueCnt2
        
        l=1
        r=10**(10)
        #r=7
        res=float('inf')
        while l<=r:
            m=(l+r)//2
            x=m-m//d1
            y=m-m//d2
            z=m-m//(lcm(d1,d2))
            
            if x<u1 or y<u2 or z<u1+u2:
                l=m+1
                continue
            else:
                res=min(res,m)
                r=m-1
                
            
            
       
        return res
