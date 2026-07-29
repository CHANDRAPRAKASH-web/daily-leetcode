class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while n!=1 and n not in a:
            a.add(n)

            n=sum(int(i)**2 for i in str(n))

        return n==1

       