class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a={}
        res={}
        for i in s1:
            a[i]=1+a.get(i,0)
        l=0
        r=len(s1)-1
            
        while r<len(s2):
            res={}
            for i in range(l,r+1):
               res[s2[i]]=1+res.get(s2[i],0)
                
            if a==res:
                return True
                
                
            l+=1
            r+=1
                
        return False
                
               
        
        