class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
            b=n
            p=1
            while b>0:
                p=p*(b%10)
                b=b//10

            if p%t==0:
                return n

            n+=1
        