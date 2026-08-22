class Solution:
    def checkDivisibility(self, n: int) -> bool:
        b=n
        s=0
        p=1
        while b>0:
            s+=b%10
            p*=b%10
            b=b//10
        return n%(s+p)==0