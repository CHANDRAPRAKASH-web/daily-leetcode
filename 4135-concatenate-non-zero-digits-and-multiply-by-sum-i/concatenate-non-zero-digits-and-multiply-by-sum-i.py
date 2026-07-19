class Solution:
    def sumAndMultiply(self, n: int) -> int:
        temp=0
        s=0
        place=1
        while n>0:
            c=n%10
            if c!=0:
                temp=c*place+temp
                place=place*10
                s=s+c
            n=n//10

        
        return temp*s
        