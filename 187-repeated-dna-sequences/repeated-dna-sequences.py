class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        a={}
        l=0
        res=[]
        for r in range(9,len(s)):
            ss=s[l:r+1]
            a[ss]=1+a.get(ss,0)
            l+=1

        for i in a:
            if a[i]>1:
                res.append(i)

        return res
