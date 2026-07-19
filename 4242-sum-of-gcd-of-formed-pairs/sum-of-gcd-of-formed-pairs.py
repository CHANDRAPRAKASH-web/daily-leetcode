class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        prefix=[]
        m=0

        for i in nums:
            if i>m:
                m=i
                prefix.append(i)
            else:
                c=gcd(i,m)
                prefix.append(c)

        prefix.sort()

        l=0
        r=len(prefix)-1

        s=0

        while l<r:
            s=s+gcd(prefix[l],prefix[r])
            l+=1
            r-=1

        return s


        