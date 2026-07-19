class Solution:
    def sumAndMultiply(self, n: int) -> int:
        temp=0
        s=0
        temp_1=0
        while n>0:
            c=n%10
            if c!=0:
                temp=temp*10
                temp=temp+c
                s=s+c
            n=n//10

        while temp>0:
            d=temp%10
            temp_1=temp_1*10
            temp_1=temp_1+d
            temp=temp//10

        return temp_1*s
        