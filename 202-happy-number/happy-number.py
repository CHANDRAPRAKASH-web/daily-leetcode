class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        def happy(n,a):
            if n==1:
                return True
            if n in a:
                return False
            a.add(n)
            s=0
            while n>0:
                c=n%10
                s+=c*c
                n=n//10
            return happy(s,a)
        
        return happy(n,a)

        
            
