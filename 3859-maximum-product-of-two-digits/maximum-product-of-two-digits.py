class Solution:
    def maxProduct(self, n: int) -> int:
        a=[]
        while n>0:
            a.append(n%10)
            n=n//10

        m=max(a)
        a.remove(m)
        return m * max(a)
