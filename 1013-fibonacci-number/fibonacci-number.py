class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        s=0

        a,b=0,1

        while n-2>=0:
            s=a+b
            a,b=b,s
            n-=1

        return s

      