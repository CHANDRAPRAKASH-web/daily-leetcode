class Solution:
    def maxProduct(self, n: int) -> int:
        max1=max2=0
        while n>0:
            c=n%10
            if c>max1:
                max2=max1
                max1=c
            elif c>max2:
                max2=c

            n=n//10

        return max1*max2
       